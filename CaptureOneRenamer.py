"""
This script rename all the jpg files in the current folder,
such that the comma separated keywords will be added to the beginning of the file name.
"""

from glob import glob
from iptcinfo3 import IPTCInfo
from os.path import basename
from shutil import copy
from tqdm import tqdm


def rename(fn):
    img = IPTCInfo(fn)
    keywords = ', '.join([x.decode('utf-8') for x in img['keywords']])
    newfn = f'{keywords}_{basename(fn)}'
    copy(fn, newfn)

if __name__ == '__main__':
    fns = glob('./*.jpg')
    for fn in tqdm(fns):
        rename(fn)
