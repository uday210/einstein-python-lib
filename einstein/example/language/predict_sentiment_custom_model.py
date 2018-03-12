import json
from einstein.language.prediction import Prediction
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    docuemt = 'An intermittently pleasing but mostly routine effort'
    model_id = 'VLEITGZ347BJBAQOHCDFV4VXTI'
    prediction = Prediction(access_token=access_token)
    response = prediction.predict_sentiment(docuemt, model_id)

    try:
        probabilities = response['probabilities']
        for x in probabilities:
            print(str(x['label']) + ":" + str(x['probability']))

    except TypeError :
        print('response ok? ' + str(response.ok))
        print('response content: ' + str(response.content))
    return True


if __name__ == "__main__":
    main()