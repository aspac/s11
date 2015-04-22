# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:35:11 2015

@author: dana
"""

   
class HEX_TOOL(object):
    
    def hex_convert_from_int(self, hexstring, base):
         '''Convert a hextring with a specified base to integer'''
         return int(hex(hexstring), base)
    
    