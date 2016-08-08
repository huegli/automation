import os
import shutil
import subprocess

from nose.tools import *

def test_basic_launch_noargs():
    # make sure we get error code if no arguments
    FNULL = open(os.devnull, 'w')
    return_code = subprocess.call(['chksum'],
            stdout=FNULL, stderr=subprocess.STDOUT)
    assert_true(return_code, 2)

    # check for short help message if no arguments
    chksum_p = subprocess.Popen(['chksum'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    chksum_output = chksum_p.communicate()[0]
    assert_in('usage: chksum', chksum_output)

def test_help():
    # make sure we get the full help if we specify '--help'
    chksum_output = subprocess.check_output(['chksum','--help'])
    assert_in('Using SHA256 to calculate', chksum_output)
    assert_in('positional arguments', chksum_output)
    assert_in('optional arguments', chksum_output)

def test_basic_operation():
     
     chksum_output = subprocess.check_output(['chksum',
         os.path.join("test_data","id_rsa.pub")]) 
     assert_in('id_rsa.pub', chksum_output)
     assert_in('4945185bdb65a118', chksum_output)

# def test_error_operation():
#     
#     shutil.copytree(os.path.join("test_data","bad_files"),
#             os.path.join("temp","temp_error"))
# 
#     picrename_p = subprocess.Popen(['picrename', '-v 1',
#         os.path.join("temp","temp_error")],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT)
#     picrename_err_out = picrename_p.communicate()[0]
#     print picrename_err_out
# 
#     try:
#         assert_in('WARNING', picrename_err_out)
#         assert_in('DUMMY.JPG', picrename_err_out)
#         assert_in('NOEXIF.JPG', picrename_err_out)
#         assert_in('NOTAG.JPG', picrename_err_out)
#     finally:
#         shutil.rmtree(os.path.join("temp","temp_error"))
# 
# def test_verbose_operation():
#     
#     shutil.copytree(os.path.join("test_data","pics"),
#             os.path.join("temp","temp_verbose"))
# 
#     picrename_p = subprocess.Popen(['picrename', '--verbose=3',
#         os.path.join("temp","temp_verbose")],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT)
#     picrename_verbose_out = picrename_p.communicate()[0]
#     print picrename_verbose_out
# 
#     try:
#         assert_in('DEBUG', picrename_verbose_out)
#         assert_in('Found EXIF Tag', picrename_verbose_out)
#         assert_in('INFO', picrename_verbose_out)
#         assert_in('Renaming', picrename_verbose_out)
#     finally:
#         shutil.rmtree(os.path.join("temp","temp_verbose"))
# 
# def test_index_operation():
#     
#     shutil.copytree(os.path.join("test_data","pics"),
#             os.path.join("temp","temp_index"))
# 
#     subprocess.call(['picrename', '-a N',
#         '--num_index=3121',
#         os.path.join("temp","temp_index")]) 
# 
#     fname1=os.path.join("temp","temp_index","20140802_N_3121.JPG")
#     fname2=os.path.join("temp","temp_index","20141231_N_3122.JPG")
#     fname3=os.path.join("temp","temp_index","20160305_N_3123.JPG")
#     fname4=os.path.join("temp","temp_index","20160625_N_3124.JPG")
# 
#     try:
#         assert_true(os.path.exists(fname1) and os.path.isfile(fname1),
#                 "Couldn't find new " + fname1)
#         assert_true(os.path.exists(fname2) and os.path.isfile(fname2),
#                 "Couldn't find new " + fname2) 
#         assert_true(os.path.exists(fname3) and os.path.isfile(fname3),
#                 "Couldn't find new " + fname3)
#         assert_true(os.path.exists(fname4) and os.path.isfile(fname4),
#                 "Couldn't find new " + fname4)
#     finally:
#         shutil.rmtree(os.path.join("temp","temp_index"))
# 
