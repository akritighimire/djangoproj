# Create your models here.
from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    password = models.CharField (max_length=100)
    active = models.BooleanField (default=False)
    created_on = models.DateField(auto_now_add=True)
    last_logged_in = models.DateField(auto_now_add=True)
    
    def __str__ (self):
        return self.name 

    """
    class => attributes and behaviours ko comination ho hai
    Charfiled like varchar
    
    In [3]: a = User ( name = "ram" , email = "ram@gmail.com" , password = "ram123")
    s.save()
    yo garda sqlite ko code aafai django ko orm lae aafai banaidinxa

    INSERT INTO userapp_users (name,email,password ,active ,.......) VALUES (........)
    
    
    In [22]: User.objects.filter( name = "hari")
    Out[22]: <QuerySet [<User: hari>]>
    
    SELECT * from userapp_user where name ="hari"
    
    
    In [25]: In [24]: User.objects.filter( email = "hari@gmail.com", password= "ram123")
    
    SELECT * from userapp_user where email = "hari@gmail.com " and password = "ram123"
    """
