from django.db import models


class Listings(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bed = models.IntegerField()
    num_bath = models.IntegerField()
    sq_foot = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return f'{self.title}'