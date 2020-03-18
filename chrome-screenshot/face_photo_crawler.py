import os, time

from google_screenshot import GoogleCrawler
from google_screenshot import GoogleScreenCrawler
from yahoo_screenshot import YahooCrawler
from bing_screenshot import BingCrawler
from instagram_screenshot import InstagramCrawler
from face_cropper_mtcnn import mtcnnCropper

# out_path = '/media/luqmanr/TOSHIBA1TB/Thailand'
# out_path = '/media/sf_H_Ext/Indonesia'
out_path = './Test'

daftar_nama = [
"Profile Picture & Wallpaper"
]

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for nama in daftar_nama:
	try:
		GoogleCrawler(nama, out_path)
		GoogleScreenCrawler(nama, out_path)
		YahooCrawler(nama, out_path)
		BingCrawler(nama, out_path)
		# InstagramCrawler(nama, out_path)

		print("cropping for", nama)
		nama_path = os.path.join(out_path,nama)
		filenames = files(nama_path)
		for filename in filenames:
			mtcnnCropper(nama_path, filename)

		time.sleep(50)
	except:
		print("failed or incomplete operation on", nama)

