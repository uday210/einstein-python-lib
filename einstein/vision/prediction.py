import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from einstein.constants import VISION_PREDICT_URL
from einstein.constants import VISION_DETECT_URL
import base64


class Prediction:

    def __init__(self,access_token):
        self.access_token = access_token

    def predict_remote_image(self, url, model_id):
        multipart_data = MultipartEncoder(
            fields={'sampleLocation': url,
                    'modelId' : model_id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(VISION_PREDICT_URL,
                            headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

    def predict_local_image(self, filename, model_id):
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        multipart_data = MultipartEncoder(
            fields={#'sampleContent': '@' + path,
                    'sampleBase64Content': encoded_string,
                    'modelId': model_id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(VISION_PREDICT_URL,
                            headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

    def detect_objects_remote_image(self, url, model_id):
        multipart_data = MultipartEncoder(
            fields={'sampleLocation': url,
                    'modelId': model_id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(VISION_DETECT_URL,
                            headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res
