# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:40:09 2015

@author: ramku
"""

import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('/Users/ramku/Documents/Personal/DataScience/Github/Mongodb/exampleResearchArticle.xml')

root = tree.getroot()

print "children of root :"
for child in root:
        print child.tag
        