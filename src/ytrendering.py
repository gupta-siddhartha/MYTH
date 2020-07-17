import numpy as np
import yt
from yt.visualization.volume_rendering.api import PointSource

########################################
#  Yt rendering
#  Reference: https://yt-project.org/doc/visualizing/volume_rendering.html
# 
#  Re-arranged by Siddhartha Gupta
#  contact: gsiddhartha@uchicago.edu
#
#  Last modified by Siddhartha Gupta
#  on 19 May 2020
########################################
def VolumeRender(colorbound, RenderingOperation, outputfile, X1,X2,X3, data, Particles):

  bbox = np.array([[X1[0], X1[-1]], [X2[0], X2[-1]], [X3[0], X3[-1]]])
  
  arr=data
  data = dict(density = (arr, "g/cm**3"))

  ds = yt.load_uniform_grid(data, arr.shape, length_unit="pc", bbox=bbox, nprocs=1) 

  #************************************** 
  # Extracting user's specified 
  #                parameters in main.py
  #**************************************
  zooming         = RenderingOperation[0]
  Operationalfile = RenderingOperation[1]
  Initial_L0      = RenderingOperation[2]
  Lmin            = RenderingOperation[3]
  Lmax            = RenderingOperation[4]
  dl              = RenderingOperation[5]
  Rotation        = RenderingOperation[6]
  RotaAngle       = RenderingOperation[7]
  RotaSteps       = int(RenderingOperation[8]) 
  length = Initial_L0
  
  frame=1
  print(">> Performing volume rendering ...")
  
  fout= "%s.%04d.png" % (outputfile,frame)

  print(">>",frame,length,fout)

  #**************************************
  # main part starts
  #**************************************
  sc = yt.create_scene(ds)
  source = sc[0]
  sc.camera.resolution = [1024, 1024]  #horizontal, verticle
  sc.camera.width = (length, 'pc')
  sc.camera.switch_orientation(normal_vector=np.array([0,0,-1]),north_vector=np.array([0,1,0]))
  #sc.camera.set_position(ds.domain_left_edge)
  
  if len(Particles) > 1:
    print(">>Adding particles")
    colors = 2 + np.zeros((len(Particles), 4)) #np.random.random([len(Particles), 4])    
    colors[:, 3] = 0.7  # Opacity of Star particles
    points = PointSource(Particles, colors=colors)
    sc.add_source(points)
  
  source.set_log(True)
  source.tfh.set_bounds((colorbound[0], colorbound[1]))
  source.tfh.set_log(True)
  source.tfh.grey_opacity = True
  source.tfh.plot('%s-transferfunction'% outputfile, profile_field='density')

  #sc.annotate_axes(alpha=.02)
  #sc.annotate_domain(ds, color=[1, 1, 1, .01]
  sc.annotate_axes()
  sc.save(fout)
  #text_string = '10' #"%s" % (length)
  #sc.save_annotated(fout,text_annotate=[[(.8, 0.2), text_string]])

  frame = frame + 1
  cam = sc.camera
  #**************************************
  # Zooming-in
  #**************************************
  if ('%s' % zooming) == 'yes':
    print("Zooming in requested!")
    # Zoom in 
    while(length>Lmin):
       print(length)
       sc.camera.width = (length, 'pc')
       sc.render()
       sc.save('%s.%04d.png' % (outputfile,frame)) 
       length = length - dl
       frame += 1

  #**************************************
  # Rotation: 180 degree
  #**************************************
  if ('%s' % Rotation) == 'yes':
    print("Rotation is requested! Forward.")
    #Rotate by 180 degrees over 5 frames
    for _ in cam.iter_rotate(RotaAngle, RotaSteps):
      sc.render()
      sc.save('%s.%04d.png' % (outputfile,frame))
      frame += 1
  
  #**************************************
  # Zooming out
  #**************************************
  if ('%s' % zooming) == 'yes':
    print("Zooming out requested!")
    length = length + dl 
    while(length<=Lmax):
       print(length)
       sc.camera.width = (length, 'pc')
       sc.render()
       sc.save('%s.%04d.png' % (outputfile,frame)) 
       length = length + dl
       frame += 1

  #**************************************
  # 180 degree rotation to return to 
  # original position
  #**************************************
  if ('%s' % Rotation) == 'yes':
    print("Rotation is requested! Backward.")
    #Rotate by 180 degrees over 5 frames
    for _ in cam.iter_rotate(RotaAngle, RotaSteps):
      sc.render()
      sc.save('%s.%04d.png' % (outputfile,frame))
      frame += 1

#**************************************
# main part ends
#************************************** 

 




