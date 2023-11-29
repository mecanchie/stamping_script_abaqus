# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def blankmaterial():
    session.viewports['Viewport: 1'].view.setValues(nearPlane=145.737, 
        farPlane=196.023, width=253.472, height=118.49, viewOffsetX=-8.41954, 
        viewOffsetY=1.11869)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material_blank')
    mdb.models['Model-1'].materials['Material_blank'].Elastic(table=((210000.0, 
        0.3), ))
    mdb.models['Model-1'].materials['Material_blank'].Plastic(scaleStress=None, 
        table=((400.0, 0.0), (461.8498989, 0.02), (476.1461575, 0.04), (
        485.9954297, 0.06), (493.7469165, 0.08), (500.2374467, 0.1), (
        505.8727928, 0.12), (510.883878, 0.14), (515.4159925, 0.16), (
        519.5671141, 0.18), (523.4067725, 0.2), (526.9862797, 0.22), (
        530.3446974, 0.24), (551.9315586, 0.4)))


