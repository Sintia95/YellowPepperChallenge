import requests
import json
from assertpy import assert_that

url = "http://localhost:8080/api/v3/pet/findByStatus"


def test_find_pet_without_status():

    response = requests.request("GET", url)

    assert_that(response).has_status_code(400)
    assert_that(response.text).contains("No status provided. Try again?")

def test_find_pet_with_status_available():

    query_params = {"status": "available"}

    response = requests.request("GET", url, params=query_params)

    assert_that(response).has_status_code(200) 
    for pet in json.loads(response.text):
        assert_that(pet["status"]).is_equal_to("available")


