# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def DispHolder():
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[20], )
    region = a.Set(referencePoints=refPoints1, name='DispHolder')
    mdb.models['Model-1'].DisplacementBC(name='DispHolder', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Model-1'].boundaryConditions['DispHolder'].setValuesInStep(
        stepName='ApplyHolderForce', u2=FREED)

def DispPunch():
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[21], )
    region = a.Set(referencePoints=refPoints1, name='DispPunch')
    mdb.models['Model-1'].DisplacementBC(name='DispPunch', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Model-1'].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='ApplyPunchDisp', u2=-60.0)
    mdb.models['Model-1'].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='RemovePunch', u2=0.0)

def Add():
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(vertices=verts1, name='Add')
    mdb.models['Model-1'].DisplacementBC(name='Add', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)

def EncDie():
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[19], )
    region = a.Set(referencePoints=refPoints1, name='Enc Die')
    mdb.models['Model-1'].DisplacementBC(name='EncDie', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)

def Blank():
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Set(vertices=verts1, name='Blank')
    mdb.models['Model-1'].XsymmBC(name='Blank', createStepName='Initial', 
        region=region, localCsys=None)


