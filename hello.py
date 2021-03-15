#!/usr/bin/env python
# -*-coding:utf-8-*-
# File Name     : hello.py
# Description   :
# Author        :
# Creation Date : 2021-03-15
# Last Modified : Mon 15 Mar 2021 04:26:41 PM CST
# Created By    : lsl
import os

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
print("hello world!")
print(username, password)
