import os

from nose.tools import *

from picrename.prnm import fileops

def test_get_exif_datetimeorig_tag_basic():
    base_dir = os.getcwd()
    exif_file = os.path.join(base_dir, 'test_data', 'pics', 'IMG_0422.JPG')
    assert_equal(fileops.get_exif_datetimeorig_tag(exif_file), "2016:03:05 17:27:23")

def test_get_exif_datetimeorig_tag_extended():
    base_dir = os.getcwd()
    exif_file = os.path.join(base_dir, 'test_data', 'pics', 'IMG_0005.JPG')
    assert_equal(fileops.get_exif_datetimeorig_tag(exif_file), "2014:08:02 15:36:39")
    exif_file = os.path.join(base_dir, 'test_data', 'pics', 'IMG_0232.JPG')
    assert_equal(fileops.get_exif_datetimeorig_tag(exif_file), "2014:12:31 18:03:25")

def test_get_exif_datetimeorig_tag_failures():
    base_dir = os.getcwd()
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'DUMMY.JPG')
    assert_raises(fileops.EXIFTagError,
            fileops.get_exif_datetimeorig_tag, bad_file)
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOEXIF.JPG')
    assert_raises(fileops.EXIFTagError,
            fileops.get_exif_datetimeorig_tag, bad_file)
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOTAG.JPG')
    assert_raises(fileops.EXIFTagError,
            fileops.get_exif_datetimeorig_tag, bad_file)

