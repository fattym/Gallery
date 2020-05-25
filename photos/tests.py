from django.test import TestCase

# Create your tests here.from django.test import TestCase
from .models import *


# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Test case for the Location class and it's behaviours.
    '''

    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location( locs = "Nairobi")

    def tearDown(self):
        Location.objects.all().delete()

  
    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly.
        '''
        self.assertTrue(isinstance(self.new_location, Location))


    def test_save_method(self):
        '''
        Method to check whether the locations are getting saved.
        '''
        self.new_location.save()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

