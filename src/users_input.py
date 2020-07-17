#######################################
# User's portal for MYTH
########################################

########################################
#            STEP 1 
########################################
# Input and Output directories
########################################
InputPath  = "../test/plutodata_neqg/"
OutputPath = "../test/myth-pluto-neqg/"
PrintLog   = 'no' # or 'no'
simulation = 'pluto'

########################################
#            STEP 2
########################################
File_Start    = 4
File_End      = 4
File_interval = 2 
Nx1, Nx2, Nx3 = 200, 60, 80

########################################
#            STEP 3
########################################
# Data proceesing to uniform grid
########################################
#FreshRead = yes or no:
# Fresh reading or Read from file dumped  previously (to save time) 
FreshRead = 'yes'
# ConverToUniformGrid= yes/np
ConverToUniformGrid= 'yes'
# Resol_x1, Resol_x2, Resol_x3= no of grids
Resol_x1, Resol_x2, Resol_x3 = 100, 50, 70
#Interpolationbox=['yes/no',Xmin,Xmax, Ymin,Ymax, Zmin,Zmax]
Interpolationbox=['yes',-1.0,1.0,-0.6,0.6,-0.8,0.8]
# Note: Set ConverToUniformGrid = no only when
# 'unigriddata%04d.txt must be present in OutputPath
# with Resol_x1, Resol_x2, Resol_x3 are unchanged.
########################################

########################################
#            STEP 4
########################################
# Compare input and interpolated data
########################################
CheckInputData     = 'yes'
CheckInterpolation = 'yes'
Check_slice = 'xy'
Check_slice_number = Resol_x3//2
########################################

########################################
#            STEP 5
########################################
#  Volrender info
########################################
#AddParticles = 'yes/no'
AddParticles = 'yes'
#colorbound = [density_min,density_max]
colorbound = [1e-3,10]
#ZoomedOperation = ['yes/no']
ZoomedOperation  = ['no']
#ZoomingInfo     = [Lini,Lmin,Lmax, dL ]
ZoomingInfo      = [1.5,0.2,1.5,0.01]
#Rotation = 'yes/no',angle of rotation,steps involved in 180 rotations
import numpy as np
Rotation  = ['no',np.pi,50] 

########################################
#            Complete
########################################
