import requests

# https://opentdb.com/api_config.php, get more parameters
PARAMETERS = {
    "amount": 10,
    "category": 15,
    "difficulty": "easy",
    "type": "boolean",

}
question_response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean",params=PARAMETERS)
requests.status_codes

question_data = question_response.json()["results"]
