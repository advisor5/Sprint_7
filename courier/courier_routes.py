import allure
import requests
from data.constants import Url
from data.constants import CourierAPI


class CourierApiClient:
    
    @allure.step('POST запрос на ручку "/api/v1/courier" - регистрация курьера')
    def post_reg_courier(self, data):
        return requests.post(f"{Url.HOST}{CourierAPI.CREATE_COURIER}", data)
    
    @allure.step('POST запрос на ручку "/api/v1/courier/login" - авторизация курьера')    
    def post_login_courier(self, data):
        return requests.post(f"{Url.HOST}{CourierAPI.LOGIN_COURIER}", data)
    
    @allure.step('DELETE запрос на ручку "/api/v1/courier/" - удаление курьера')    
    def delete_courier(self, id):
        return requests.delete(f"{Url.HOST}{CourierAPI.DELETE_COURIER}{id}")
    
    @allure.step('POST запрос на ручку "/api/v1/orders" - создание заказа')
    def create_order(self, json, headers):
        return requests.post(f"{Url.HOST}{CourierAPI.ORDER}", json, headers=headers)
        
    @allure.step('GET запрос на ручку "/api/v1/orders" - получение списка заказов')
    def get_order_list(self, params, headers):
        return requests.get(f"{Url.HOST}{CourierAPI.ORDER}", params=params, headers=headers)
