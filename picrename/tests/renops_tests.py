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

def test_metadata_to_datestr_basic():
    # actual EXIF data
    assert_equal(renops.metadata_to_datetimestr(
        "- Creation date: 2014-08-02 15:36:39"),"20140802153639")

def test_metadata_to_datestr_extended():
    assert_equal(renops.metadata_to_datetimestr(
        "- Some date: 2014-12-31 18:03:25"),"20141231180325")
    assert_equal(renops.metadata_to_datetimestr(
        "2016-03-05 17:27:23"),"20160305172723")
    assert_equal(renops.metadata_to_datetimestr(
        "2015-04-11 20:33:14 This is junk"),"20150411203314")

def test_exif_to_datestr_failures():
    # this should fail
    assert_raises(renops.DateStrError,renops.metadata_to_datetimestr,
            "hello")
    assert_raises(renops.DateStrError,renops.metadata_to_datetimestr,
            "2015- bla bla")
    assert_raises(renops.DateStrError,renops.metadata_to_datetimestr,
            "2015-12-31 bla")


def test_get_fname_ext():
    assert_equal(renops.get_fname_ext("IMG_0123.JPG"),".JPG")
    assert_equal(renops.get_fname_ext("112233.PNG"), ".PNG")
    assert_equal(renops.get_fname_ext("bla.jpg"), ".jpg")

def test_incr_indexstr():
    assert_equal(renops.incr_indexstr("001"), "002")
    assert_equal(renops.incr_indexstr("42"), "43")
    assert_equal(renops.incr_indexstr("12345"), "12346")
    assert_equal(renops.incr_indexstr("999999"), "000000")

def test_extract_exif():
    base_dir = os.getcwd()

    exif_file = os.path.join(base_dir, 'test_data', 'pics', 'IMG_0422.JPG')
    assert_equal(renops.extract_exif(exif_file), "20160305172723")

    exif_file = os.path.join(base_dir, 'test_data', 'pics', 'IMG_0232.JPG')
    assert_equal(renops.extract_exif(exif_file), "20141231180325")

    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'DUMMY.JPG')
    assert_equal(renops.extract_exif(bad_file), "")

    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOEXIF.JPG')
    assert_equal(renops.extract_exif(bad_file), "")
    
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOTAG.JPG')
    assert_equal(renops.extract_exif(bad_file), "")

def test_extract_date_metadata():
    base_dir = os.getcwd()

    video_file = os.path.join(base_dir, 'test_data', 'videos', 'IMG_0421.MOV')
    assert_equal(renops.extract_date_metadata(video_file),"20160306012640")

    video_file = os.path.join(base_dir, 'test_data', 'videos', 
            '20090808_0347.MOV')
    assert_equal(renops.extract_date_metadata(video_file),"20090808110044")

    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'DUMMY.JPG')
    assert_equal(renops.extract_date_metadata(bad_file), "")

    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOEXIF.JPG')
    assert_equal(renops.extract_date_metadata(bad_file), "")
    
    # this file actually has a valid date metadata tag
#     bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOTAG.JPG')
#     assert_equal(renops.extract_date_metadata(bad_file), "")



def test_rename_all_basic():

    shutil.copytree(os.path.join("test_data","pics"),
            os.path.join("temp","temp_basic"))

    renops.rename_all(os.path.join("temp","temp_basic"),"A","001",0)

    fname1=os.path.join("temp","temp_basic","20140802_A_001.JPG")
    fname2=os.path.join("temp","temp_basic","20141231_A_002.JPG")
    fname3=os.path.join("temp","temp_basic","20160305_A_003.JPG")
    fname4=os.path.join("temp","temp_basic","20160625_A_004.JPG")

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
        shutil.rmtree(os.path.join("temp","temp_basic"))

def test_rename_all_extended():

    shutil.copytree("test_data",
            os.path.join("temp","temp_ext"))

    renops.rename_all(os.path.join("temp","temp_ext"),
            "S","120042",3)

    fnames = []

    fnames.append(os.path.join("temp", "temp_ext", 'videos', 
            "20090327_S_120042.AVI"))
    fnames.append(os.path.join("temp", "temp_ext", 'videos', 
            "20090808_S_120043.MOV"))
    fnames.append(os.path.join("temp","temp_ext","pics",
            "20140802_S_120044.JPG"))
    fnames.append(os.path.join("temp","temp_ext","pics",
            "20141231_S_120045.JPG"))
    fnames.append(os.path.join("temp","temp_ext","pics",
            "20160305_S_120046.JPG"))
    fnames.append(os.path.join("temp","temp_ext","videos",
            "20160306_S_120047.MOV"))
    fnames.append(os.path.join("temp", "temp_ext", 'videos', 
            "20160622_S_120048.MP4"))
    fnames.append(os.path.join("temp","temp_ext","pics",
            "20160625_S_120049.JPG"))
# 
    try:
        for fn in fnames:
            assert_true(os.path.exists(fn) and os.path.isfile(fn),
                    "Couldn't find new " + fn)
    finally:
        shutil.rmtree(os.path.join("temp","temp_ext"))
