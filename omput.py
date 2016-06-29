# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

################################################################
#
# OpenMath integer (OMI)
#
def OMInt( x ):
    omelt = Element("OMI")
    omelt.text = str(x)
    return omelt

################################################################
#
# List (list1.list)
#
def OMList( x ):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'list1', 'name' : 'list' }
    omelt.insert(1,oms)
    n = 1
    for t in x: 
        n = n + 1
        omelt.insert(n, OMelement(t))
    return omelt

################################################################
#
# OMelement
#
# Dispatches OpenMath encoding method dependently on the type of x
#
def OMelement( x ):
    t = type (x)
    if t == int:
        return OMInt(x)
    elif t == list:
        return OMList(x)

################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def OMobject( x ):
    omobj = Element("OMOBJ")
    omobj.insert(1,OMelement(x))
    return omobj

################################################################

