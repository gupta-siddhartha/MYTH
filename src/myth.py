#======================================================================
# MYTH : Multipurpose code compiles YT-rendering for Hydro-simulations
#  
# Author: Siddhartha Gupta
# contact: gsiddhartha@uchicago.edu
#     
# Last modified on 17 July 2020
#======================================================================
from headers import *
from users_input import *
import timeit
start = timeit.default_timer()

print(CodeInfo)
########################################
# Creating Output directory 
########################################
dirName = "%s" % (OutputPath)
if not os.path.exists(dirName):
   os.makedirs(dirName)
   print(">> Creating directory: %s\n" % (dirName))
else:
   print(">> Directory: ", dirName ,  "already exists\n")

if PrintLog == 'yes':
   sys.stdout = open("%s/myth.log"%OutputPath, 'w')

########################################
#  Input data file main loop starts
########################################
for infilenumber in range(File_Start,File_End+1,1):

 #**************************************
 # Input data files
 #**************************************
 print(">> Input File Number:%d"%infilenumber)
 nx,ny,nz = Nx1, Nx2, Nx3
 
 #**************************************
 # Volrender info
 #**************************************
 Zoomedinout = ZoomedOperation + [infilenumber] + ZoomingInfo
 RenderingOperation=Zoomedinout+Rotation 

 #**************************************
 #      Reading input data file
 #**************************************

 if FreshRead == 'yes':
  data     = readfile.Read_InputFile(simulation, 'data', nx,ny,nz,infilenumber,InputPath)
  X1,X2,X3  = readfile.Read_InputFile(simulation, 'grid', nx,ny,nz,infilenumber,InputPath)

 if AddParticles == 'yes':
  Particles = readfile.Read_Particles(infilenumber,InputPath)
  Particles=Particles[:,[1,2,3]]
 else:
  Particles = [0]

 #**************************************
 # Check a data slice 
 #**************************************
 if (FreshRead == 'yes' and CheckInputData == 'yes'):
   import matplotlib.pyplot as plt
   import matplotlib as mpl
   fig,ax = plt.subplots(1,1)
   ax = fig.add_subplot(111,aspect='equal')
   ax = fig.add_subplot(111,aspect=1.0)
   ax.set_aspect('equal')
   plt.axes().set_aspect('equal')

   color_map_name = 'magma'
   if Check_slice == 'xy':
     print(data.shape)
     plt.pcolormesh(X1,X2,np.log10(data[len(X3)//2,:,:]), cmap=color_map_name) 
     plt.colorbar()
     if AddParticles == 'yes':
       plt.scatter(Particles[:,0],Particles[:,1])

   print(">> Please check at %s file:checkinput%04d.png" % (OutputPath,infilenumber))
   plt.savefig("%s/checkinput%04d.png"%(OutputPath,infilenumber))
   plt.close()

 #**************************************
 #   Convert data to uniform grid 
 #**************************************
 if FreshRead == 'yes':
  #
  if ConverToUniformGrid == 'yes':
    unidata = tools.Interpolate(Resol_x1,Resol_x2,Resol_x3,Interpolationbox,X1,X2,X3,data)
  #
  else:
    unidata = data 

  dumpfilename="%s/unigriddata%04d.txt" % (OutputPath,infilenumber) 
  print(">>Dumping data into file=%s" % dumpfilename)
  file = open(dumpfilename, "w")
  for k in range((Resol_x3)):
    for j in range((Resol_x2)):
      for i in range((Resol_x1)):
            file.write("%e\n"% (unidata[k,j,i]))
      file.write("\n")
    file.write("\n")
  file.close()
  
 else:
   dumpfilename="%s/unigriddata%04d.txt" % (OutputPath,infilenumber)
   print(">>Reading data from the file dumped previously (%s)"%(dumpfilename))
   data = np.loadtxt(dumpfilename)
   data = np.reshape(data,(Resol_x3,Resol_x2,Resol_x1))
   unidata = data

 #**************************************
 # Reshaping data for the yt project
 #**************************************
 #unidata = np.moveaxis(unidata.reshape(Resol_x3,Resol_x2,Resol_x1),0,-2)

 x1beg, x1end = Interpolationbox[1], Interpolationbox[2]
 x2beg, x2end = Interpolationbox[3], Interpolationbox[4]
 x3beg, x3end = Interpolationbox[5], Interpolationbox[6]
 x1 = np.linspace(x1beg, x1end, Resol_x1)
 x2 = np.linspace(x2beg, x2end, Resol_x2)
 x3 = np.linspace(x3beg, x3end, Resol_x3)

 #**************************************
 # Checking if interpolation is correct
 # Please see figure in output dir 
 #              checkdum.filenumber.png
 #**************************************
 if CheckInterpolation == 'yes':
   import matplotlib.pyplot as plt
   import matplotlib as mpl
   fig,ax = plt.subplots(1,1)
   ax = fig.add_subplot(111,aspect='equal')
   ax = fig.add_subplot(111,aspect=1.0)
   ax.set_aspect('equal')
   plt.axes().set_aspect('equal')

   print(unidata.shape)
   color_map_name = 'magma'
   if Check_slice == 'xy':
     #plt.pcolormesh(x1,x2,np.log10(unidata[Check_slice_number,:,:], cmap=color_map_name) 
     #vmin=np.log10(colorbound[0]),vmax=np.log10(colorbound[1]))
     plt.pcolormesh(x1,x2,np.log10(unidata[Check_slice_number,:,:]), cmap=color_map_name)
     plt.colorbar()
     if AddParticles == 'yes':
       plt.scatter(Particles[:,0],Particles[:,1])

   print(">> Please check at %s file:checkdump%04d.png" % (OutputPath,infilenumber))
   plt.savefig("%s/checkdump%04d.png"%(OutputPath,infilenumber))
   plt.close()
 
 #**************************************
 #  Volume rendering 
 #************************************** 
 # yt reads d[nx,ny,nz] instead d[nz,ny,nz], so we reshape data below
 B=np.moveaxis(unidata,2,0)
 unidata=np.moveaxis(B,1,-1)
 #Ready for performing yt-rendering
 outputfilename = "%s/volren%04d" % (OutputPath,infilenumber)
 ytrendering.VolumeRender(colorbound, RenderingOperation, outputfilename, x1,x2,x3,unidata,Particles)

 #**************************************
 # Job completed for filenumber
 #**************************************
 print(">> File: %d Completed! cheers!!!"%infilenumber)

stop = timeit.default_timer()
tools.RuntimeCalculation(start, stop)
print(">> Completed! cheers!!!")
print(Completion)
########################################
# Input data file main loop ends
########################################
