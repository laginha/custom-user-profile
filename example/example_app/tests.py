from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldError
from .models import Buyer, Seller

User = get_user_model()


class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.get_or_create(email='some@email.com')[0]
        self.seller = Seller.objects.get_or_create(user=self.user)[0]
    
    def test_manager(self):
        self.assertEqual( User.queryset.seller().filter(email__isnull=False).count(), 1 )
        self.assertEqual( User.queryset.buyer().count(), 0 )
        self.assertRaises( FieldError, User.queryset.something )
        
    def test_get_profile(self):
        self.assertEqual( self.seller.user.seller, self.user.profile )

    def test_is_profile(self):
        self.assertEqual( self.seller.user.is_profile('seller'), self.user.is_seller )
        self.assertTrue( self.user.is_profile('seller') )
        self.assertEqual( self.seller.user.is_profile('buyer'), self.user.is_buyer )
        self.assertFalse( self.user.is_profile('buyer') )
        self.assertEqual( self.seller.user.is_profile('something'), self.user.is_something )
        self.assertFalse( self.user.is_profile('something'), False )
