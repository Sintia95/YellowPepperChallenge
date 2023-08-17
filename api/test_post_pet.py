import requests
import json
from assertpy import assert_that

url = "http://localhost:8080/api/v3/pet/"


def test_create_pet_without_body():

    response = requests.request("POST", url)

    assert_that(response).has_status_code(400)


def test_create_pet_with_invalid_body():

    body = {"invalid" : "invalid"}
    response = requests.request("POST", url, data = body)

    assert_that(response).has_status_code(500)
    assert_that(response.text).contains("There was an error processing your request.")

def test_create_pet_with_valid_body():

    body = {
        "id": 77,
        "name": "elefante",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.request("POST", url, data = body)

    assert_that(response).has_status_code(200)
    assert_that(json.loads(response.text)["name"]).is_equal_to("elefante")
    assert_that(json.loads(response.text)["id"]).is_equal_to(77)