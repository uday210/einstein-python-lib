import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from einstein.constants import LANG_DATASETS_URL
from einstein.constants import LANG_BASE_URL
from einstein.constants import LANG_MODEL_URL


class DataSet:

    def __init__(self,access_token):
        self.access_token = access_token

    def create_dataset(self, path):
        multipart_data = MultipartEncoder(
            fields={
                'path': path,
                'type': 'text-intent'
            }
        )
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(LANG_DATASETS_URL + '/upload',
                            headers=headers, data=multipart_data)
        json_response = json.loads(res.text)
        return json_response

    def delete_dataset(self, id):
        multipart_data = MultipartEncoder(
            fields={})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(LANG_DATASETS_URL + '/' + id,
                            headers=headers, data=multipart_data)

        return res

    def get_dataset_details(self, id):
        multipart_data = MultipartEncoder(
            fields={'type': 'image'})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.get(LANG_DATASETS_URL + '/' + id,
                              headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

    def train_dataset(self, id, model_name):
        multipart_data = MultipartEncoder(
            fields={'name': model_name,
                    'datasetId': id})

        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(LANG_BASE_URL + '/train',
                            headers=headers, data=multipart_data)
        return res

    def get_model_details(self, id):
        multipart_data = MultipartEncoder(
            fields={'type': 'image'})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.get(LANG_MODEL_URL + '/' + id,
                              headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res