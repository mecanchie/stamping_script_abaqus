# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def bcs():
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[9], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='DispDie', createStepName='Initial', 
        region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    

    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[11], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='DispPunch', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    

    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='DispHolder', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    

    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = regionToolset.Region(vertices=verts1)
    mdb.models['Model-1'].XsymmBC(name='Symmetry', createStepName='Initial', 
        region=region, localCsys=None)
    #Free dispHolder for next steps 
    mdb.models['Model-1'].boundaryConditions['DispHolder'].setValuesInStep(
        stepName='ApplyHolderForce', u2=FREED)
    
    #Moving the punch
    mdb.models['Model-1'].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='ApplyPunchDisp', u2=-60.0)
    mdb.models['Model-1'].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='RemovePunch', u2=0.0)
    

    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region = regionToolset.Region(referencePoints=refPoints1)

    #Applying force on Holder
    mdb.models['Model-1'].ConcentratedForce(name='Load-1', 
        createStepName='ApplyHolderForce', region=region, cf2=-90000.0, 
        distributionType=UNIFORM, field='', localCsys=None)


