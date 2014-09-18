import opengm
import numpy
#---------------------------------------------------------------
# MinSum  with SelfFusion
#---------------------------------------------------------------
numpy.random.seed(42)

#gm=opengm.loadGm("/home/tbeier/models/image-seg/3096.bmp.h5","gm")
#gm=opengm.loadGm("/home/tbeier/models/image-seg/175032.bmp.h5","gm")
#gm=opengm.loadGm("/home/tbeier/datasets/knott-3d-450/gm_knott_3d_102.h5","gm") (ROTTEN)
gm=opengm.loadGm("/home/tbeier/datasets/knott-3d-300/gm_knott_3d_072.h5","gm")
#gm=opengm.loadGm("/home/tbeier/datasets/knott-3d-150/gm_knott_3d_038.h5","gm")

#---------------------------------------------------------------
# Minimize
#---------------------------------------------------------------
#get an instance of the optimizer / inference-algorithm

print opengm.__file__

print gm



with opengm.Timer("with new method"):

    proposalParam = opengm.InfParam(
        noise = 10.1,
        stopWeight=-10.0,
        reduction=0.99
    )

    infParam = opengm.InfParam(
        numStopIt=20,
        numIt=200,
        generator='randomizedHierarchicalClustering',
        multicutFusion=True,
        proposalParam=proposalParam
    )
    inf=opengm.inference.FusionBased(gm, parameter=infParam)
    # inf.setStartingPoint(arg)
    # start inference (in this case verbose infernce)
    visitor=inf.verboseVisitor(printNth=1,multiline=False)
    inf.infer(visitor)
    arg = inf.arg()


with opengm.Timer("with multicut method"):

    infParam = opengm.InfParam(
        #workflow="(MTC)(CC)"
    )
    inf=opengm.inference.Multicut(gm, parameter=infParam)
    # inf.setStartingPoint(arg)
    # start inference (in this case verbose infernce)
    visitor=inf.verboseVisitor(printNth=1,multiline=False)
    inf.infer(visitor)
    arg = inf.arg()
