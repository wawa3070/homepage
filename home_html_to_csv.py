#!/usr/bin/python
from bs4 import BeautifulSoup
import csv, sys, getopt
# This script is based on using <br><b>category</b> and <a>url</a>.


def main(argv):
  """ Usage home_html_to_csv.py -i intput.html -o output.cvs """

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
   
  # Load home.html.
  with open(input_file, 'r') as html_file:
    html_content = html_file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

  # Convert to a table
  category = ""
  urls = list()
  category_to_urls = dict()
  for element in soup.body.find_all(['br','a']):
    # Create new category.
    if element.b:
      if category:
        category_to_urls[category] = urls
      category = element.b.string
      urls = list()
    elif 'href' in element.attrs:
      urls.append((element.string, element['href'])) 
  category_to_urls[category] = urls


  # Write to an cvs file with columns category, name, url.
  with open(output_file, 'wb') as csv_file:
    field_names = ['category', 'name', 'url']
    writer = csv.DictWriter(csv_file, field_names)
    writer.writeheader()
    for category, urls in category_to_urls.iteritems():
      for name_url in urls:
        writer.writerow({'category': category, 'name': name_url[0], 'url': name_url[1]})

if __name__ == "__main__":
  main(sys.argv[1:])
