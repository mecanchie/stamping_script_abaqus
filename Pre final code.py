# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import time
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import numpy
import odbAccess
from odbAccess import openOdb

import __main__


# Stamping Settings

blankHolderRadius = [5]
punchRadius = [5]
holderForce = [90000]
punchDisp=[60]
t = [1.0]


def Blank_Holder(count):
    s1 = mdb.models['Model-' + str(count)].ConstrainedSketch(name='__profile__', 
        sheetSize=1000.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(160.0, 140.0))
    s1.FixedConstraint(entity=v[0])
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-56.1858825683594, 
        51.9852905273438), value=50.0)
    s1.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(83.5055847167969, 
        -24.1911773681641), value=65.0)
    s1.FilletByRadius(radius=blankHolderRadius[0], curve1=g[2], nearPoint1=(-1.54641723632812, 
        19.5588073730469), curve2=g[5], nearPoint2=(19.072265625, 
        0.514694213867188))
    p = mdb.models['Model-' + str(count)].Part(name='Blank_Holder', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-' + str(count)].parts['Blank_Holder']
    p.AnalyticRigidSurf2DPlanar(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-' + str(count)].parts['Blank_Holder']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-' + str(count)].sketches['__profile__']

def Blank(count):
    s1 = mdb.models['Model-' + str(count)].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(48.75, 0.0))
    s1.HorizontalConstraint(entity=g[2], addUndoState=False)
    s1.FixedConstraint(entity=v[0])
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(22.2239456176758, 
        10.7854957580566), value=143.56)
    p = mdb.models['Model-' + str(count)].Part(name='Blank', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-' + str(count)].parts['Blank']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-' + str(count)].sketches['__profile__']


def Die(count):
    s = mdb.models['Model-' + str(count)].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Spot(point=(0.0, 0.0))
    s.Spot(point=(80.0, 0.0))
    s.Spot(point=(0.0, 80.0))
    s.Spot(point=(80.0, 80.0))
    s.Line(point1=(0.0, 80.0), point2=(80.0, 80.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(80.0, 80.0), point2=(80.0, 0.0))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(80.0, 0.0), point2=(0.0, 0.0))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(0.0, 0.0), point2=(0.0, 80.0))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.FilletByRadius(radius=10.0, curve1=g[2], nearPoint1=(74.4298248291016, 
        80.2981185913086), curve2=g[3], nearPoint2=(79.53955078125, 
        75.8002853393555))
    p = mdb.models['Model-' + str(count)].Part(name='Die', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-' + str(count)].parts['Die']
    p.AnalyticRigidSurf2DPlanar(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-' + str(count)].parts['Die']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-' + str(count)].sketches['__profile__']


def PunchGeometry(count,p_r):
    s1 = mdb.models['Model-' + str(count)].ConstrainedSketch(name='__profile__', 
        sheetSize=100.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(0.0, 16.0))
    s1.VerticalConstraint(entity=g[2], addUndoState=False)
    s1.Line(point1=(0.0, 0.0), point2=(14.0, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(3.34565353393555, 
        -5.09044933319092), value=30.0)
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-1.26729583740234, 
        7.67365837097168), value=80.0)
    s1.FilletByRadius(radius=p_r, curve1=g[3], nearPoint1=(3.24427032470703, 
        -0.0253257751464844), curve2=g[2], nearPoint2=(-0.152076721191406, 
        2.6085376739502))
    p = mdb.models['Model-' + str(count)].Part(name='Punch',  dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-' + str(count)].parts['Punch']
    p.AnalyticRigidSurf2DPlanar(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-' + str(count)].parts['Punch']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-' + str(count)].sketches['__profile__']

def blankMaterial(count):
    mdb.models['Model-' + str(count)].Material(name='Material_Blank')
    mdb.models['Model-' + str(count)].materials['Material_Blank'].Elastic(table=((210000.0, 
        0.3), ))
    mdb.models['Model-' + str(count)].materials['Material_Blank'].Plastic(scaleStress=None, 
        table=((400.0, 0.0), (461.8498989, 0.02), (476.1461575, 0.04), (
        485.9954297, 0.06), (493.7469165, 0.08), (500.2374467, 0.1), (
        505.8727928, 0.12), (510.883878, 0.14), (515.4159925, 0.16), (
        519.5671141, 0.18), (523.4067725, 0.2), (526.9862797, 0.22), (
        530.3446974, 0.24), (551.9315586, 0.4)))
    


def Assembly(count, t_s):
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    p = mdb.models['Model-' + str(count)].parts['Blank']
    a1.Instance(name='Blank-1', part=p, dependent=ON)
    p = mdb.models['Model-' + str(count)].parts['Blank_Holder']
    a1.Instance(name='Blank_Holder-1', part=p, dependent=ON)
    p = mdb.models['Model-' + str(count)].parts['Punch']
    a1.Instance(name='Punch-1', part=p, dependent=ON)
    p = mdb.models['Model-' + str(count)].parts['Die']
    a1.Instance(name='Die-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=302.916, 
        farPlane=354.466, width=256.414, height=119.865, viewOffsetX=-4.28003, 
        viewOffsetY=-9.362)
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Blank-1', ), vector=(-113.56, -0.5*t_s-0.6, 0.0))
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Blank_Holder-1', ), vector=(-66.0, 0.0, 0.0))
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Die-1', ), vector=(-81.0, -80.0-t_s-1.2, 0.0))

def Steps(count):
    mdb.models['Model-' + str(count)].StaticStep(name='ApplyHolderForce', previous='Initial', 
        maxNumInc=1000, initialInc=0.1, nlgeom=ON)
    mdb.models['Model-' + str(count)].StaticStep(name='ApplyPunchDisp', 
        previous='ApplyHolderForce', maxNumInc=1000, initialInc=0.1)
    mdb.models['Model-' + str(count)].StaticStep(name='RemovePunch', previous='ApplyPunchDisp', 
        maxNumInc=1000, initialInc=0.1, maxInc=0.1)


def ReferencePoint(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    v1 = a.instances['Die-1'].vertices
    a.ReferencePoint(point=v1[1])
    a = mdb.models['Model-'+ str(count)].rootAssembly
    e1 = a.instances['Blank_Holder-1'].edges
    a.ReferencePoint(point=a.instances['Blank_Holder-1'].InterestingPoint(
        edge=e1[3], rule=MIDDLE))
    a = mdb.models['Model-' + str(count)].rootAssembly
    v11 = a.instances['Punch-1'].vertices
    a.ReferencePoint(point=v11[0])



def Constraint(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    a.regenerate()
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[9], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].RigidBody(name='Constraint-Die', refPointRegion=region1, 
        surfaceRegion=region5)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[11], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].RigidBody(name='Constraint-Punch', 
        refPointRegion=region1, surfaceRegion=region5)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].RigidBody(name='Constraint-Holder', 
        refPointRegion=region1, surfaceRegion=region5)
    

def interaction_properties(count):
    mdb.models['Model-' + str(count)].ContactProperty('IntProp-1')
    mdb.models['Model-' + str(count)].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-' + str(count)].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)


def interaction(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-' + str(count)].SurfaceToSurfaceContactStd(name='Blank_Holder', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-' + str(count)].SurfaceToSurfaceContactStd(name='Die_Blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-' + str(count)].SurfaceToSurfaceContactStd(name='punch_Blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)



def BCDispHolder(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region = a.Set(referencePoints=refPoints1, name='DispHolder')
    mdb.models['Model-' + str(count)].DisplacementBC(name='DispHolder', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Model-' + str(count)].boundaryConditions['DispHolder'].setValuesInStep(
        stepName='ApplyHolderForce', u2=FREED)


def BCEncDie(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[9], )
    region = a.Set(referencePoints=refPoints1, name='EncDie')
    mdb.models['Model-' + str(count)].DisplacementBC(name='EncDie', createStepName='Initial', 
        region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)

def BCDispPunch(count,p_d):
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[11], )
    region = a.Set(referencePoints=refPoints1, name='DispPunch')
    mdb.models['Model-' + str(count)].DisplacementBC(name='DispPunch', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Model-' + str(count)].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='ApplyPunchDisp', u2=-p_d)
    mdb.models['Model-' + str(count)].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='RemovePunch', u2=0.0)

def BCAdd(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    v1 = a.instances['Blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(vertices=verts1, name='Add')
    mdb.models['Model-' + str(count)].DisplacementBC(name='Add', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)

def BCBlank(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    a = mdb.models['Model-' + str(count)].rootAssembly
    v1 = a.instances['Blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Set(vertices=verts1, name='Blank_set')
    mdb.models['Model-1'].XsymmBC(name='Blank_set', createStepName='Initial', 
        region=region, localCsys=None)



def Mesh(count):
    p = mdb.models['Model-' + str(count)].parts['Blank']
    p = mdb.models['Model-' + str(count)].parts['Blank']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=200, constraint=FINER)
    elemType1 = mesh.ElemType(elemCode=B21, elemLibrary=STANDARD)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(edges, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    p = mdb.models['Model-' + str(count)].parts['Blank']
    p.generateMesh()



def bcs(count,p_d,h_f):
    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[9], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].DisplacementBC(name='DispDie', createStepName='Initial', 
        region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    

    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[11], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].DisplacementBC(name='DispPunch', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    

    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-' + str(count)].DisplacementBC(name='DispHolder', 
        createStepName='Initial', region=region, u1=SET, u2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    

    a = mdb.models['Model-' + str(count)].rootAssembly
    v1 = a.instances['Blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = regionToolset.Region(vertices=verts1)
    mdb.models['Model-' + str(count)].XsymmBC(name='Symmetry', createStepName='Initial', 
        region=region, localCsys=None)
    #Free dispHolder for next steps 
    mdb.models['Model-' + str(count)].boundaryConditions['DispHolder'].setValuesInStep(
        stepName='ApplyHolderForce', u2=FREED)
    
    #Moving the punch
    mdb.models['Model-' + str(count)].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='ApplyPunchDisp', u2=-p_d)
    mdb.models['Model-' + str(count)].boundaryConditions['DispPunch'].setValuesInStep(
        stepName='RemovePunch', u2=0.0)
    

    a = mdb.models['Model-' + str(count)].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[10], )
    region = regionToolset.Region(referencePoints=refPoints1)

    #Applying force on Holder
    mdb.models['Model-' + str(count)].ConcentratedForce(name='Load-1', 
        createStepName='ApplyHolderForce', region=region, cf2=-h_f, 
        distributionType=UNIFORM, field='', localCsys=None)
    
    a = mdb.models['Model-' + str(count)].rootAssembly
    v1 = a.instances['Blank-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(vertices=verts1)
    mdb.models['Model-' + str(count)].DisplacementBC(name='add', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)


def Section(count,t_s):
    mdb.models['Model-' + str(count)].RectangularProfile(name='Profile-1', a=300.0, b=t_s)
    mdb.models['Model-' + str(count)].BeamSection(name='Section-1', 
        integration=DURING_ANALYSIS, poissonRatio=0.0, profile='Profile-1', 
        material='Material_Blank', temperatureVar=LINEAR, 
        consistentMassMatrix=False)
    p1 = mdb.models['Model-' + str(count)].parts['Blank']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(edges=edges)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

def BeamOrientationJob(count):
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-' + str(count)].parts['Blank']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region=regionToolset.Region(edges=edges)
    p = mdb.models['Model-' + str(count)].parts['Blank']
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
        -1.0))
    a = mdb.models['Model-' + str(count)].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.Job(name='Job-'+ str(count), model='Model-' + str(count), description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
        multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
    

def translate(count):
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    e2 = a1.instances['Die-1'].edges
    e1 = a1.instances['Blank_Holder-1'].edges
    a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[2], flip=OFF, clearance=0.0)
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    e2 = a1.instances['Blank_Holder-1'].edges
    e1 = a1.instances['Punch-1'].edges
    a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[1], flip=ON, clearance=0.0)
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Die-1', ), vector=(0.0, 1.2, 0.0))  
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Blank-1', ), vector=(-0.2, 0.6, 0.0))  
    a1 = mdb.models['Model-' + str(count)].rootAssembly
    a1.translate(instanceList=('Punch-1', ), vector=(-0.2, 0.0, 0.0))


def interactionChange(count):
    a = mdb.models['Model-' + str(count)].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-' + str(count)].interactions['Blank_Holder'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side2Edges=side2Edges1)
    mdb.models['Model-' + str(count)].interactions['Die_Blank'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-' + str(count)].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-' + str(count)].interactions['punch_Blank'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)


def PostProcessing(p_r, h_f,t_s,disp,count):
	
	odbname = 'Job-'+ str(count)
	path = './'
	odbpath = path+odbname+'.odb'
	odb = openOdb(odbpath)
	All_points1 = odb.steps['ApplyPunchDisp'].frames[-1].fieldOutputs['S'].values
	All_points2 = odb.steps['ApplyPunchDisp'].frames[-1].fieldOutputs['PEEQ'].values
	Mises_Stress=[]
	Plastic_Strain = []
	for i in range (0, len(All_points1)):
		VM = All_points1[i].mises
		Mises_Stress.append(VM)
	for i in range (0, len(All_points2)):
		PS = All_points2[i].data
		Plastic_Strain.append(PS)

	max_Stress = max(Mises_Stress)
	max_Strain = max(Plastic_Strain)
	outfile = open('Results.txt','a')
	outfile.write('\n'+ str(p_r) + ',' + str(h_f) + ',' + str(t_s) + ',' + str(max_Stress)+',' + str(disp)+','+str(max_Strain))
	odb.close()
	outfile.close()


outfile = open('Results.txt','w')
outfile.write('\nPunch radius (mm),Holder Force (N),Thickness(mm),Max. Stress (MPa),Punching displacement(mm),Max.Strain')
outfile.close()

count = 0
for i1 in range(0, len(punchRadius)):
	for j1 in range(0, len(punchDisp)):
		for k1 in range(0,len(holderForce)):
			for l1 in range(0, len(t)):
				count+=1
				if count >=2:
					mdb.Model(name='Model-'+ str(count), modelType=STANDARD_EXPLICIT)
    				session.viewports['Viewport: 1'].setValues(displayedObject=None)

				Blank_Holder(count)
				Blank(count)
				Die(count)
				PunchGeometry(count,punchRadius[i1])

				blankMaterial(count)

				Assembly(count,t[l1])
				ReferencePoint(count)
				Constraint(count)

				interaction_properties(count)
				interaction(count)


				Steps(count)

				boundaryConditions = True
				if(boundaryConditions):
    					bcs(count,punchDisp[j1],holderForce[k1])
				Mesh(count)
				Section(count,t[l1])
				BeamOrientationJob(count)
				translate(count)
				interactionChange(count)
		
				if count >=2:
					mdb.Job(name='Job-'+str(count), model='Model-'+ str(count), description='', type=ANALYSIS, 
       		 			atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        	 			memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        				explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        				modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        				scratch='', resultsFormat=ODB)

				mdb.jobs['Job-'+ str(count)].submit(consistencyChecking=OFF)
				time.sleep(240) # change the time for your computer 

				PostProcessing(punchRadius[i1],holderForce[k1],t[l1],punchDisp[j1],count)
		
		





