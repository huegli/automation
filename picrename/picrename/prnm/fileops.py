import piexif

import hachoir_core
import hachoir_core.cmd_line
import hachoir_metadata
import hachoir_parser
import sys

class EXIFTagError(Exception):
    pass

class VideoMetadataError(Exception):
    pass

def get_exif_datetimeorig_tag(fname):
    """
    Returns the EXIF Tag 36867 (DateTimeOriginal) from a file

    The return string will have the format 'YYYY:MM:DD HH:MM:SS' or 
    if no EXIF tag is found or the file is not valid or doesn't exist,
    an exception will be thrown

    :param fname:   Name of file to read EXIF tag from
    :returns:       EXIF tag in specified format

    :Example:

        >>> import fileops
        >>> print fileops.get_exif_datetimeorig_tag("IMG_1234.JPG")
        '2013:09:30 15:21:42'
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

def get_video_creation_date_metadata(fname):

    """
    Returns the "Creation date" entry from the metadata of a file

    The return string will have the format
    '- Creation date: YYYY-MM-DD HH:MM:SS' or if no metadata is found
    or the file is not valid or doesn't exist, an exception will be thrown

    :param fname:   Name of file to read the metadata from
    :returns:       creation data metadata in specified format

    :Example:

        >>> import fileops
        >>> print fileops.get_video_creation_date_metadata("IMG_1234.JPG")
        '- Creation date: 2013-09-30 15:21:42'
    """

    try:
        fname, realname = hachoir_core.cmd_line.unicodeFilename(
                fname), fname
        parser = hachoir_parser.createParser(fname, realname)
    except:
        raise VideoMetadataError, "Unable to parse video file"

    if not parser:
        raise VideoMetadataError, "Unable to parse video file"

    try:
        metadata = hachoir_metadata.extractMetadata(parser)
    except HachoirError:
        raise VideoMetadataError, "Error extracting metadata "
    
    if not metadata:
        raise VideoMetadataError, "No metadata found" 
    
    text = metadata.exportPlaintext()

    for line in text:
        printable = hachoir_core.tools.makePrintable(line,
                hachoir_core.i18n.getTerminalCharset())
        if "Creation date" in printable:
            return printable

    raise VideoMetadataError, "No 'Creation date' found in metadata"
        
