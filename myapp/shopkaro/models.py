from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category,
                               on_delete=models.CASCADE)  # incase we want to delete our subcategories when we ddelete categories
    sub_name = models.CharField(max_length=30)

    def __str__(self):
        return self.sub_name


class Product(models.Model):
    cat_id = models.ForeignKey(Category,
                               on_delete=models.CASCADE)  # incase we want to delete our subcategories when we ddelete categories
    subcat_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_description = models.TextField(max_length=5000)
    price = models.IntegerField()
    product_image1 = models.ImageField(upload_to="productimages", blank=True, null=True)
    product_image2 = models.ImageField(upload_to="productimages", blank=True, null=True)
    product_image3 = models.ImageField(upload_to="productimages", blank=True, null=True)
    discount = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name
