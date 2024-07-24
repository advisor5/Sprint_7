class Url:
    HOST = 'https://qa-scooter.praktikum-services.ru'

class CourierAPI:
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    ORDER = '/api/v1/orders'
    
class Parameter:
    PARAMS = {"limit": 1, "page": 0}
    HEAREDS = {"Content-type": "application/json"}

class StatusCode:
    OK_200 = 200
    CREATED_201 = 201
    BAD_REQUEST_400 = 400
    NOT_FOUND_404 = 404
    CONFLICT_409 = 409

class Message:
    NOT_FOUND_ID = "Учетная запись не найдена"
    NOT_ENOUGTH_DATA = "Недостаточно данных для входа"
    NOT_ENOUGTH_DATA_FOR_REG = "Недостаточно данных для создания учетной записи"
    OK_TRUE = {"ok": True}
    KEY_TRACK = "track"
    KEY_ID = 'id'
    KEY_ORDERS = 'orders'

class CourierData:
    NOT_EXIST_USER = {
            "login": "sergeik14",
            "password": "1234"
        }
    
    NEW_USER  = {
            "login": "dzheday007",
            "password": "1234",
            "firstName": "Obi"
        }
    
    DATA_FOR_LOGIN={
            "login": NEW_USER['login'],
            "password": NEW_USER['password']
        }
    
    NEW_USER_WHITHOUT_LOGIN = {
            "login": "",
            "password": NEW_USER['password'],
            "firstName": NEW_USER['firstName']
        }
    
    NEW_USER_WHITHOUT_PASS = {
            "login": NEW_USER['login'],
            "password": "",
            "firstName": NEW_USER['firstName']
        }
    CURRENT_USER = {
            "login": "dzheday001",
            "password": "1234",
            "firstName": "Obi"
        }

class Order:
    BASE_ORDER = {
        "firstName": "Sergei",
        "lastName": "Ivanov",
        "address": "Moscow, 51",
        "metroStation": 7,
        "phone": "+7 800 355 35 35",
        "rentTime": 7,
        "deliveryDate": "2020-07-07",
        "comment": "order for Sergei",
        "color": ["BLACK"]
        }
    
    DATA_ORDER_WITHOUT_COLOR = {
        "firstName": "Sergei",
        "lastName": "Ivanov",
        "address": "Moscow, 51",
        "metroStation": 7,
        "phone": "+7 800 355 35 35",
        "rentTime": 7,
        "deliveryDate": "2020-07-07",
        "comment": "order for Sergei"
        }
    
    COLORS = [[], ["BLACK"], ["GREY"], ["BLACK","GREY"]]