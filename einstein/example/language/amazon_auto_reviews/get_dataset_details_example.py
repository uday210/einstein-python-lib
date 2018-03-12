import json
from einstein.language.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    id = '1043007'
    dataset = DataSet(access_token=access_token)
    response = dataset.get_dataset_details(id)
    if('available' in response):
        print(json.dumps(response, indent=4, sort_keys=True))

    else:
        print('Response status ok?: ' + str(response.ok))
        print(response.text )


if __name__ == "__main__":
    main()
