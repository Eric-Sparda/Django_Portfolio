from django.db import models

# Create your models here.
class logo(models.Model):
    name = models.CharField("Company name", max_length=60)
    img = models.ImageField("logo", upload_to='images')

    def __str__(self) -> str:
        return self.name
    
class welcome(models.Model):
    name = models.TextField("What do we provide")
    text = models.TextField("Text")
    
    def __str__(self) -> str:
        return self.name
    
class Content(models.Model):
    name = models.CharField("Company name", max_length=60)
    text = models.TextField("Text")
    img = models.ImageField("logo", upload_to='images')
    
    def __str__(self) -> str:
        return self.name
    
class text(models.Model):
    name = models.CharField("Company name", max_length=60)
    text = models.TextField("Text")
    img = models.ImageField("logo", upload_to='images')

    def __str__(self) -> str:
        return self.name
    

class price(models.Model):
    bigname = models.CharField("Company name", max_length=60)
    text = models.TextField("Text")
    plan_name = models.CharField("Plan", max_length=50,default='0000000', editable=True)
    price = models.PositiveBigIntegerField("Price")
    offer_1 = models.TextField("Offer1",default='0000000', editable=True)
    offer_2 = models.TextField("Offer2",default='0000000', editable=True)
    offer_3 = models.TextField("Offer3",default='0000000', editable=True)
    offer_4 = models.TextField("Offer4",default='0000000', editable=True)
    offer_5 = models.TextField("Offer5",default='0000000', editable=True)
    offer_6 = models.TextField("Offer6",default='0000000', editable=True)

    def __str__(self) -> str:
        return self.bigname
    
class contact(models.Model):
    name = models.CharField("Your name", max_length=60)
    email = models.TextField("mail")
    message = models.TextField("message")

    def __str__(self) -> str:
        return self.name