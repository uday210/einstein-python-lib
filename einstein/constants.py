
EINSTEIN_BASE_URL = 'https://api.einstein.ai/v2'
VISION_BASE_URL = EINSTEIN_BASE_URL + '/vision'
DATASETS_URL = VISION_BASE_URL + '/datasets'
VISION_MODEL_URL = VISION_BASE_URL + '/models'
VISION_PREDICT_URL = VISION_BASE_URL + '/predict'

LANG_BASE_URL = EINSTEIN_BASE_URL + '/language'
LANG_DATASETS_URL = LANG_BASE_URL + '/datasets'
LANG_MODEL_URL = LANG_BASE_URL + '/models'
#https://api.einstein.ai/v2/language/intent
LANG_INTENT_PREDICT_URL = LANG_BASE_URL + '/intent'

ACCESS_TOKEN = ''
#
# curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -
# H "Content-Type: multipart/form-data" -F "path=http://einstein.ai/text/weather.csv"
# -F "type=text-intent"  https://api.einstein.ai/v2/language/datasets/upload
