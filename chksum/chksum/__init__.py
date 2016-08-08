import hashlib
import argparse

def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()



def main():

    parser = argparse.ArgumentParser(
        prog = 'chksum',
        description =
            "Using SHA256 to calculate a checksum for one or more files",
        formatter_class=argparse.RawTextHelpFormatter
        )

    parser.add_argument('fnames', metavar='fname', type=str, nargs='+',
            help="One or more filenames to calculate the checksum for")

    args = parser.parse_args()

    for fname in args.fnames:
        print "%s: %s" %(fname, 
                hashfile(open(fname, 'rb'), hashlib.sha256())[:16])
