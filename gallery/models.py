from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=255)
    image_description = models.TextField()
    image_path = CloudinaryField('image')
    image_date = models.DateTimeField(auto_now_add=True)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name


    @classmethod
    def get_image_by_id(cls,new_id):
        image_result = cls.objects.get(id=new_id)
        return image_result

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

        
    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item


    @classmethod
    def update_image(cls,current_value,new_value):
        updated_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return updated_object

    @classmethod
    def filter_by_location(cls,location):
        filtered_result = cls.objects.filter(image_location__location_name__icontains=location)
        return filtered_result


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_category_by_id(cls,category_id):
        category_result = Category.objects.get(id=category_id)
        return category_result

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(category_name__icontains=search_term)
        return search_result

class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    

