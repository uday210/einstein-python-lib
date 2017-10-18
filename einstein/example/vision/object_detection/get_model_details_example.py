import json
from einstein.vision.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    id = 'UVNMAD26FSVAVPHOWNFKKN63FM'
    dataset = DataSet(access_token=access_token)
    response = dataset.get_model_details(id)

    try:
        print(json.dumps(response, indent=4, sort_keys=True))
    except TypeError :
        print('response ok? ' + str(response.ok))
        print('response content: ' + str(response.content))
    return True


if __name__ == "__main__":
    main()
