from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phones/')
    description = models.TextField()
    buy_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
