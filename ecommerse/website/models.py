from django.db import models

# Create your models here.

class catagory(models.Model):
    catagory_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.catagory_name
    


class product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_catagory =models.ForeignKey(catagory, on_delete= models.CASCADE)
    subcatagory =models.CharField(max_length =70, default="")
    catagory =models.CharField(max_length = 70 ,default="")
    product_name = models.CharField(max_length = 50)
    product_details = models.TextField()
    product_price = models.IntegerField(default=0)
    published_date = models.DateField()
    product_image = models.FileField()

    def __str__(self):
        return self.product_name


