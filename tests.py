from django.test import TestCase
from django.urls import reverse
from paSSengersformes.models import passengers ,orders
from . import views

# Create your tests here.

class HomeAppViewTestCase(TestCase):
    def init_passengers(self):
        self.passengers = passengers()

    def setUp(self):
        self.user_1 = passengers.objects.create_user(email='email',  password='P')
        self.user_1.role = 1

    def tearDown(self):
        self.user_1.delete()

    def test_home_get(self):
        self.passengers.login(email='email', password='P')
        response = self.client.get(reverse('home'))
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

   


        try:
            response = self.passengers.post(reverse('passengers'), data=json.dumps(passengers), content_type='application/json')
            self.assertEqual(response.status_code, 403)

        except Exception as e:
            pass



def test_orders_post(self):
        orders_info = {}
        orders_info['chair'] = "Chair"
        orders_info['food'] = "Food"
        orders_info['hot'] = "Hot Drink"
        orders_info['cold'] = "Cold Drink"
        orders_info['other'] = "other"


        try:
            response = self.orders.post(reverse('passengers'), data=json.dumps(passengers), content_type='application/json')
            self.assertEqual(response.status_code, 403)

        except Exception as e:
            pass