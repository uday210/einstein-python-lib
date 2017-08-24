import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from einstein.constants import DATASETS_URL
from einstein.constants import VISION_BASE_URL
from einstein.constants import VISION_MODEL_URL


class DataSet:

    def __init__(self,access_token):
        self.access_token = access_token

    def create_dataset(self, path):
        multipart_data = MultipartEncoder(
            fields={
                'path': path,
                'type': 'image'
            }
        )
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(DATASETS_URL + '/upload',
                            headers=headers, data=multipart_data)
        json_response = json.loads(res.text)
        return json_response

    def delete_dataset(self, _id, name):
        multipart_data = MultipartEncoder(
            fields={'name': name,
                    'datasetId': _id})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post(DATASETS_URL + '/train',
                            headers=headers, data=multipart_data)
        # builder.addTextBody("name", "Beach Mountain Model Test")
        #builder.addTextBody("datasetId", id)

        return res

    def train_dataset(self, id):
        multipart_data = MultipartEncoder(
            fields={'name': 'Beach Mountain Model Test',
                    'datasetId' : id})
        # builder.addTextBody("name", "Beach Mountain Model Test")
        # builder.addTextBody("datasetId", id)
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.post( VISION_BASE_URL + '/train',
                              headers=headers, data=multipart_data)
        return res

    def update_dataset(self):
        pass

    def get_all_datasets(self):
        pass

    def get_dataset_details(self, id):
        multipart_data = MultipartEncoder(
            fields={'type': 'image'})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.get(DATASETS_URL + '/' + id,
                              headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

    def get_model_details(self, id):
        multipart_data = MultipartEncoder(
            fields={'type': 'image'})
        headers = {'Authorization': 'Bearer ' + self.access_token,
                   'Content-Type': multipart_data.content_type}
        res = requests.get(VISION_MODEL_URL + '/' + id,
                              headers=headers, data=multipart_data)
        if res.ok:
            json_response = json.loads(res.text)
            return json_response
        else:
            return res

