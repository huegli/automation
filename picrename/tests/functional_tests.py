import os
import shutil
import subprocess

from nose.tools import *

def test_basic_launch_noargs():
    # make sure we get error code if no arguments
    FNULL = open(os.devnull, 'w')
    return_code = subprocess.call(['picrename'],
            stdout=FNULL, stderr=subprocess.STDOUT)
    assert_true(return_code, 2)

    # check for short help message if no arguments
    picrename_p = subprocess.Popen(['picrename'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    picrename_output = picrename_p.communicate()[0]
    assert_in('usage: picrename', picrename_output)

def test_help():
    # make sure we get the full help if we specify '--help'
    picrename_output = subprocess.check_output(['picrename','--help'])
    assert_in('Rename pictures with a date string', picrename_output)
    assert_in('positional arguments', picrename_output)
    assert_in('optional arguments', picrename_output)

def test_basic_operation():
    
    shutil.copytree(os.path.join("test_data","pics"),
            os.path.join("test_data","temp_func"))

    curdir = os.getcwd()
    os.chdir(os.path.join("test_data","temp_func"))
   
    subprocess.call(['picrename', '.']) 

    os.chdir(curdir)

    fname1=os.path.join("test_data","temp_func","20140802_A_001.JPG")
    fname2=os.path.join("test_data","temp_func","20141231_A_002.JPG")
    fname3=os.path.join("test_data","temp_func","20160305_A_003.JPG")
    fname4=os.path.join("test_data","temp_func","20160625_A_004.JPG")

    try:
        assert_true(os.path.exists(fname1) and os.path.isfile(fname1),
                "Couldn't find new " + fname1)
        assert_true(os.path.exists(fname2) and os.path.isfile(fname2),
                "Couldn't find new " + fname2) 
        assert_true(os.path.exists(fname3) and os.path.isfile(fname3),
                "Couldn't find new " + fname3)
        assert_true(os.path.exists(fname4) and os.path.isfile(fname4),
                "Couldn't find new " + fname4)
    finally:
        shutil.rmtree(os.path.join("test_data","temp_func"))

