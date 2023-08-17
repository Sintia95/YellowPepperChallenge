import requests
import json
from assertpy import assert_that

url = "http://localhost:8080/api/v3/pet"


def test_edit_pet():

    body = {
        "id": 77,
        "name": "tortuga",
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

    response = requests.request("GET", url = f"{url}/77")
    assert_that(json.loads(response.text)["name"]).is_equal_to("elefante")
    response = requests.request("PUT", url, data= body)
    response = requests.request("GET", url = f"{url}/77")
    assert_that(json.loads(response.text)["name"]).is_equal_to("tortuga")


