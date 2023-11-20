# Web Scraping in Python

# Web scraping - process of extracting, copying and screening of data from the web
'''
HTML - hyperText Markup Language for documents designed to displayed in a web browser
CSS - another language used to define the look and feel of HTML documents
'''
'''
Markup Language - are used to annotate text so that a computer can understand it
<!DOCTYPE html> - tells that it is html document so read it as html document
'''
# id are unique not class are not

# Beautiful Soup - python package for parsing HTML and XML documents
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p class = 'subtitle' >This is a paragraph.</p>
<p class = 'star-rating Three'>Data</p>
<ul>
    <li>Agrima</li>
    <li>Jennifer</li>
    <li>Amaira</li>
    <li>Niyati</li>
</body>
</html>'''
import re
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
print(simple_soup.find('h1').string) # This is a Heading
''' find - gives you one whereas findall gives you all'''

def list_items():
    list_item = simple_soup.find_all('li')
    element = [ele.string for ele in list_item]
    print(element)
list_items()

# to find a tag with class
simple_soup.find('p', {'class': 'subtitle'}) # takes dictionary

# to find a all tags without that class name
para = simple_soup.find_all('p')
other_para = [ele for ele in para if 'subtitle' not in ele.attrs.get('class', [])] # [] instead of None so that it returns empty list for comparison if class name does not match

class ParsedItemLocators:
    NAME_LOCATOR = 'article p.star-rating'

class ParsedItem:
    def __init__(self, page):
          self.simple_soup = BeautifulSoup(page, 'html.parser')

    def find_item_name(self):
        locator = 'article.class_name h3 a' # called CSS locator # we want to find content which is inside article attribute then h3 and a
        item_link = self.simple_soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    def find_item_price(self):
        locator = 'article.product p.price_colour'
        item_price = self.simple_soup.select_one(locator).attrs['href']

        pattern = '$([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        # print(matcher.group(0)) # with symbols
        return matcher.group(1) # value

    # ques - <p class = 'star-rating Three'> for class three
    def find_item(self):
        #text =  BeautifulSoup(SIMPLE_HTML, 'html.parser')
        locator = ParsedItemLocators.NAME_LOCATOR
        star_rating_tag = self.simple_soup.select_one(locator)
        classes = star_rating_tag.attrs['class'] # will give  ['star-rating, 'Three'] - order can be anything
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating = [i for i in classes if i != 'star-rating']
        return rating[0]
    
item = ParsedItem(SIMPLE_HTML)
print(item.find_item())


# REQUESTS
'''
requests module allows you to send HTTP requests using python
the HTTP request returns a Response Object with all the response data (content, encoding, status) 
'''
import requests

page = requests.get('http://www.example.com') # converts the response to object
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('h1').string)
