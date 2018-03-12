import json
from einstein.vision.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    id = '1018800'
    dataset = DataSet(access_token=access_token)
    response = dataset.train_dataset(id)
    if('available' in response):
        print(json.dumps(response, indent=4, sort_keys=True))

    else:
        print('Response status ok?: ' + str(response.ok))
        res = json.loads(response.text)
        print('status: ' + res['status'])
        print('modelId: ' + res['modelId'])
        print('createdAt: ' + res['createdAt'])
        print('name: ' + res['name'])

        response_text = json.dumps(response.text)


if __name__ == "__main__":
    main()
