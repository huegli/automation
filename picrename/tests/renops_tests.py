from nose.tools import *

from picrename.prnm import renops

def test_exif_to_datestr_basic():
    # actual EXIF data
    assert_equal(renops.exif_to_datestr("2014:08:02 15:36:39"), "20140802")

def test_exif_to_datestr_extended():
#    assert_equal(renops.exif_to_datestr("2014:12:31 18:03:25"), "20141231")
#    assert_equal(renops.exit_to_datestr("2016:03:05 17:27:23"), "20160305")
#    
#    # made up
#    assert_equal(renops.exif_to_datestr("1970:01:01 00:00:00"), "19700101")
    pass    

def test_exif_to_datstr_failures():
    # this should fail
#    assert_raises(renops.exif_to_datestr("hello"))
#    assert_raises(renops.exif_to_datestr("2015: bla bla"))
#    assert_raises(renops.exif_to_datestr("2015:12:31 bla"))
    pass

# renops.rename_all("","A","001")

