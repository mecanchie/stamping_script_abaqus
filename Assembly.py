# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Assembly():
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Blank']
    a1.Instance(name='Blank-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Blank_Holder']
    a1.Instance(name='Blank_Holder-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Punch']
    a1.Instance(name='Punch-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['die']
    a1.Instance(name='die-1', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Blank-1', ), vector=(-113.56, -1.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Blank_Holder-1', ), vector=(-66.0, 0.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('die-1', ), vector=(-81.0, -82.0, 0.0))


