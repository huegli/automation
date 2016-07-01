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

def test_get_video_creation_date_metadata_basic():
    base_dir = os.getcwd()
    video_file = os.path.join(base_dir, 'test_data', 'videos', 'IMG_0421.MOV')
    assert_equal(fileops.get_video_creation_date_metadata(video_file),
            "- Creation date: 2016-03-06 01:26:40")

def test_get_video_creation_date_metadata_extended():
    base_dir = os.getcwd()
    video_file = os.path.join(base_dir, 'test_data', 'videos', 
            '20090327_0308.AVI')
    assert_equal(fileops.get_video_creation_date_metadata(video_file),
            "- Creation date: 2009-03-27 13:45:12")
    video_file = os.path.join(base_dir, 'test_data', 'videos', 
            '20090808_0347.MOV')
    assert_equal(fileops.get_video_creation_date_metadata(video_file),
            "- Creation date: 2009-08-08 11:00:44")
    video_file = os.path.join(base_dir, 'test_data', 'videos', 
            'WP_20160621_15_33_12_Pro.mp4')
    assert_equal(fileops.get_video_creation_date_metadata(video_file),
            "- Creation date: 2016-06-22 06:33:12")

def test_get_video_creation_date_metadata_failures():
    base_dir = os.getcwd()
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'DUMMY.JPG')
    assert_raises(fileops.VideoMetadataError,
            fileops.get_video_creation_date_metadata, bad_file)
    bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOEXIF.JPG')
    assert_raises(fileops.VideoMetadataError,
            fileops.get_video_creation_date_metadata, bad_file)
    # This file actually has a proper creation date tag
    # bad_file = os.path.join(base_dir, 'test_data', 'bad_files', 'NOTAG.JPG')
