from django.db import models

# Create your models here.
class ChickenManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        chickens_with_name = Chicken.objects.filter(name=reqPOST['chicken_name'])
        if len(chickens_with_name) >= 1:
            errors['unique'] = "Name already taken"
        if len(reqPOST['chicken_name']) < 3:
            errors['name'] = "Name is too short, use at least 3 characters"
        if len(reqPOST['color']) < 3:
            errors['color'] = "Color is too short, use at least 3 characters"
        return errors

    def edit_validator(self, reqPOST, chicken_id):
        errors = {}
        chickens_with_name = Chicken.objects.filter(name=reqPOST['chicken_name'])
        if len(chickens_with_name) >= 1:
            if chicken_id != chickens_with_name[0].id:
                errors['unique'] = "Name already taken"
        if len(reqPOST['chicken_name']) < 3:
            errors['name'] = "Name is too short, use at least 3 characters"
        if len(reqPOST['color']) < 3:
            errors['color'] = "Color is too short, use at least 3 characters"
        return errors

class Chicken(models.Model):
    name = models.TextField()
    color = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ChickenManager()
    