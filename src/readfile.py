import numpy as np
########################################################
#
#   Read input files
#
#   Author: Siddhartha Gupta
#   contact: gsiddhartha@uchicago.edu
# 
#   Last modified on July 2020
########################################################
def Read_InputFile(code, readtype, nx,ny,nz,filenumber,InputPath):

    if code == 'pluto':
       if readtype == 'data':
          return Read_PLUTO_BinaryFile(nx,ny,nz,filenumber,InputPath)
       if readtype == 'grid':
          return Read_PLUTO_GridFile(nx,ny,nz,filenumber,InputPath)
    else:
       print('Simulation code is undetected!')
       return None

########################################################
#    Following functions read 'DBL' file.
########################################################
def  Read_PLUTO_BinaryFile(nx,ny,nz,filenumber,InputPath):

     filename="%s/data.%04d.dbl"  % (InputPath,filenumber)
     
     f = open(filename, "rb")

     n = nx*ny*nz
     
     data=np.fromfile(f, dtype = 'double', count=int(n))
     #data=np.reshape(data,(nx,ny,nz))
     data=np.reshape(data,(nz,ny,nx))
     return data

def Read_PLUTO_GridFile(nx, ny, nz, filenumber,InputPath):
   
    filename  = "%s/grid.out"  % (InputPath)
    filename2 = "%s/tgrid.txt" % (InputPath)

    file1 = open(filename, 'r') 
    Lines = file1.readlines() 

    lbeg = 10 # starting line
    nx1 = (int) (Lines[lbeg])
    nx2 = (int) (Lines[lbeg +nx1+1])
    nx3 = (int) (Lines[lbeg +nx1+1 +nx2+1])

    if (nx != nx1 or ny != nx2 or nz != nx3):
      print(">> Please set your grid numbers Nx1, Nx2, Nx3 in user_input.py correctly.")
      print(">> Error: specified grid:[%d,%d,%d] but actual [%d,%d,%d]" % (nx,ny,nz,nx1,nx2,nx3))
      exit()
    
    file = open(filename2, 'w')

    for i in range(lbeg+1, lbeg +nx1+1, 1):
      file.write('%s' % (Lines[i]))

    for i in range(lbeg+ nx1+2, lbeg +nx1+1 +nx2+1, 1):
      file.write('%s' % (Lines[i]))

    for i in range(lbeg +nx1+1 +nx2+2, lbeg +nx1+1 +nx2 +nx3+2, 1):
      file.write('%s' % (Lines[i]))

    file.close()

    f1 = np.loadtxt(filename2)
      
    x1_beg, x1_len = 0, nx
    x2_beg, x2_len = nx, nx+ny
    x3_beg, x3_len = nx+ny, nx+ny+nz

    X1g = 0.5*(f1[x1_beg:x1_len,1]+f1[x1_beg:x1_len,2])
    X2g = 0.5*(f1[x2_beg:x2_len,1]+f1[x2_beg:x2_len,2])
    X3g = 0.5*(f1[x3_beg:x3_len,1]+f1[x3_beg:x3_len,2])

    return X1g, X2g, X3g

########################################################
#   Add functions to read other data types
########################################################



########################################################
#   A sample file for adding star particles
########################################################

def Read_Particles(filenumber,InputPath):
    # Format: #no, x, y, z
    filename = "%s/stars.%04d.txt" % (InputPath,filenumber)
    X = np.loadtxt(filename)
    return X



