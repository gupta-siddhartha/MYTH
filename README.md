# ==========================================================================
#  M Y T H :  Multipurpose YT-rendering code for Hydro-simulations
# ==========================================================================

 M Y T H is a multipurpose YT-rendering code especially designed 
 to compile the 'yt-rendering' (https://yt-project.org/). 
 Author of the MYTH code, Siddhartha Gupta, is a postdoctoral scholar 
 in the Department of Astronomy and Astrophysics at the University of Chicago.

 Please note, MYTH is neither connected with the yt community
 nor it wants to violate any copyright of yt-project.

 The main intention of developing MYTH is to provide a simple 
 user-friendly interface to compile yt-rendering. Code documentation
can be found at https://astro.uchicago.edu/~siddhartha/MYTH/myth.html

#****************************************************
# Installations
#****************************************************

To run this code you will need python 3 and the yt in your pc.

1. You should have Python 3 installed in your mac. 
    The current version of MYTH is checked on python 3.7.7

2. Installation steps for yt can be found at 
   https://yt-project.org/doc/installing.html#activating-your-installation. 

3. You can directly download MYTH from 
   https://github.com/gupta-siddhartha/MYTH


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

After successful installation, you may run a test job.

In MYTH/test/plutodata_neqg/, sample data files (data.0004.dbl,grid.out,stars.0004.txt) are provided. Data is in 3D cartesian coordinate, nx x ny x nz = 200x60x80. 

    cd src

Look into user_input.py file. You will notice:
 InputPath  = "../test/plutodata_neqg/".
 OutputPath = "../test/myth-pluto-neqg/".
It means, if you run MYTH then it will generate output at ../test/myth-pluto-neqg/. 
To run MYTH, use the following command on the terminal (note: your current directory is 'src'):

    python myth.py

Please wait. It will take a while (for this test it may take ~ 2 min).
After all steps, when you will see a Thank you message, you may look into 
your MYTH/test/myth-pluto-neqg/, which must contain the following files:

checkinput0004.png: z=0 slice of input data file

unigriddata0004.txt: Interpolated data with user's specified resolution.

checkdump0004.png: z=0 slice of interpolated data file 

volren0004-transferfunction.png: Density transfer function. Note: label may not be correct.

volren0004.0001.png: Final output

To check whether everything is correct or not, you
may visit https://astro.uchicago.edu/~siddhartha/MYTH/myth.html

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
