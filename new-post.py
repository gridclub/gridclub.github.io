#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2017 KG

"""

$ python new-post "title of the post"

or, new-post can be executed directly,

$ new-post "title of the post"

"""

import argparse
import time
import uuid

def main():
    parser = argparse.ArgumentParser(description='Jekyll Post')
    parser.add_argument('title', help='The title of the post.')
    #parser.add_argument('category', help='The categores of the post.')
    #parser.add_argument('--tag', help='The tags of the post.')
    args = parser.parse_args()
    
    title = args.title
    categories = "" #args.category
    tags = "" #args.tag if args.tag else args.category

    name, date = time.strftime('%Y-%m-%d') + '-' + title.replace(' ','-') + '.md', time.strftime('%Y-%m-%d %H-%M-%S %z')

    path = "_posts/" + name

    yaml = '''---
layout: post
title: "%s"
date: %s
categories: %s
tags: %s
---'''
    post = yaml % (title, date, categories, tags, disqus_identifier)
    fp = None
    try:
        fp = open(path, 'w')
        fp.write(post)
    finally:
        if fp:
            fp.close()

if __name__ == '__main__':
    main()
