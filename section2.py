#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:06:35 2018

@author: arry
"""

import json
import pip

failedPackages = []
with open('dependencies.json') as f:
    data = json.load(f)
for package in data['Dependencies']:
    print(package)
    try:
        pip.main(['install', package])
    except:
        failedPackages.append(package)
if(len(failedPackages)):
    for package in failedPackages:
        print(package + " failed to install")
else:
    print("Success")