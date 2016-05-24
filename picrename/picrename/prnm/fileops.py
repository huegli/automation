import piexif

class EXIFTagError(Exception):
    pass

def get_exif_datetimeorig_tag(fname):
    """
    Returns the EXIF Tag 36867 (DateTimeOriginal) from a file

    The return string will have the format 'YYYY:MM:DD HH:MM:SS' or 
    if no EXIF tag is found or the file is not valid or doesn't exist,
    an exception will be thrown
    """

    try:
        exif_dict = piexif.load(fname)

    except ValueError:
        raise EXIFTagError, "Not a valid picture file"

    else:

        if exif_dict['Exif']:
            try:
                date_string = exif_dict['Exif'][36867]
            except KeyError:
                raise EXIFTagError, "No DateTimeOriginal EXIF Tag found"
            else:
                return date_string
        else:
            raise EXIFTagError, "No EXIF information found"
def get_pic_fnames(dirpath):
    pass

def get_pic_datestring(fname):
    pass

def rename_file(old_fnamepath, new_fnamepath):
    pass

def rename_all(dirpath, startletter, startindex):
    pass
