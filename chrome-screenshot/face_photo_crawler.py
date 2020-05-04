import os, time, argparse
from tqdm import tqdm
from multiprocessing import Process

from google_screenshot import GoogleCrawler
from google_screenshot import GoogleScreenCrawler
from yahoo_screenshot import YahooCrawler
from bing_screenshot import BingCrawler
from instagram_screenshot import InstagramCrawler
# from mtcnn_face_cropper import mtcnnCropper
'''
## USAGE
python3 face_photo_crawler.py -o <path-to folders of ids>
## EXAMPLE
python3 face_photo_crawler.py -o '/mnt/e/RKB-Dataset/Filipina2'
'''

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of downloads")
ap.add_argument("--google",
    help="use if you want to google crawl", action='store_true')
ap.add_argument("--bing",
    help="use if you want to bing crawl", action='store_true')
args = vars(ap.parse_args())

out_path = args['output']
# out_path = '/media/sf_E/RKB-Dataset/Filipina2/'

daftar_nama = [
  "Chua Phung Kim Singapore",
  "Chua Thian Poh Singapore",
  "Corrinne May Singapore",
  "Daniel Bennett Singapore",
  "David Bala Singapore",
  "David Saul Marshall Singapore",
  "Davinder Singh Singapore",
  "Desmond Kuek Singapore",
  "Devan Nair Singapore",
  "Dick Lee Singapore",
  "Dr Ng Eng Hen Singapore",
  "Eunice Olsen Singapore",
  "Fandi Ahmad Singapore",
  "Fann Wong Singapore",
  "Felicia Chin Singapore",
  "Ferlyn Wong Singapore",
  "Fiona Xie Singapore",
  "Geh Min Singapore",
  "Gerard Ee Singapore",
  "Goh Cheng Liang Singapore",
  "Goh Chok Tong Singapore",
  "Goh Keng Swee Singapore",
  "Goh Tat Chuan Singapore",
  "Gurmit Singh Singapore",
  "Han Sai Por Singapore",
  "Hazlina Halim Singapore",
  "Heng Swee Keat Singapore",
  "Ho Ching Singapore",
  "Hoi Kim Heng Singapore",
  "Hon Sui Sen Singapore",
  "Indranee Rajah Singapore",
  "Ivan Heng Singapore",
  "Jack Neo Singapore",
  "Jason Chang Singapore",
  "Jeanette Aw Singapore",
  "Jeremy Monteiro Singapore",
  "Jiang Yanmei Singapore",
  "Jing Jun Hong Singapore",
  "JJ Lin Singapore",
  "Joanna Dong Singapore",
  "Joshua Benjamin Jeyaretnam Singapore",
  "Kam Ning Singapore",
  "Keith Goh Singapore",
  "Kelvin Tan Wei Lian Singapore",
  "Ken Lim Singapore",
  "Khaw Boon Wan Singapore",
  "Khoo Boon Hui Singapore",
  "Khoo Teck Puat Singapore",
  "Kit Chan Singapore",
  "Koh Wee Meng Singapore",
  "Kuok Khoon Hong Singapore",
  "Kwa Geok Choo Singapore",
  "Kwee Family Singapore",
  "Kwek Leng Beng Singapore",
  "Kym Ng Singapore",
  "Lawrence Wong Singapore",
  "Lee Hsien Loong Singapore",
  "Lee Hsien Yang Singapore",
  "Lee Huei Min Singapore",
  "Lee Kim Lai Singapore",
  "Lee Kong Chian Singapore",
  "Lee Kuan Yew Singapore",
  "Lee Seng Wee Singapore",
  "Lee Siew Choh Singapore",
  "Li Jiawei Singapore",
  "Li Li Singapore",
  "Lim Bo Seng Singapore",
  "Lim Boon Keng Singapore",
  "Lim Hock Siew Singapore",
  "Lim Kim San Singapore",
  "Lim Oon Kuin Singapore",
  "Lim Yew Hock Singapore",
  "Lin Junjie Singapore",
  "Ling How Doong Singapore",
  "Lionel Lewis Singapore",
  "Low Thia Khiang Singapore",
  "Maia Lee Singapore",
  "Mavis Hee Singapore",
  "Michelle Chong Singapore",
  "Natasha Low Singapore",
  "Nathan Hartono Singapore",
  "Ng Ser Miang Singapore",
  "Ng Teng Fong Singapore",
  "Oei Hong Leong Singapore",
  "Olivia Lum Singapore",
  "Ong Keng Yong Singapore",
  "Ong Teng Cheong Singapore",
  "Ou Mei Wen Singapore",
  "Ou Wen Han Singapore",
  "Peter Lim Singapore",
  "Philip Jeyaretnam Singapore",
  "Philip Ng Singapore",
  "Poh Seng Song Singapore",
  "Rajesh Sreenivasan Singapore",
  "Rebecca Lim Singapore",
  "Remy Ong Singapore",
  "Robert Ng Singapore",
  "Rohan Gunaratna Singapore",
  "Ron Sim Singapore",
  "Ronald Susilo Singapore",
  "Rui En Singapore",
  "Russell Lee Singapore",
  "S Dhanabalan Singapore",
  "Sam Goi Singapore",
  "Sellapan Ramanathan Singapore",
  "Shamsul Maidin Singapore",
  "Shu Ping Singapore",
  "Shunmugam Jayakumar Singapore",
  "Simon Chua Singapore",
  "Sinnathamby Rajaratnam Singapore",
  "Siow Lee Chin Singapore",
  "Stefanie Sun Singapore",
  "Steven Chong Singapore",
  "Su-Chen Christine Lim Singapore",
  "Subhas Anandan Singapore",
  "Sumiko Tan Singapore",
  "Susan Long Singapore",
  "Sylvester Sim Singapore",
  "Tan Cheng Bock Singapore",
  "Tan Chong Tee Singapore",
  "Tan Howe Liang Singapore",
  "Tan Jee Say Singapore",
  "Tan Kah Kee Singapore",
  "Tan Keng Yam Tony Singapore",
  "Tan Kin Lian Singapore",
  "Tan Lark Sye Singapore",
  "Tan Ser Cher Singapore",
  "Tan Swie Hian Singapore",
  "Tan Tock Seng Singapore",
  "Tanya Chua Singapore",
  "Taufik Batisah Singapore",
  "Teo Chee Hean Singapore",
  "Tharman Shanmugaratnam Singapore",
  "Thum Ping Tjin Singapore",
  "Tin Pei Ling Singapore",
  "Toh Chin Chye Singapore",
  "V. K. Rajah Singapore",
  "Vivian Balakrishnan Singapore",
  "Vivian Lai Singapore",
  "Wee Cho Yaw Singapore",
  "Wee Kim Wee Singapore",
  "Wong Kan Seng Singapore",
  "Wong Ming Yang Singapore",
  "Wong Peng Soon Singapore",
  "Wong Yip Yan Singapore",
  "Woon Cheong Ming Walter Singapore",
  "Yam Ah Mee Singapore",
  "Yeo Yong-Boon George Singapore",
  "Youyi Singapore",
  "Yusof bin Ishak Singapore",
  "Zhang Yong Singapore",
  "Zhao Tao Singapore",
  "Zhong Sheng Jian Singapore"
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
    
    # GoogleCrawling = Process(target=GoogleCrawler, args=(nama, out_path))
    # GoogleCrawling.start()
    # BingCrawling = Process(target=BingCrawler, args=(nama, out_path))
    # BingCrawling.start()
    if args['google'] == True:
        GoogleCrawler(nama, out_path)
    if args['bing'] == True:
        BingCrawler(nama, out_path)

    # GoogleCrawler(nama, out_path)
    # GoogleScreenCrawler(nama, out_path)
    # YahooCrawler(nama, out_path)
    # BingCrawler(nama, out_path)
    # InstagramCrawler(nama, out_path)

    # GoogleCrawling.join()
    # BingCrawling.join()

    try:    
        # cropper()

        if index < (len(daftar_nama) - 1):
            for i in tqdm(range(50)):
                time.sleep(1)
    except:
        print("failed or incomplete operation on", nama)