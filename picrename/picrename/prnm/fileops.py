import piexif

def get_exif_datetimeorig_tag(fname):
    """
    Returns the EXIF Tag 36867 (DateTimeOriginal) from a file

    The return string will have the format 'YYYY:MM:DD HH:MM:SS' or 
    if no EXIF tag is found, an exception will be thrown
    """

    exif_dict = piexif.load(fname)
    return exif_dict['Exif'][36867]

def get_pic_fnames(dirpath):
    pass

def get_pic_datestring(fname):
    pass

def rename_file(old_fnamepath, new_fnamepath):
    pass

def rename_all(dirpath, startletter, startindex):
    pass
