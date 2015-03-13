from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Buyer, Seller

User = get_user_model()


class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.get_or_create(email='some@email.com')[0]
        self.seller = Seller.objects.get_or_create(user=self.user)[0]
        
    def test_get_profile(self):
        assert self.seller.user.seller == self.user.profile

    def test_is_profile(self):
        assert self.seller.user.is_profile('seller') == self.user.is_seller
        assert self.user.is_profile('seller') == True
        assert self.seller.user.is_profile('buyer') == self.user.is_buyer
        assert self.user.is_profile('buyer') == False
        assert self.seller.user.is_profile('something') == self.user.is_something
        assert self.user.is_profile('something') == False
