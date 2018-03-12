import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import jwt
import time

API_ROOT = 'https://api.einstein.ai/v2/'

API_OAUTH = API_ROOT + 'oauth2/token'
email = '<change_me>@gmail.com'
private_key_file = '/PATH/predictive_services.pem'
file = open(private_key_file,'r' )
private_key_str = file.read()
token = ''

def get_token():
    """ Acquires a token for futher API calls, unless you already have a token this will be the first thing
        you do before you use this.
        :param email: string, the username for your EinsteinVision service, usually in email form
        :para pem_file: string, file containing your Secret key. Copy contents of relevant Config Var
        on Heroku to a file locally.
        attention: this will set self.token on success
        attention: currently spitting out results via a simple print
        returns: requests object
    """
    payload = {
        'aud': API_OAUTH,
        'exp': time.time() + 600,  # 10 minutes
        'sub': email
    }

    header = {'Content-type': 'application/x-www-form-urlencoded'}

    assertion = jwt.encode(payload, private_key_str, algorithm='RS256')
    assertion = assertion.decode('utf-8')

    response = requests.post(
        url=API_OAUTH,
        headers=header,
        data='grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=' + assertion
    )

    print(response.text)

    if response.status_code == 200:
        print('status 200 ok for Token')
        token = response.json()['access_token']
    else:
        print('Could not get Token. Status: ' + str(response.status_code))

    #return response

if __name__ == "__main__":
    get_token()