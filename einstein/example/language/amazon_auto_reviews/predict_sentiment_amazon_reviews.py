import json
import os
from einstein.vision.prediction import Prediction
from einstein.language.prediction import Prediction
from einstein.constants import ACCESS_TOKEN

access_token = ACCESS_TOKEN
model_id = 'QSSDPMITHUVHYVWVE6PRRVVU4A'
import os
cwd = os.getcwd()
file = cwd + '/data/amz_automobile_reviews_unlabeled.csv'
def main():
    predict()

def predict():
    prediction = Prediction(access_token=access_token)
    with open(file) as f:
        for line in f:
            response = prediction.predict_sentiment(line, model_id)
            #print(response.status_code)
            probabilities = response['probabilities']
            print(line)
            print(probabilities[0]['label'] + "," + str(probabilities[0]['probability']))

if __name__ == "__main__":
    main()