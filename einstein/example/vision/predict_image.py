import json
from einstein.vision.prediction import Prediction
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Pepperoni_pizza.jpg/' \
          '440px-Pepperoni_pizza.jpg'
    model_id = 'FoodImageClassifier'
    prediction = Prediction(access_token=access_token)
    response = prediction.predict_remote_image(url, model_id)
    probabilities = response['probabilities']
    for x in probabilities:
        print(str(x['label']) + ":" + str(x['probability']))


if __name__ == "__main__":
    main()