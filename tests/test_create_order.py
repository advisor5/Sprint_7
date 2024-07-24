import pytest
import allure
import json
from data.constants import StatusCode
from data.constants import Order
from data.constants import Parameter
from data.constants import Message
from courier.courier_routes import CourierApiClient


class TestCreateOrder:
    @allure.title('Тест успешного создания заказа')
    @allure.description(
    'Проверка, что заказ создается указав цвета: (нет цвета, черный, серый, оба цвета) и возвращается код 201')
    @pytest.mark.parametrize('color', Order.COLORS)
    def test_create_order_with_colors_and_return_201(self, color):

        data = Order.DATA_ORDER_WITHOUT_COLOR
        data["color"]=color
        payload = json.dumps(data)
        
        response = CourierApiClient().create_order(payload, Parameter.HEAREDS)

        actually_value = response.status_code
        expected_value = StatusCode.CREATED_201
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")


    @allure.title('Тест содержания в ответа ключа "track" при успешном создания заказа')
    @allure.description(
    'Проверка, что при успешном создании заказа тело ответа содержит "track"')
    def test_create_order_and_return_track(self):

        data = Order.BASE_ORDER
        payload = json.dumps(data)
        response = CourierApiClient().create_order(payload, Parameter.HEAREDS)

        actually_value = response.json()
        expected_value = Message.KEY_TRACK
        assert expected_value in actually_value
        allure.attach(f"{response.json()}", "Message")
