# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Mesh():
    p = mdb.models['Model-1'].parts['Blank']
    p = mdb.models['Model-1'].parts['Blank']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=200, constraint=FINER)
    elemType1 = mesh.ElemType(elemCode=B21, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Blank']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(edges, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    p = mdb.models['Model-1'].parts['Blank']
    p.generateMesh()


