import os, time, argparse, glob
from tqdm import tqdm

# from google_screenshot import GoogleCrawler
# from google_screenshot import GoogleScreenCrawler
# from yahoo_screenshot import YahooCrawler
# from bing_screenshot import BingCrawler
# from instagram_screenshot import InstagramCrawler
from mtcnn_cropper import mtcnnCropper

'''
## USAGE
python3 face_cropper.py -i <path-to folders of ids>
## EXAMPLE
python3 face_cropper.py -i '/mnt/e/RKB-Dataset/Filipina2'
'''

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
args = vars(ap.parse_args())

out_path = args['dataset']
daftar_nama = os.listdir(out_path)

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def cropper():
	print("cropping for", nama)
	nama_path = os.path.join(out_path,nama)
	# filenames = files(nama_path)
	filenames_jpg = glob.glob(nama_path + '/**/*.jpg', recursive=True)
	filenames = glob.glob(nama_path + '/**/*.png', recursive=True)
	filenames.extend(filenames_jpg)
	for filename in filenames:
		mtcnnCropper(nama_path, filename, rmv_srcimg=True)

for index, nama in enumerate(daftar_nama):
	try:
		print('processing', nama)
		# GoogleCrawler(nama, out_path)
		# GoogleScreenCrawler(nama, out_path)
		# YahooCrawler(nama, out_path)
		# BingCrawler(nama, out_path)
		# InstagramCrawler(nama, out_path)
		
		cropper()

	# 	if index < (len(daftar_nama) - 1):
	# 		for i in tqdm(range(50)):
	# 			time.sleep(1)
	except:
		print("failed or incomplete operation on", nama)
