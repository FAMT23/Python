#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Date(object):

    def __init__(self, dd,mm,yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd,self.__mm,self.__yy)

    def esBisiesto(self):
        anyo = self.__yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

    def __getYY(self):
        return self.__yy

    def __setYY(self,yy):
        self.__yy = yy

    yy = property(__getYY,__setYY)
