# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__


def interaction_properties():
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)


def interaction():
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['BlankHolder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='blank_holder', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='die_blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='punch_blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)


