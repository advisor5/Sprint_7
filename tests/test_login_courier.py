import allure
from courier.courier_routes import CourierApiClient
from data.constants import StatusCode
from data.constants import Message
from data.constants import CourierData


class TestLoginCourier:
    @allure.title('Тест получения кода 200 при успешной авторизации курьера')
    @allure.description(
    'Проверка, что авторизация успешна и возвращается код 200')
    def test_login_courier_and_return_200(self, register_rand_user):
        
        login_pass = register_rand_user[0]
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = CourierApiClient().post_login_courier(payload)
        
        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
 
    @allure.title('Тест получения "id" при успешной авторизации курьера')
    @allure.description(
    'Проверка, что авторизация успешна и возвращается id курьера')
    def test_login_courier_and_return_id(self, register_rand_user):
        
        login_pass = register_rand_user[0]
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = CourierApiClient().post_login_courier(payload)
        
        actually_value = response.json()
        expected_value = Message.KEY_ID
        assert expected_value in actually_value
        allure.attach(f"{response.json()}", "Message")

    @allure.title('Тест получения ошибки 400 при авторизации без указания логина')
    @allure.description(
    'Проверка, что при запросе без логина получим ошибку 400')
    def test_login_courier_whithout_field_login_return_400(self, register_rand_user):
        
        payload = {
            "login": "",
            "password": register_rand_user[1]
        }

        response = CourierApiClient().post_login_courier(payload)
        
        actually_value = response.status_code
        expected_value = StatusCode.BAD_REQUEST_400
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
           
    @allure.title('Тест получения текста ошибки при авторизации без указания логина')
    @allure.description(
    'Проверка, что при запросе без логина получим текст ошибки')
    def test_login_courier_whithout_field_login_return_error_message(self, register_rand_user):
        
        payload = {
            "login": "",
            "password": register_rand_user[1] 
        }

        response = CourierApiClient().post_login_courier(payload)
        
        actually_value = response.json()["message"]
        expected_value = Message.NOT_ENOUGTH_DATA
        assert actually_value == expected_value
        allure.attach(f"{response.json()}", "Message")
       
    @allure.title('Тест получения текста ошибки при авторизации без указания пароля')
    @allure.description(
    'Проверка, что при запросе без пароля получим текст ошибки')
    def test_login_courier_whithout_field_password_return_error_message(self, register_rand_user):
        
        payload = {
            "login": register_rand_user[0],
            "password":""
        }

        response = CourierApiClient().post_login_courier(payload)
        
        actually_value = response.json()["message"]
        expected_value = Message.NOT_ENOUGTH_DATA
        assert actually_value == expected_value
        allure.attach(f"{response.json()}", "Message")

    @allure.title('Тест получения кода 404 при авторизации несуществующего курьера')
    @allure.description(
    'Проверка, что при запросе c несуществующей парой логин-пароль получим ошибку 404')
    def test_login_courier_not_existent_pair_login_pass_return_404(self):
        
        response = CourierApiClient().post_login_courier(CourierData.NOT_EXIST_USER)
        
        actually_value = response.status_code
        expected_value = StatusCode.NOT_FOUND_404
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status") 

    @allure.title('Тест получения текста ошибки при авторизации несуществующего пользователя')
    @allure.description(
    'Проверка, что при запросе c несуществующей парой логин-пароль получим текст ошибки')
    def test_login_courier_not_existent_pair_login_pass_return_error_text(self):
        
        response = CourierApiClient().post_login_courier(CourierData.NOT_EXIST_USER)
        
        actually_value = response.json()["message"]
        expected_value = Message.NOT_FOUND_ID
        assert actually_value ==  expected_value
        allure.attach(f"{response.json()}", "Message")
