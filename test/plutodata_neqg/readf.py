import numpy as np

def Read_PLUTO_GridFile(nx, ny, nz, filenumber,InputPath):
   
    filename  = "%/grid.out"  % (InputPath)
    filename2 = "%/tgrid.txt" % (InputPath)

    file1 = open(filename, 'r') 
    Lines = file1.readlines() 

    lbeg = 10 # starting line
    nx1 = (int) (Lines[lbeg])
    nx2 = (int) (Lines[lbeg +nx1+1])
    nx3 = (int) (Lines[lbeg +nx1+1 +nx2+1])

    print(nx1,nx2,nx3)
    
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

    print(X1g)
    print(X2g)
    print(X3g)
    


nx, ny, nz = 200, 60, 80
Read_PLUTO_GridFile(nx, ny, nz, '10', 'a')

