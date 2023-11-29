# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__


def ReferencePoint():
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Die-1'].vertices
    a.ReferencePoint(point=v1[0])
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['BlankHolder-1'].edges
    a.ReferencePoint(point=a.instances['BlankHolder-1'].InterestingPoint(
        edge=e1[3], rule=MIDDLE))
    a = mdb.models['Model-1'].rootAssembly
    v11 = a.instances['Punch-1'].vertices
    a.ReferencePoint(point=v11[0])


def Constraint():
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=a.Surface(side2Edges=side2Edges1, name='Surf-10')
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[34], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='die_constraint', refPointRegion=region1, 
        surfaceRegion=region5)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region5=a.Surface(side2Edges=side2Edges1, name='Surf-11')
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[36], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='punch_constraint', 
        refPointRegion=region1, surfaceRegion=region5)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['BlankHolder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=a.Surface(side2Edges=side2Edges1, name='Surf-12')
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[35], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='blank_holder_constraint', 
        refPointRegion=region1, surfaceRegion=region5)


