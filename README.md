# ==========================================================================
#  M Y T H :  Multipurpose code complies YT-rendering for Hydro-simulations
# ==========================================================================

 M Y T H is a multipurpose YT-rendering code especially designed 
 for compelling the 'yt-rendering' (https://yt-project.org/). 
 Author of the MYTH code, Siddhartha Gupta, is a postdoctoral scholar 
 in the Department of Astronomy and Astrophysics at the University of Chicago.

 Please note, MYTH is not connected with the yt community
 neither it wants to violate any copyrights of yt.

 The main intention of developing MYTH is to provide a simple 
 user-friendly interface to complies yt-rendering.

#****************************************************
# Installations
#****************************************************
To run this code you will need python 3 and the yt in your pc.

1. You should have Python 3 installed in your mac. 
    The current version of MYTH is checked on python 3.7.7

2. Installation steps for yt can be found at 
   https://yt-project.org/doc/installing.html#activating-your-installation. 

3. You can directly download MYTH from 
   'git@github.com:gupta-siddhartha/MYTH.git'
   or use the following command:

   git clone git@github.com:gupta-siddhartha/MYTH.git

#****************************************************
#  How to run
#****************************************************
1. Use the guidelines in users_input.py
2. If want to use log file, set PrintLog == 'yes' in users_input.py
3. Use the following command to run.
   
   python myth.py

#****************************************************
#  Test run 
#****************************************************
1. After successful installation, you may run a test job.

In MYTH/test/plutodata_neqg/, a sample data file is provided.

Data is in 3D cartesian coordinate, nx*ny*nz = 200*60*80
>> Open terminal and go inside MYTH directory and then type
    cd src
>> Look at user_input.py file. You will notice 
InputPath  = "../test/plutodata_neqg/"
OutputPath = "../test/myth-pluto-neqg/"
>> These mean, if you run MYTH then it will generate output in ../test/myth-pluto-neqg/ 
>> To run MYTH, use the following command on the terminal (note: you are inside src/)

    python myth.py

>> Please wait. It will take a while (for this test it may take ~ 2 min).
>> After all steps, when you will see a Thank you message, you may look into 
>> your MYTH/test/myth-pluto-neqg/  

To check whether everything is correct or not, you
may visit https://astro.uchicago.edu/~siddhartha/#codes.

#****************************************************
#  Note
#****************************************************
1. Do not touch myth.py unless you wish to do some runtime analysis

2. Current version of MYTH read PLUTO dbl file format and extract only density column.
   If you wish to read other formats, then please do so by following 
   the guidelines in 'readfile.py'

3. The current version has been checked on MPI/Open-MPI or similar platform for the parallel job, but it may not be difficult to extend it. 

4. Most importantly, you must have sufficient space/memory in your machine in order to run yt.

#****************************************************
#  List of files and their roles.
#****************************************************
1. myth.py        ==> main file
2. headers.py     ==> imports all necessary python dir
3. readfile.py    ==> reads all data file
4. tools.py       ==> for interpolation
5. ytrendering.py ==> yt rendering operations done here.
6. users_input.py ==> user's portal to control input/output.

# ==================================================================
#                  All the best (Y) :-) 
# ================================================================== 
