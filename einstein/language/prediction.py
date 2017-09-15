import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from einstein.constants import LANG_INTENT_PREDICT_URL
from einstein.constants import LANG_SENTIMENT_PREDICT_URL


class Prediction:

    def __init__(self,access_token):
        self.access_token = access_token

    def predict_intent(self, document, model_id):
        multipart_data = MultipartEncoder(
            fields={'document': document,
                    'modelId' : model_id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(LANG_INTENT_PREDICT_URL,
                            headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

    def predict_sentiment(self, document, model_id):
        multipart_data = MultipartEncoder(
            fields={'document': document,
                    'modelId': model_id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(LANG_SENTIMENT_PREDICT_URL,
                            headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res
