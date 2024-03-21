#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fecha, hora

class DateTime(fecha.Date,hora.Time):

    def __init__(self,dd=0,MM=0,yy=0,hh=0,mm=0,ss=0):
        fecha.Date.__init__(self,dd,MM,yy)
        hora.Time.__init__(self,hh,mm,ss)

    def __str__(self):
        return fecha.Date.__str__(self) + " " + hora.Time.__str__(self)

print (__name__)
