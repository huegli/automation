from nose.tools import *

from picrename.prnm import renops

def test_exif_to_datestr_basic():
    # actual EXIF data
    assert_equal(renops.exif_to_datestr("2014:08:02 15:36:39"), "20140802")

def test_exif_to_datestr_extended():
    assert_equal(renops.exif_to_datestr("2014:12:31 18:03:25"), "20141231")
    assert_equal(renops.exif_to_datestr("2016:03:05 17:27:23"), "20160305")
    
    # made up
    assert_equal(renops.exif_to_datestr("1970:01:01 00:00:00"), "19700101")

def test_exif_to_datestr_failures():
    # this should fail
    assert_raises(renops.DateStrError,renops.exif_to_datestr,"hello")
    assert_raises(renops.DateStrError,renops.exif_to_datestr,"2015: bla bla")
    assert_raises(renops.DateStrError,renops.exif_to_datestr,"2015:12:31 bla")

def test_get_fname_ext():
    assert_equal(renops.get_fname_ext("IMG_0123.JPG"),".JPG")
    assert_equal(renops.get_fname_ext("112233.PNG"), ".PNG")
    assert_equal(renops.get_fname_ext("bla.jpg"), ".jpg")

def test_incr_indexstr():
    assert_equal(renops.incr_indexstr("001"), "002")
    assert_equal(renops.incr_indexstr("42"), "43")
    assert_equal(renops.incr_indexstr("12345"), "12346")
    assert_equal(renops.incr_indexstr("999999"), "000000")

#def test_rename_all_basic():
#    renops.rename_all("test_data/pics","A","001")
#    assert_equal(0,1)

