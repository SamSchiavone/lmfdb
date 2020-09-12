# -*- coding: utf-8 -*-
import os, yaml, re
from sidebar import linked_name

# note that some of the headings are multilevel, meaning you have to go down one more level before getting other tags, e.g., status
# actually, Drew is editing the sidebar now, so I think there will be separate main and beta sidebars

def make_categories(status):
    _curdir = os.path.dirname(os.path.abspath(__file__))
    #toc = yaml.load(open("sidebar.yaml"), Loader=yaml.FullLoader)
    if status == 'prod':
        toc = yaml.load(open(os.path.join(_curdir, "sidebar.yaml")), Loader=yaml.FullLoader)
    elif status == 'beta':
        toc = yaml.load(open(os.path.join(_curdir, "betasidebar.yaml")), Loader=yaml.FullLoader)
    else:
        raise ValueError("Invalid value for status")
    bad = [re.compile(r'^\d+intro'), re.compile(r'^\d+L-functions'), re.compile(r'^\d+Know'), re.compile(r'^\d+Inv')]
    categories = []
    for c in list(toc):
        add_me = True
        for b in bad:
            if b.match(c):
                add_me = False
        if add_me:
            categories.append(c)
    return categories, toc

def get_random_obj(status):
    categories, toc = make_categories(status)
    cat = categories[randint(0,len(categories)-1)]
    # then cat['parts']?
