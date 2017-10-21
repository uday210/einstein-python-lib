import json
from einstein.vision.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    dataset = DataSet(access_token=access_token)
    response = dataset.get_all_datasets()
    data = response['data']
    for d in data:
        print(str(d))

if __name__ == "__main__":
    main()
