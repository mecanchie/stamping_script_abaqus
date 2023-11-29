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
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior


import __main__

def Blank_Holder():
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
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
    p = mdb.models['Model-1'].Part(name='Blank_Holder', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts['Blank_Holder']
    p.AnalyticRigidSurf2DPlanar(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Blank_Holder']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

def Blank():
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(48.75, 0.0))
    s1.HorizontalConstraint(entity=g[2], addUndoState=False)
    s1.FixedConstraint(entity=v[0])
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(22.2239456176758, 
        10.7854957580566), value=143.56)
    p = mdb.models['Model-1'].Part(name='Blank', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Blank']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Blank']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def Die():
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
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
    p = mdb.models['Model-1'].Part(name='Die', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts['Die']
    p.AnalyticRigidSurf2DPlanar(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Die']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def PunchGeometry():
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
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
    s1.FilletByRadius(radius=5.0, curve1=g[3], nearPoint1=(3.24427032470703, 
        -0.0253257751464844), curve2=g[2], nearPoint2=(-0.152076721191406, 
        2.6085376739502))
    p = mdb.models['Model-1'].Part(name='Punch',  dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts['Punch']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Punch']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

def blankMaterial():
    mdb.models['Model-1'].Material(name='Material_Blank')
    mdb.models['Model-1'].materials['Material_Blank'].Elastic(table=((210000.0, 
        0.3), ))
    mdb.models['Model-1'].materials['Material_Blank'].Plastic(scaleStress=None, 
        table=((400.0, 0.0), (461.8498989, 0.02), (476.1461575, 0.04), (
        485.9954297, 0.06), (493.7469165, 0.08), (500.2374467, 0.1), (
        505.8727928, 0.12), (510.883878, 0.14), (515.4159925, 0.16), (
        519.5671141, 0.18), (523.4067725, 0.2), (526.9862797, 0.22), (
        530.3446974, 0.24), (551.9315586, 0.4)))
    


def Assembly():
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Blank']
    a1.Instance(name='Blank-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Blank_Holder']
    a1.Instance(name='Blank_Holder-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Punch']
    a1.Instance(name='Punch-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Die']
    a1.Instance(name='Die-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=302.916, 
        farPlane=354.466, width=256.414, height=119.865, viewOffsetX=-4.28003, 
        viewOffsetY=-9.362)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Blank-1', ), vector=(-113.56, -1.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Blank_Holder-1', ), vector=(-66.0, 0.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Die-1', ), vector=(-81.0, -82.0, 0.0))

def Steps():
    mdb.models['Model-1'].StaticStep(name='ApplyHolderForce', previous='Initial', 
        maxNumInc=1000, initialInc=0.1, nlgeom=ON)
    mdb.models['Model-1'].StaticStep(name='ApplyPunchDisp', 
        previous='ApplyHolderForce', maxNumInc=1000, initialInc=0.1)
    mdb.models['Model-1'].StaticStep(name='RemovePunch', previous='ApplyPunchDisp', 
        maxNumInc=1000, initialInc=0.1, maxInc=0.1)


def ReferencePoint():
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Die-1'].vertices
    a.ReferencePoint(point=v1[1])
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Blank_Holder-1'].edges
    a.ReferencePoint(point=a.instances['Blank_Holder-1'].InterestingPoint(
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
    mdb.models['Model-1'].RigidBody(name='Die_constraint', refPointRegion=region1, 
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
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region5=a.Surface(side2Edges=side2Edges1, name='Surf-12')
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[35], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Blank_Holder_constraint', 
        refPointRegion=region1, surfaceRegion=region5)
    
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
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Blank_Holder', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Die_Blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='punch_Blank', 
        createStepName='Initial', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)






blankHolderRadius = [5]


Blank_Holder()
Blank()
Die()
PunchGeometry()

blankMaterial()

Assembly()
ReferencePoint()
#Constraint()

interaction_properties()
#interaction()


Steps()

