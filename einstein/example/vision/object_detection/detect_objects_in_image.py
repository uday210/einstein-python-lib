import json
from einstein.vision.prediction import Prediction
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    url = 'https://www.dropbox.com/s/xryf4smcgfih5m0/astro2.JPG?dl=1'
    model_id = 'UVNMAD26FSVAVPHOWNFKKN63FM'
    prediction = Prediction(access_token=access_token)
    response = prediction.detect_objects_remote_image(url, model_id)
    probabilities = response['probabilities']
    for x in probabilities:
        print(str(x['label']) + ":" + str(x['probability']))


if __name__ == "__main__":
    main()