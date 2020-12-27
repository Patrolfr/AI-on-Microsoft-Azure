import argparse
import json
import time

import pandas as pd
import requests
from IPython.core.display import HTML
from PIL import Image
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

PREDICTION_URL = 'https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/c25f9428-620d-4d73-a916-9b674753eb6f/classify/iterations/Iteration1/image'
PREDICTION_KEY = '13b9b42be84f403691e8868051e174a5'

def getImage(url, name):
    with open(name, 'wb') as f:
        f.write(requests.get(url).content)


def get_face_client():
    SUBSCRIPTION_KEY = "0cc9df6afba14ac68d53f3196d193156"
    ENDPOINT = "https://garmid.cognitiveservices.azure.com/"
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)


def path_to_image_html(path):
    return '<img src="'+ path + '" width="100" >'


def postForEyes(path):
    with open(path, 'rb') as f:
        data = f.read()
    res = requests.post(
        url=PREDICTION_URL,
        data=data,
        headers={'Content-Type': 'application/octet-stream', 'Prediction-Key': PREDICTION_KEY})
    return res.json()


parser = argparse.ArgumentParser(description='Parse image url.')
parser.add_argument('url', type=str, nargs='?', help='an url to image')
URL = parser.parse_args().url
if not URL:
    raise Exception("Url of image to process should be provided.")
print(URL)

face_client = get_face_client()

attributes = ["emotion", "smile", "age", "gender"]
include_id = True
include_landmarks = False

detected_faces = face_client.face.detect_with_url(URL, include_id, include_landmarks, attributes, raw=True)

if not detected_faces:
    raise Exception("No face detected in image")

result = detected_faces.response.json()

getImage(URL, 'imgs/imgToProcess')
im = Image.open("imgs/imgToProcess")
im.show()

# crop rois from image and eyes classification
rois = []
for index, face in enumerate(result, start=1):
    print(index)
    print(face)
    roi = face["faceRectangle"]
    box = (roi["left"], roi["top"], roi["left"] + roi["width"], roi["top"] + roi["height"])
    im1 = im.crop(box)
    im1Name = "imgs/roi{}.jpg".format(index)
    im1.save(im1Name)
    rois.append(im1Name)
    face['eyes'] = postForEyes(im1Name)
    time.sleep(1)

print(result)

# generate html
df = pd.DataFrame()
df["faceImage"] = rois
df["age"] = list(map(lambda res: res["faceAttributes"]["age"], result))
df["gender"] = list(map(lambda res: res["faceAttributes"]["gender"], result))
df["smile"] = list(map(lambda res: res["faceAttributes"]["smile"], result))
df["emotion"] = list(map(lambda res: json.dumps(res["faceAttributes"]["emotion"],
                                                sort_keys=True, indent=4, default=str).replace("\n","<br/>"), result))
df["eyes"] = list(map(lambda res: json.dumps(res["eyes"]["predictions"],
                                             sort_keys=True, indent=4, default=str).replace("\n","<br/>"), result))

df.to_html(escape=False, formatters=dict(faceImage=path_to_image_html))
HTML(df.to_html(escape=False,formatters=dict(faceImage=path_to_image_html)))
df.to_html('feedback.html',escape=False, formatters=dict(faceImage=path_to_image_html))