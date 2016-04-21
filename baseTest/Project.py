#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

TYPE_NORMAL = 0;
TYPE_STUDIO = 1;

class ProjectDir :
    rootDir = '';
    type = TYPE_NORMAL;

def analyseType(dirPath) :
    if( os.path.isdir(dirPath) ) :
        childs = os.path.list