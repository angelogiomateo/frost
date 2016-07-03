#identify.py

#Purpose: Identify poems on w#www.internal.org written by Robert Frost and collect their links.

#Input

#Output

#Imports
import requests
from lxml import html
import re

#www.internal.org puts all RF poems on the following link
toplink = 'http://www.internal.org/robert_frost'

#The following lines collect the html page.
page = requests.get(toplink)
tree = html.fromstring(page.content)

#Collect links to poems
link_list = []
for link in tree.xpath('//a/@href'):
    if re.search("\/Robert_Frost\/",link) != None:
        link_list.append(link)

print link_list