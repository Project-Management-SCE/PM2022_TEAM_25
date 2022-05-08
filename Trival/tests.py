from django.test import TestCase
from django.urls import reverse
from paSSengersformes.models import passengers ,orders
from . import views

# Create your tests here.

class HomeAppViewTestCase(TestCase):
    def init_passengers(self):
        self.passengers = passengers()

    def setUp(self):
        self.user_1 = passengers.objects.create_user('test@email.com', 'temp1234')
        self.user_1.role = 1

    def tearDown(self):
        self.user_1.delete()

    def test_home_get(self):
        self.passengers.login(email='test@email.com', password='temp1234')
        response = self.client.get(reverse('home'))
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_passengers_post(self):
        self.passengers.login(email='test@email.com', password='temp1234')
        passengers_info = {}
        passengers_info['fn'] = "test Name"
        passengers_info['ln'] = 00.00
        passengers_info['phone'] = "000000000"
        passengers_info['id'] = "000000000"
        passengers_info['email'] = "test@gmail.com"
        passengers_info['gender'] = "gender"
        passengers_info['password'] = "True"
        passengers_info['age'] = "01/01/2004"
        passengers_info['country'] = "country"


        try:
            response = self.passengers.post(reverse('nurse'), data=json.dumps(nurse_info), content_type='application/json')
            self.assertEqual(response.status_code, 403)

        except Exception as e:
            pass



def test_nurse_post(self):
        orders_info = {}
        orders_info['chair'] = "Chair"
        orders_info['food'] = "Food"
        orders_info['hot'] = "Hot Drink"
        orders_info['cold'] = "Cold Drink"
        orders_info['other'] = "other"


        try:
            response = self.orders.post(reverse('nurse'), data=json.dumps(nurse_info), content_type='application/json')
            self.assertEqual(response.status_code, 403)

        except Exception as e:
            pass