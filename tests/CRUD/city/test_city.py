from app.entity.mongo.city import City
from tests.test_client import FlaskClientTestCase


class CityTestCase(FlaskClientTestCase):

    # Ensure city is inited
    def test_create(self):
        city = City(name="Long an")
        self.assertTrue(city.name, "Long an")

    # Ensure list city is showed
    def test_list_cate(self):
        with self.client:
            response = self.client.get('/city', follow_redirects=True)
            self.assertIn(b'City Table', response.data)

    # Ensure city is created
    def test_create_city(self):
        with self.client:
            response = self.client.post('/city/create', data=dict(
                cityName="Khulalumbua"
            ), follow_redirects=True)
            self.assertIn(response.status, '200 OK')

    # Ensure city is created with city_name is empty
    def test_create_city_1(self):
        with self.client:
            response = self.client.post('/city/create', data=dict(
                cityName=""
            ), follow_redirects=True)
            self.assertIn(b"Your city is error", response.data)

    # Ensure api list city is working correctly
    def test_api_list_cate(self):
        with self.client:
            response = self.client.get('/city/api/list?page=1', follow_redirects=True)
            self.assertIn(response.status, '200 OK')

    # Ensure city is edit
    def test_edit_prod(self):
        with self.client:
            response = self.client.post('/city/edit', data=dict(
                city_id="1",
                city_name="Viet Nam vo dich"
            ), follow_redirects=True)
            self.assertIn(response.status, '200 OK')
