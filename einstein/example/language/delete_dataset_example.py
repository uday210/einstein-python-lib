import json
from einstein.language.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    id = '1010487'
    dataset = DataSet(access_token=access_token)
    response = dataset.delete_dataset(id)
    print('Status Code: ' + str(response.status_code))
    print('Text Message: ' + response.text)

if __name__ == "__main__":
    main()
