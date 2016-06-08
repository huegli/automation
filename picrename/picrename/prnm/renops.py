import os
import re

from picrename.prnm import fileops

class DateStrError(Exception):
    pass

def exif_to_datestr(exif_data_string):
    """
    Extracts the date from an EXIF tag and reformats it
    """
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
    """
    Helper function to get the extension of a filename
    """
    splitext = os.path.splitext(fname)

    return splitext[-1]

def incr_indexstr(indexstr):
    """
    Increments a numerical index in string form.
    String will be truncated to original length on roll-over
    """
    index = int(indexstr)
    length = len(indexstr)

    index = index + 1

    # fill in leading zero's
    newindexstr = str(index).rjust(length, "0")

    # maintain original length, truncating on the right if needed
    return newindexstr[-length:]


def rename_all(dirpath, startletter, startindex):
    """
    Renames all files in a directory that have EXIF data using the
    DateTimeOrig tag information. Renamed files will have the format 
    'YYYYMMDD_<startletter>_<incr index>'.

    :param dirpath:     Path to do the renaming in
    :param startletter: letter that froms part of the renamed filename
    :param startindex:  incrementing index that forms part of the 
                        renamed filename


    :Example:

        >>> import os
        >>> print os.listdir(".")
        ['IMG_1234.JPG']
        >>> import renops
        >>> print renops.rename_all(".", "A", "001")
        >>> print os.listdir(".")
        ['20110217_A_001.JPG']

    .. note::   If dirpath contains subdirectories, these are processed
                recursively.
    """
    indexstr = startindex

    for rootdir, alldirs, allfiles in os.walk(dirpath):
        
        for afile in allfiles:
            
            afileext = get_fname_ext(afile)
       
            fullfname = os.path.join(rootdir, afile)

            try:
                exif_data = fileops.get_exif_datetimeorig_tag(fullfname)

                datestr = exif_to_datestr(exif_data)
            except:
                print "Something went wrong with " + afile

            else:

                newfname = datestr + "_" + startletter + "_" + indexstr + afileext

                newfullfname = os.path.join(rootdir, newfname)

                os.rename(fullfname, newfullfname)

                indexstr = incr_indexstr(indexstr)
