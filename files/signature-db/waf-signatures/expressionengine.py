#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I

def expressionengine(headers,content):
	detect = False
	detect |= search(r"Invalid GET Data",content,I) is not None
	if detect : 
		return "ExpressionEngine (EllisLab)"
