import numpy as np
from scipy.ndimage import map_coordinates
####################################################################
#
#   Data interpolation
#
#   Author: Siddhartha Gupta
#   contact: gsiddhartha@uchicago.edu
# 
#   Last modified on July 2020
####################################################################

####################################################################
# Data interpolation for non-uniform grid
####################################################################
def Interpolate(resoX1, resoX2, resoX3, intpbox, X1, X2, X3, data):

    print('>> Interpolating the received data.')

    x = X1
    y = X2
    z = X3

    n1, n2, n3 = np.int(resoX1), np.int(resoX2), np.int(resoX3)

    slicenumber = n3//2
    den = np.zeros((n3,n2,n1))

    print(">> Interpolation box: x1(,),x2(,),x3(,):",intpbox)
    if intpbox[0] == 'default':
      x1beg, x1end = x[0],x[-1]
      x2beg, x2end = y[0],y[-1]
      x3beg, x3end = z[0],z[-1]
    else :
      x1beg, x1end = intpbox[1], intpbox[2]
      x2beg, x2end = intpbox[3], intpbox[4]
      x3beg, x3end = intpbox[5], intpbox[6]

    x1 = np.linspace(x1beg, x1end, n1)
    x2 = np.linspace(x2beg, x2end, n2)
    x3 = np.linspace(x3beg, x3end, n3)

    # If your data is not on Cartesian grid then you should convert it
    # here before interpolation. 
    # Converting function must return x, y, z, v. 

   
    # Interpolation when data already on Cartesian grid.
    print(">> Please wait, it can take a while.")
    for k in range((n3)):
       print(k)
       for j in range((n2)):
         for i in range((n1)):
           den[k,j,i] = Interpolation_3D(x, y, z, data, x1[i], x2[j], x3[k])
   
    print(">> Interpolation is complete!")

    return den


def Interpolation_3D(x, y, z, v, xi, yi, zi):
    
    iloc, jloc, kloc = 1,1,1
    for i in range(len(x)-1): 
       if(xi >= x[i] and xi < x[i+1]):
         iloc = i
         break

    for i in range(len(y)-1): 
       if(yi >= y[i] and yi < y[i+1]):
         jloc = i
         break

    for i in range(len(z)-1): 
       if(zi >= z[i] and zi < z[i+1]):
         kloc = i
         break

    # Corner average; to be improved later.
    output = 0.25*(v[kloc,jloc,iloc] + \
                   v[kloc,jloc,iloc+1] + v[kloc,jloc+1,iloc] + v[kloc+1,jloc,iloc] + \
                   v[kloc,jloc+1,iloc+1] + v[kloc+1,jloc,iloc+1] + v[kloc+1,jloc+1,iloc]\
                 + v[kloc+1,jloc+1,iloc+1])
    return output


####################################################################
#  Calculating run time
####################################################################
def RuntimeCalculation(start, end):
    
  time_spent = (end - start) / 1.;

  days  = (int) (time_spent/86400.0);
  hours = (int) ((time_spent - 86400.0*days)/3600.0);
  mins  = (int) ((time_spent - 86400.0*days - 3600.0*hours)/60.);
  secs  =       ((time_spent - 86400.0*days - 3600.0*hours - 60.0*mins));

  from datetime import datetime
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  print("\n>> Date and time =", dt_string)	
  print(">> Elapsed time:%dd:%dh:%dm:%0.2fs\n\n" %  (days, hours, mins, secs))

