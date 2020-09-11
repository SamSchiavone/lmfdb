# -*- coding: utf-8 -*-
import os, yaml, re
from sidebar import linked_name

#_curdir = os.path.dirname(os.path.abspath(__file__))
#toc = yaml.load(open("sidebar.yaml"), Loader=yaml.FullLoader)
headings = list(toc.keys())
self.toc_dic = yaml.load(open(os.path.join(_curdir, "sidebar.yaml")), Loader=yaml.FullLoader)

bads = [re.compile(r'^\d+intro'), re.compile(r'^\d+L-functions'), re.compile(r'^\d+Know'), re.compile(r'^\d+Inv')]

# note that some of the headings are multilevel, meaning you have to go down one more level before getting other tags, e.g., status
