from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def create_valdiator(self, reqPOST):
        errors = {}
        if len(reqPOST['user_name']) < 3:
            errors['user_name'] = "Name is too short"
        if len(reqPOST['email']) < 6:
            errors['email'] = "Email is too short"
        if len(reqPOST['password']) < 8:
            errors['email'] = "Password is too short"
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['match'] = "Password and password confirmation dont match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqData['email']):            
            errors['regex'] = ("Email in wrong format")
        users_with_email = User.objects.filter(email=reqPOST['email'])
        if len(users_with_email) >= 1:
            errors['dup'] = "Email taken, use another"
        return errors

class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class GiraffeManager(models.Manager):
    def create_validator(self, reqPOST):
        if len(reqPOST['giraffe_name']) < 3:
            errors['giraffe_name'] = "Name is too short"
        if len(reqPOST['catchphrase']) < 6:
            errors['catchphrase'] = "Catchphrase is too short"
        if len(reqPOST['password']) < 8:
            errors['email'] = "Password is too short"

class Giraffe(models.Model):
    name = models.TextField()
    catchphrase = models.TextField()
    owner = models.ForeignKey(User, related_name="giraffes_owned", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GiraffeManager()