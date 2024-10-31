from django.db import models
class Category(models.Model):
    image = models.ImageField(upload_to="category/image", null=True, blank=True)
    name=models.CharField(max_length=20)
    discription=models.TextField()


    def __str__(self):
        return self.name
class Products(models.Model):
    image = models.ImageField(upload_to="products/image", null=True, blank=True)
    name=models.CharField(max_length=20)
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    Available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
