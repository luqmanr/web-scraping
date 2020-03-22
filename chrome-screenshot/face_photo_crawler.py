import os, time
from tqdm import tqdm

from google_screenshot import GoogleCrawler
from google_screenshot import GoogleScreenCrawler
from yahoo_screenshot import YahooCrawler
from bing_screenshot import BingCrawler
from instagram_screenshot import InstagramCrawler
from mtcnn_face_cropper import mtcnnCropper

out_path = './output/Timor Leste'

daftar_nama = [
  "Manuel Viegas Carrascalao Timor Leste",
  "Marcelino Da Costa Fernandes Timor Leste",
  "Mari Alkatiri Timor Leste",
  "Marí Alkatiri Timor Leste",
  "Maria Ângela Carrascalão Timor Leste",
  "Maria de Lourdes Martins Cruz Timor Leste",
  "Maria Domingas Alves Timor Leste",
  "Maria Terezinha Viegas Timor Leste",
  "Mariana Diaz Ximenez Timor Leste",
  "Martinho da Costa Lopes Timor Leste",
  "Martinho de Araujo Timor Leste",
  "Miguel Santos Soares Timor Leste",
  "Miro Baldo Bento Timor Leste",
  "Nando football Timor Leste",
  "Nicolau dos Reis Lobato Timor Leste",
  "Nino Konis Santana Timor Leste",
  "Norberto Do Amaral Timor Leste",
  "Olinda Morais Timor Leste",
  "Rogerio Lobato Timor Leste",
  "Rosa Bonaparte Timor Leste",
  "Rosária Corte-Real Timor Leste",
  "Salvador Carlos Timor Leste",
  "Taur Matan Ruak Timor Leste",
  "Vicente Guterres Timor Leste",
  "Vicente Ramos Freitas Timor Leste",
  "Xanana Gusmão Timor Leste",
  "Zacarias da Costa Timor Leste"
]

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
		GoogleCrawler(nama, out_path)
		GoogleScreenCrawler(nama, out_path)
		YahooCrawler(nama, out_path)
		BingCrawler(nama, out_path)
		# InstagramCrawler(nama, out_path)
		
		# cropper()

		if index < (len(daftar_nama) - 1):
			for i in tqdm(range(50)):
				time.sleep(1)
	except:
		print("failed or incomplete operation on", nama)

