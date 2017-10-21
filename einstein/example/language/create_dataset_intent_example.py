import json
from einstein.language.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    #curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache"
    # -H "Content-Type: multipart/form-data" -F "path=http://einstein.ai/text/weather.csv"
    # -F "type=text-intent"  https://api.einstein.ai/v2/language/datasets/upload

    access_token = ACCESS_TOKEN
    dataset = DataSet(access_token=access_token)
    path = 'http://einstein.ai/text/weather.csv'
    response = dataset.create_intent_dataset(path)
    print(json.dumps(response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
