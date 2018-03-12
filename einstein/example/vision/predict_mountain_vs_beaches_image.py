import json
from einstein.vision.prediction import Prediction
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Mount_McKinley_and_Denali_National_Park_Road_2048px.jpg/220px-Mount_McKinley_and_Denali_National_Park_Road_2048px.jpg'
    model_id = 'F2C4M43BDS3AULHG7AGKLF2MIE'
    prediction = Prediction(access_token=access_token)
    response = prediction.predict_remote_image(url, model_id)
    probabilities = response['probabilities']
    for x in probabilities:
        print(str(x['label']) + ":" + str(x['probability']))


if __name__ == "__main__":
    main()