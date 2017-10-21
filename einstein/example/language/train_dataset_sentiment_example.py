import json
from einstein.language.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    id = '1016532'
    name = 'Movie Review DataSet'
    dataset = DataSet(access_token=access_token)
    response = dataset.train_dataset(id, model_name=name)
    if('available' in response):
        print(json.dumps(response, indent=4, sort_keys=True))

    else:
        print('Response status ok?: ' + str(response.ok))
        print(json.dumps(response.text, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
