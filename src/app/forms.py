from django import forms
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()

class SubcategoryForm(forms.Form):
	Category_id = forms.IntegerField()

class ProductSubcategoryForm(forms.Form):
	SubCategory_id = forms.IntegerField()

class ProductCategoryForm(forms.Form):
	Category_id = forms.IntegerField()

class InsertProductForm(forms.Form):
	#Category_id = forms.IntegerField()
	SubCategory_id = forms.IntegerField()
	Product_name = forms.CharField()
	Product_id = forms.IntegerField()

	def clean_Product_id(self):
		Product_id = self.cleaned_data.get("Product_id")
		print(Product_id)
		qs = Product.objects.filter(product_id=Product_id)
		print(qs)
		if (qs.exists()):
			raise forms.ValidationError("Prod Id taken")
		else:
			print("Inserted")
			return Product_id