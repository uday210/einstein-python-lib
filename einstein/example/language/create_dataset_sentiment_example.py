import json
from einstein.language.dataset import DataSet
from einstein.constants import ACCESS_TOKEN


def main():
    access_token = ACCESS_TOKEN
    dataset = DataSet(access_token=access_token)
    path = 'https://www.dropbox.com/s/fi501unouuzet39/movie_review_train_1000_v2.tsv?dl=1'
    response = dataset.create_sentiment_dataset(path)
    print(json.dumps(response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
