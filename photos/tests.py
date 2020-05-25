from django.test import TestCase

# Create your tests here.from django.test import TestCase
from .models import Images,Category,Location


# Create your tests here.


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nairobi = Location(locs_name='nairobi')
        self.animals = Category(name='general')
        self.image = Image(image='media/download.jpeg',image_name='animal', image_descprition='best gift you can give to lover',location=self.nairobi,category=self.animals, id=1)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    # Testing Save Method

    def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name = 'animals', id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

    def test_save_method(self):
        self.category.save_category()
        cate = Category.objects.all()
        self.assertTrue(len(cate)>0)
        
    def test_delete_method(self):
        self.category.delete_category
        cate = Category.objects.all()
        self.assertTrue(len(cate) is 0)
        
    def test_display_all(self):
        animals = Category(name='general')
        animals.save_category()
        one = Category.objects.all()
        print(len(one))
        self.assertTrue(len(one),2)
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.nairobi = Location(locs_name = 'nairobi', id=1)
        
        
    #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location)) 

    def test_save_method(self):
        self.nairobi.save_locs()
        images = Location.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_method(self):
        self.nairobi.delete_locs()
        locations = Location.objects.all()
        self.assertTrue(len(locations) is 0)
        
    def test_display_all(self):
        animal= Location(loc_name='nairobi')
        animal.save_loc()
        self.nairobi.save_loc()
        locations = Location.objects.all()
        print(len(locations))
        self.assertTrue(len(locations),2)

        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        


    