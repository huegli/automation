import os
import re
import logging

from picrename.prnm import fileops

class DateStrError(Exception):
    pass

def exif_to_datetimestr(exif_data_string):
    """
    Extracts the date from an EXIF tag and reformats it
    """
    dateregex = re.compile(r"""
                    (?P<year>\d\d\d\d): # match the year
                    (?P<month>\d\d):    # match the month
                    (?P<day>\d\d)       # match the day
                    \s
                    (?P<hour>\d\d):     # match the hour
                    (?P<min>\d\d):      # match the minute
                    (?P<sec>\d\d)       # match the second
                    """, re.VERBOSE)

    match = re.match(dateregex, exif_data_string)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        hour = match.group(4)
        mins = match.group(5)
        sec = match.group(6)
        return year + month + day + hour + mins + sec
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


def rename_all(dirpath, startletter, startindex, verbose=1):
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

    if (verbose == 0):
        logging.getLogger().setLevel(logging.ERROR)
    elif (verbose == 1):
        logging.getLogger().setLevel(logging.WARNING)
    elif (verbose == 2):
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.getLogger().setLevel(logging.DEBUG)

    indexstr = startindex
    datetimestr_to_fullfname_dict = {}

    # iterate over all files in subdirectories from given root directory
    for rootdir, alldirs, allfiles in os.walk(dirpath):

        for afile in allfiles:

            # create the full path to the file
            fullfname = os.path.join(rootdir, afile)

            # check if there is a valid file
            if not (os.path.exists(fullfname) and
                    os.path.isfile(fullfname)):
                logging.warning("Cannot access %r, skipping it", fullfname)
                continue

            # First try if the file is an image file with EXIF tags
            try:
                # check if file has EXIF date, exception if not
                exif_data = fileops.get_exif_datetimeorig_tag(fullfname)
                # extract the date/time string from EXIF, exception if
                # not the proper format
                datetimestr = exif_to_datetimestr(exif_data)

                logging.debug("Found EXIF Tag %r for file %r", datetimestr, afile)

                # store full file name in dictionarly using date/time
                # string as a key
                datetimestr_to_fullfname_dict[datetimestr] = fullfname

                continue

            except fileops.EXIFTagError:
                logging.warning(
                        "%r does not have a proper EXIF tag, skipping it",
                        afile)
                continue

            except DateStrError:
                logging.warning(
                        "%r EXIF tag not the right format, skipping it",
                        afile)
                continue


            # Otherwise, it might be a video file with creation date tag
            try:
                # check if file has creation date, exception if not
                date_metadata = fileops.get_video_creation_date_metadata(fullfname)
                # extract the date/time string from metadata, exception if
                # not the proper format
                datetimestr = exif_to_datetimestr(date_metadata)

                logging.debug("Found creation date metadata %r for file %r",
                        datetimestr, afile)

                # store full file name in dictionarly using date/time
                # string as a key
                datetimestr_to_fullfname_dict[datetimestr] = fullfname

                continue

            except fileops.VideoMetadataError:
                logging.warning(
                        "%r does not have a proper creation date metadata, skipping it",
                        afile)
                continue

            except DateStrError:
                logging.warning(
                        "%r EXIF tag not the right format, skipping it",
                        afile)
                continue



    # Go through the alphabetically (and therefore time-stamp sorted)
    # list of keys of the dictionary to do the rename
    for a_dtstr in sorted(datetimestr_to_fullfname_dict.keys()):

        # we discard the time portion as we don't need it for
        # the filename
        datestr = a_dtstr[:8]

        # the file extension from original filename
        afileext = get_fname_ext(
                datetimestr_to_fullfname_dict[a_dtstr]).upper()

        newfname = datestr + "_" + startletter + "_" + indexstr + afileext

        # create the new full filename by taking existing path of old 
        # full filename and combining with new file name
        newfullfname = os.path.join(
            os.path.dirname(datetimestr_to_fullfname_dict[a_dtstr]),
            newfname)

        try:
            logging.info("Renaming %r -> %r",
                    datetimestr_to_fullfname_dict[a_dtstr],
                    newfullfname)
            os.rename(datetimestr_to_fullfname_dict[a_dtstr],
                    newfullfname)
        except:
            print "Can't rename file %s to %s" % (
                    datetimestr_to_fullfname_dict[a_dtstr], newfullfname)


        indexstr = incr_indexstr(indexstr)
