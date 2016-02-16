#!/usr/bin/python
from bs4 import BeautifulSoup
from csv import DictReader
from collections import OrderedDict
import sys, getopt    

# This script is based on using <br><b>category</b> and <a>url</a>.
# Columns of the csv file is assumed to be 'category', 'name', 'url'.

def AddToCategoryToUrls(table, category, name, url):
  """ Add to a table of list of name and url pairs. table key is category """
  if category in table:
    table[category].append((name, url))
  else:
    table[category] = list()
    table[category].append((name, url))

def TableToHtmlTags(table):
  category_tag = "<br><b>{}</b>"
  url_tag = "<a href={}>{}</a>"
  output = ""
  for category, urls in table.iteritems():
    output += (category_tag.format(category) + "\n")
    for url in urls:
      output += (url_tag.format(url[1], url[0]) + "\n")
    output += "<br>\n"
  return output

def SortUrls(table):
  """ Sort urls based on the name of the url. """
  output = dict()
  for category, urls in table.iteritems():
    output[category] = sorted(urls, key = lambda tup: tup[0])
  return output

def main(argv):
  """ Usage home_csv_to_html.py -i intput.csv -o output.html """

  input_file = ''
  output_file = ''

  # Handle flags
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    if len(opts) < 2:
      raise ValueError
  except:
    print 'home_html_to_csv.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print argv[0] + '-i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      input_file = arg
    elif opt in ("-o", "--ofile"):
      output_file = arg

  # Load home.csv.
  category_to_urls = dict()
  with open(input_file, 'rb') as csv_file:
    reader = DictReader(csv_file)
    for row in reader:
      AddToCategoryToUrls(category_to_urls, row['category'], row['name'], row['url'])

  # Sort the urls
  category_to_urls = SortUrls(category_to_urls)
  # Sort the table
  sorted_category_to_urls = OrderedDict(sorted(category_to_urls.items(), key = lambda item: item[0]))

  # Create home.html.
  with open("home_template.html") as template_file:
    template = template_file.read()
    output  = template.replace("{tags}", TableToHtmlTags(sorted_category_to_urls))
    with open(output_file, 'wb') as output_html_file:
      output_html_file.write(output)

if __name__ == "__main__":
  main(sys.argv[1:])
