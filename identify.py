# identify.py

# Purpose: Identify poems on www.internal.org written by Robert Frost and
# collect their links.

# Input

# Output

# Imports
import requests
from lxml import html
import re

# www.internal.org puts all RF poems on the following link

website = 'http://www.internal.org/robert_frost'

# The following lines collect the html page.
page = requests.get(website)
tree = html.fromstring(page.content)

# Collect links to poems
link_list = []
for link in tree.xpath('//a/@href'):
    if re.search("\/Robert_Frost\/", link) is not None:
        link_list.append(link)

# Add the site's name to links for scraping.
for i in range(len(link_list)):
    link_list[i] = 'www.internal.org' + link_list[i]
print link_list
