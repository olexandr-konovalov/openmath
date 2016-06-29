################################################################
#
# Parsing OpenMath objects
# 

################################################################
#
# Basic OpenMath elements
#

# OpenMath integer
def ParseOMI(node):
    return int(node.text)
    

################################################################
#
# OpenMath content dictionaries
#
omdicts = {}

# list1    http://www.openmath.org/cd/list1.xhtml
omdicts['list1'] = {}

# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list


# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# logic1.true
omdicts['logic1']['true'] = True


################################################################

def ParseOMS(node):
    # returns a function or an object
    return omdicts[ node.get('cd') ][ node.get('name') ]

def ParseOMA(node):
    elts = []
    for child in node.findall("*"):
        elts.append( ParseOMelement(child) )
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:len(elts)]) 

ParseOMelementHandler = { 'OMI' : ParseOMI, 'OMS' : ParseOMS, 'OMA' : ParseOMA }

def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)

def ParseOMroot(root):
    return ParseOMelement(root[0])


################################################################
