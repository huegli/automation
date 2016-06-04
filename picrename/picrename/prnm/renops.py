import re

class DateStrError(Exception):
    pass

def exif_to_datestr(exif_data_string):

    dateregex = re.compile(r"""
                    (?P<year>\d\d\d\d): # match the year
                    (?P<month>\d\d):    # match the month
                    (?P<day>\d\d)       # match the day
                    \s\d\d:\d\d\:\d\d   # the rest of the data string
                    """, re.VERBOSE)

    match = re.match(dateregex, exif_data_string)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        return year + month + day
    else:
        raise DateStrError

def get_pic_fnames(dirpath):
    pass

def get_pic_datestring(fname):
    pass

def rename_file(old_fnamepath, new_fnamepath):
    pass

def rename_all(dirpath, startletter, startindex):
    pass
