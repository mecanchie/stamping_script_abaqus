# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Constraint():
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[9], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-Die', refPointRegion=region1, 
        surfaceRegion=region5)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[11], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-Punch', 
        refPointRegion=region1, surfaceRegion=region5)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-Holder', 
        refPointRegion=region1, surfaceRegion=region5)


