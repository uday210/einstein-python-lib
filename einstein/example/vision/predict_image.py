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
    print(response)

    try:
        print(json.dumps(response, indent=4, sort_keys=True))
    except TypeError :
        print('response ok? ' + str(response.ok))
        print('response content: ' + str(response.content))
    return True


if __name__ == "__main__":
    main()