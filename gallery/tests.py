from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class MyGalery_TestCases(TestCase):
    def setUp(self):
        self.new_category = Category(cat_name='ladiesbodycon')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'Mombasa')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='bodycon dress', image_description='bodycon dress 2017',image_path='media/gallery/ladiesbodycon-3134828_1920.jpg',image_category=self.new_category,image_location=self.new_location)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='bodycon dress')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.image_name,'bodycon dress')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('bodycon dress','Greener')
        fetched = Image.objects.get(image_name='Greener')
        self.assertEqual(fetched.image_name,'Greener')
        
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    def test_search_by_category(self):
        self.new_image.save_image()        
        fetch_specific = Category.objects.get(cat_name='ladiesbodycon')
        self.assertTrue(fetch_specific.cat_name=='ladiesbodycon')

    def test_filter_by_location(self):
        self.new_image.save_image()        
        fetch_specific = Location.objects.get(location_name='Mombasa')
        self.assertTrue(fetch_specific.location_name=='Mombasa')
