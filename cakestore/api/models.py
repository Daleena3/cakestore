from django.db import models




class Cakes(models.Model):
    name=models.CharField(max_length=10)
    weight=models.PositiveBigIntegerField()
    shape=models.CharField(max_length=10)
    description=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images",null=True)
    price=models.PositiveBigIntegerField()


    def __str__(self): 
        return self.name()


