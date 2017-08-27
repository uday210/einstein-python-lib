import json
from einstein.language.prediction import Prediction
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    docuemt = 'what is the weather in los angeles'
    model_id = 'V3E7CDCNLYMQD7XFM3NBXMZICE'
    prediction = Prediction(access_token=access_token)
    response = prediction.predict_intent(docuemt, model_id)

    try:
        print(json.dumps(response, indent=4, sort_keys=True))
    except TypeError :
        print('response ok? ' + str(response.ok))
        print('response content: ' + str(response.content))
    return True


if __name__ == "__main__":
    main()