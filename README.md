# homepage
home_html_to_csv.py converts simple html to a csv file.
home_csv_to_html.py sorts the content and convert them to a html file.
I use home_html_to_csv.py to convert my urls to cvs once. Then I will add url to csv 
file whenever I found a useful link and use home_csv_to_html.py to sort them and produce
a clean home.html.


Dependence:
We use Beautiful Soup to convert html to dictionary like object. 
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

Usage:
chomd u+x home_html_to_csv.py home_csv_to_html.py.
./home_html_to_csv.py -i home.html -o home.csv
./home_csv_to_html.py -i home.csv -o home.html


Tests:
./home_html_to_csv.py -i simple_home.html -o simple_home.csv
./home_csv_to_html.py -i simple_home.csv -o sorted_simple_home.html
