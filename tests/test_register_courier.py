import allure
from courier.courier_routes import CourierApiClient
from data.constants import CourierData
from data.constants import StatusCode
from data.constants import Message


class TestRegisterCourier:
    @allure.title('Тест регистрации нового курьера')
    @allure.description(
    'Проверка успешного создания курьера и возвращение кода 201')
    def test_register_courier_and_return_201(self):
                
        response = CourierApiClient().post_reg_courier(CourierData.NEW_USER)
        
        actually_value = response.status_code
        expected_value = StatusCode.CREATED_201
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

        login_courier = CourierApiClient().post_login_courier(CourierData.DATA_FOR_LOGIN)
        id_courier = login_courier.json()['id']
        CourierApiClient().delete_courier(id_courier)

    @allure.title('Тест получения сообщения при успешной регистрации курьера')
    @allure.description(
    'Проверка, что успешный запрос на создание курьера возвращает {"ok":true}') 
    def test_register_courier_and_return_ok_true(self, register_rand_user):

        response = register_rand_user[1]

        actually_value = response.json()
        expected_value = Message.OK_TRUE
        assert actually_value == expected_value
        allure.attach(f"{response.json()}", "Message")
        
    @allure.title('Тест получения кода 409 при регистрации уже существующего курьера')
    @allure.description(
    'Если создать курьера с логином, который уже есть, возвращается ошибка 409')
    def test_register_courier_which_exist(self):

        response = CourierApiClient().post_reg_courier(CourierData.CURRENT_USER)
        
        actually_value = response.status_code
        expected_value = StatusCode.CONFLICT_409
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
       
    @allure.title('Тест получения кода 400 при регистрации нового курьера без указания логина')
    @allure.description(
    'Если поле "login" не заполнено, запрос возвращает ошибку 400')
    def test_register_courier_whithout_field_login_return_400(self):

        response = CourierApiClient().post_reg_courier(CourierData.NEW_USER_WHITHOUT_LOGIN)
        actually_value = response.status_code
        expected_value = StatusCode.BAD_REQUEST_400
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
    
    @allure.title('Тест получения текста ошибки при регистрации нового курьера без указания логина')
    @allure.description(
    'Если поле "login" не заполнено, запрос возвращает текст ошибки')
    def test_register_courier_whithout_field_login_return_error_message(self):

        response = CourierApiClient().post_reg_courier(CourierData.NEW_USER_WHITHOUT_LOGIN)
        
        actually_value = response.json()["message"]
        expected_value = Message.NOT_ENOUGTH_DATA_FOR_REG
        assert actually_value == expected_value
        allure.attach(f"{response.json()}", "Message")

    @allure.title('Тест получения кода 400 при регистрации нового курьера без указания пароля')
    @allure.description(
    'Если поле "password" не заполнено, запрос возвращает ошибку 400')
    def test_register_courier_whithout_field_password_return_400(self):

        response = CourierApiClient().post_reg_courier(CourierData.NEW_USER_WHITHOUT_PASS)
        actually_value = response.status_code
        expected_value = StatusCode.BAD_REQUEST_400
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
