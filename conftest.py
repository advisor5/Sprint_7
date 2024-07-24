import pytest 
import random
import string
from courier.courier_routes import CourierApiClient


@pytest.fixture
def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string

@pytest.fixture
def register_rand_user(generate_random_string):

    login = generate_random_string
    password = generate_random_string
    first_name = generate_random_string
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = CourierApiClient().post_reg_courier(payload)
        
    login_pass = []
    login_pass.append(login)
    login_pass.append(password)
    yield login_pass, response    
    
    response_login = CourierApiClient().post_login_courier(payload)
    id_courier = response_login.json()['id']
    CourierApiClient().delete_courier(id_courier)
