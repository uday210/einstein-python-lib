import json
import os
from einstein.vision.prediction import Prediction
from einstein.constants import ACCESS_TOKEN

access_token = ACCESS_TOKEN
model_id = 'AKCA4Y3GXG3QDS3WQVON37D6XM'

def main():
    folder = '/Users/rdua/work/metamind/datasets/001/Type_1'
    predict_folder(folder)

def predict_folder(folder):
    prediction = Prediction(access_token=access_token)

    for filename in os.listdir(folder):
        filename_long = folder + '/' + filename

        response = prediction.predict_local_image(filename_long, model_id)
        probabilities = response['probabilities']
        print(filename + ": " + probabilities[0]['label'] + "," + str(probabilities[0]['probability']))

if __name__ == "__main__":
    main()