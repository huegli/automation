import os
import shutil

from nose.tools import *

from picrename.prnm import renops

def test_exif_to_datestr_basic():
    # actual EXIF data
    assert_equal(renops.exif_to_datetimestr("2014:08:02 15:36:39"),
            "20140802153639")

def test_exif_to_datestr_extended():
    assert_equal(renops.exif_to_datetimestr("2014:12:31 18:03:25"),
            "20141231180325")
    assert_equal(renops.exif_to_datetimestr("2016:03:05 17:27:23"),
            "20160305172723")
    
    # made up
    assert_equal(renops.exif_to_datetimestr("1970:01:01 00:00:00"),
            "19700101000000")

def test_exif_to_datestr_failures():
    # this should fail
    assert_raises(renops.DateStrError,renops.exif_to_datetimestr,
            "hello")
    assert_raises(renops.DateStrError,renops.exif_to_datetimestr,
            "2015: bla bla")
    assert_raises(renops.DateStrError,renops.exif_to_datetimestr,
            "2015:12:31 bla")

def test_get_fname_ext():
    assert_equal(renops.get_fname_ext("IMG_0123.JPG"),".JPG")
    assert_equal(renops.get_fname_ext("112233.PNG"), ".PNG")
    assert_equal(renops.get_fname_ext("bla.jpg"), ".jpg")

def test_incr_indexstr():
    assert_equal(renops.incr_indexstr("001"), "002")
    assert_equal(renops.incr_indexstr("42"), "43")
    assert_equal(renops.incr_indexstr("12345"), "12346")
    assert_equal(renops.incr_indexstr("999999"), "000000")

def test_rename_all_basic():

    shutil.copytree(os.path.join("test_data","pics"),
            os.path.join("test_data","temp_basic"))

    renops.rename_all(os.path.join("test_data","temp_basic"),"A","001")

    fname1=os.path.join("test_data","temp_basic","20140802_A_001.JPG")
    fname2=os.path.join("test_data","temp_basic","20141231_A_002.JPG")
    fname3=os.path.join("test_data","temp_basic","20160305_A_003.JPG")
    fname4=os.path.join("test_data","temp_basic","20160625_A_004.JPG")

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
        shutil.rmtree(os.path.join("test_data","temp_basic"))

def test_rename_all_extended():

    shutil.copytree("test_data",
            os.path.join("test_data","temp_ext"))

    renops.rename_all(os.path.join("test_data","temp_ext"),
            "S","120042")

    fname1=os.path.join("test_data","temp_ext","pics",
            "20140802_S_120042.JPG")
    fname2=os.path.join("test_data","temp_ext","pics",
            "20141231_S_120043.JPG")
    fname3=os.path.join("test_data","temp_ext","pics",
            "20160305_S_120044.JPG")
    fname4=os.path.join("test_data","temp_ext","pics",
            "20160625_S_120045.JPG")

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
        shutil.rmtree(os.path.join("test_data","temp_ext"))
