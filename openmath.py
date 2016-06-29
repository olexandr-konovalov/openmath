# Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

import omparse
from omparse import *

import omput
from omput import *

################################################################

def ParseOMfile(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    omobj = ParseOMroot(root)
    return omobj

def ParseOMstring(omstring):
    root = ET.fromstring(omstring)
    omobj = ParseOMroot(root)
    return omobj

################################################################

def OMstring( x ):
    return ET.tostring( OMobject( x ) ) 

def OMprint( x ):
    ET.dump( OMobject( x ) ) 

################################################################

