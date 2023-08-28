# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Pet Steps
Steps file for Pet.feature
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import requests
from behave import given

# Load data here

@given('the following pets')
def step_impl(context):
    """Refresh all Pets in the database"""

    # List all of the pets and delete them one by one
    response = requests.get(f"{context.base_url}/pets")
    assert response.status_code == 200
    for pet in response.json():
        response = requests.delete(f"{context.base_url}/pets/{pet['id']}")
        assert response.status_code == 204

    # load the database with new pets
    for row in context.table:
        payload = {
            "name": row['name'],
            "category": row['category'],
            "available": row['available'] in ['True', 'true', '1'],
            "gender": row['gender'],
            "birthday": row['birthday']
        }
        response = requests.post(f"{context.base_url}/pets", json=payload)
        assert response.status_code == 201
