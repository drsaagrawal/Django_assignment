from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Category(models.Model):  
	category_id = models.IntegerField(primary_key=True) 
	category_name =  models.CharField(max_length=120)
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name

class SubCategory(models.Model):  
	cat_id = models.ForeignKey(Category)
	subcategory_id = models.IntegerField(primary_key=True) 
	subcategory_name =  models.CharField(max_length=120)

	class Meta:
		verbose_name = 'SubCategory'
		verbose_name_plural = 'SubCategories'

	def __str__(self):
		return self.subcategory_name

class Product(models.Model):  
	sub_cat_id = models.ForeignKey(SubCategory)
	product_id = models.IntegerField(primary_key=True) 
	product_name =  models.CharField(max_length=120)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.product_name

