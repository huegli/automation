import os
import re

from picrename.prnm import fileops

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

def get_fname_ext(fname):

    splitext = os.path.splitext(fname)

    return splitext[-1]

def incr_indexstr(indexstr):

    index = int(indexstr)
    length = len(indexstr)

    index = index + 1

    newindexstr = str(index).rjust(length, "0")

    return newindexstr[-length:]


def rename_all(dirpath, startletter, startindex):

    indexstr = startindex

    for rootdir, alldirs, allfiles in os.walk(dirpath):
        
        for afile in allfiles:
            
            afileext = get_fname_ext(afile)
       
            fullfname = os.path.join(rootdir, afile)

            exif_data = fileops.get_exif_datetimeorig_tag(fullfname)

            datestr = exif_to_datestr(exif_data)

            newfname = datestr + "_" + startletter + "_" + indexstr + afileext

            newfullfname = os.path.join(rootdir, newfname)

            os.rename(fullfname, newfullfname)

            indexstr = incr_indexstr(indexstr)
