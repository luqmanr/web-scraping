import os, argparse
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
    help='path to the directory you want to scan')
args = vars(ap.parse_args())

src = args['input']

## src = path to highest folder you want to scan
import glob
files = glob.glob(src + '/**/*.jpg', recursive=True)

for index, file in enumerate(files):
    if index == 0:
        path = Path(file).parent.absolute()
        print(path)

        break