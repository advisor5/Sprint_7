import allure
from courier.courier_routes import CourierApiClient
from data.constants import Parameter
from data.constants import StatusCode
from data.constants import Message


class TestOrderList:
    @allure.title('Тест успешного получения списка заказов при запросе')
    @allure.description(
    'Проверка, что на запрос списка заказов возвращается код 200') 
    def test_get_order_return_200(self):
        
        response = CourierApiClient().get_order_list(Parameter.PARAMS, Parameter.HEAREDS)
        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
    
    @allure.title('Тест возвращения ответа списка заказов в формате словаря')
    @allure.description(
    'Проверка, что в тело ответа возвращается список заказов в формате словаря') 
    def test_get_order_return_dict(self):
        
        response = CourierApiClient().get_order_list(Parameter.PARAMS, Parameter.HEAREDS)
        actually_value = type(response.json())
        expected_value = dict
        assert actually_value == expected_value
        allure.attach(f"{response.json()}", "Message")

    @allure.title('Тест наличия текста "orders" в возвращаемом списке заказов')
    @allure.description(
    'Проверка, что тело ответа со списком заказов содержит ключ "orders"') 
    def test_get_order_return_key_orders_in_list(self):
        
        response = CourierApiClient().get_order_list(Parameter.PARAMS, Parameter.HEAREDS)
        actually_value = response.json()
        expected_value = Message.KEY_ORDERS
        assert expected_value in actually_value
        allure.attach(f"{response.json()}", "Message")
