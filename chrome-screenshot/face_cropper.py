import os, time
from tqdm import tqdm

# from google_screenshot import GoogleCrawler
# from google_screenshot import GoogleScreenCrawler
# from yahoo_screenshot import YahooCrawler
# from bing_screenshot import BingCrawler
# from instagram_screenshot import InstagramCrawler
from mtcnn_face_cropper import mtcnnCropper

out_path = '/mnt/e/RKB-Dataset/Filipina3/'

daftar_nama = os.listdir('/mnt/e/RKB-Dataset/Filipina2/')

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def cropper():
	print("cropping for", nama)
	nama_path = os.path.join(out_path,nama)
	filenames = files(nama_path)
	for filename in filenames:
		mtcnnCropper(nama_path, filename)

for index, nama in enumerate(daftar_nama):
	try:
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