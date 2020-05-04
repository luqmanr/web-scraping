import sys, os, json, time, argparse, cv2, imutils
import tensorflow as tf
from mtcnn.mtcnn import MTCNN
from tqdm import tqdm
from datetime import datetime

detector = MTCNN(min_face_size=50)

def mtcnnCropper(
    keyword_path, filename, margin_percent = 0.45, rmv_srcimg=True):
    
    image_path = os.path.join(keyword_path, filename)
    
    try:
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    except:
        print('[Warning!]:{} image reading process not successful!'.format(image_path))
        return
    
    results = detector.detect_faces(image)
    
    iterator = 1
    print('processing', image_path)
    for result in results:
        # FORMAT DATA result[box] = [left-x, top-y, width, height]
        bbox = result['box']
        # print('bbox', bbox)

        marginY = int(margin_percent * bbox[3])
        marginX = int(margin_percent * bbox[2])
        # print('marginY, marginX', marginY, marginX)

        # print('image.shape[0], image.shape[1]', image.shape[0], image.shape[1])

        bottomY = bbox[1] + bbox[3] + marginY if bbox[1] + bbox[3] + marginY < image.shape[0] else image.shape[0]
        rightX = bbox[0] + bbox[2] + marginX if bbox[0] + bbox[2] + marginX < image.shape[1] else image.shape[1]
        topY = bbox[1] - marginY if bbox[1] - marginY > 0 else 0
        leftX = bbox[0] - marginX if bbox[0] - marginX > 0 else 0
        # print('topY, rightX, bottomY, leftX', topY, rightX, bottomY, leftX)

        img_width = abs(rightX - leftX)
        img_height = abs(bottomY - topY)
        # print('img_width, img_height', img_width, img_height)

        try:
            if (img_height < 250):
                cropped_img = image[topY:bottomY, leftX:rightX]
                cropped_img = imutils.resize(cropped_img, height=250, width=(round(img_width*250/img_height)))
            if (img_width < 250):
                cropped_img = image[topY:bottomY, leftX:rightX]
                cropped_img = imutils.resize(cropped_img, width=250, height=(round(img_height*250/img_width)))
            else:
                cropped_img = image[topY:bottomY, leftX:rightX]
        except:
            print('[Warning!]:{} crop process not successful!'.format(image_path))
            continue

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        img_name = os.path.join(keyword_path, str(timestamp) + '.jpg')
        iterator += 1

        try:
            cv2.imwrite(img_name, cv2.cvtColor(cropped_img, cv2.COLOR_RGB2BGR))
        except:
            print()
            print('[Warning!]:{} save process not successful!'.format(img_name))
            continue
    try:
        if rmv_srcimg:
            open(image_path, 'w').close()
            os.remove(image_path)
    except:
        print('origin photo not deleted')