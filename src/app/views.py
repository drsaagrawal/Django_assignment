from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
from .models import Category,SubCategory,Product
from .forms import SubcategoryForm,ProductSubcategoryForm,ProductCategoryForm,InsertProductForm
from django.contrib.auth import get_user_model

from django.views.generic import ListView,DetailView

#User = get_user_model()

class CategoryList(ListView):
	queryset = Category.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.category_name)
	template_name = "category/cat_list.html"


def SubCategoryList(request):
	subcategory_form = SubcategoryForm(request.POST or None)
	context ={
	'form' : subcategory_form
	}

	if subcategory_form.is_valid():
		#print("Hi")
		print(subcategory_form.cleaned_data['Category_id'])
		qs = SubCategory.objects.filter(cat_id=subcategory_form.cleaned_data['Category_id'])

		print(qs)
		return render(request,"Subcategory/cat_sub_list.html",{'posts': qs})

	return render(request,"Subcategory/sub_list.html",context)



def ProductSubCategoryList(request):
	productsubcategory_form = ProductSubcategoryForm(request.POST or None)
	context ={
	'form' : productsubcategory_form
	}

	if productsubcategory_form.is_valid():
		#print("Hi")
		print(productsubcategory_form.cleaned_data['SubCategory_id'])
		qs = Product.objects.filter(sub_cat_id=productsubcategory_form.cleaned_data['SubCategory_id'])

		print(qs)
		return render(request,"Product/sub_prod_list.html",{'posts': qs})

	return render(request,"Product/prod_list.html",context)


def ProductCategoryList(request):
	productcategory_form = ProductCategoryForm(request.POST or None)
	context ={
	'form' : productcategory_form
	}

	if productcategory_form.is_valid():
		#print("Hi")
		print(productcategory_form.cleaned_data['Category_id'])
		qs = Product.objects.filter(sub_cat_id__cat_id__category_id__contains=productcategory_form.cleaned_data['Category_id'])
		#qs = SubCategory.objects.filter(cat_id=productcategory_form.cleaned_data['Category_id'])
		#qss = Product.objects.filter( in qs)

		print(qs)
		return render(request,"Product/prod_cat_list.html",{'posts': qs})

	return render(request,"Product/prod_cat.html",context)

def InsertProduct(request):
	category = {1:"Electronics",2:"Clothings"}
	#print(category[1])
	insertproduct_form = InsertProductForm(request.POST or None)
	context ={
	'form' : insertproduct_form
	}

	if insertproduct_form.is_valid():
		print(insertproduct_form.cleaned_data)
		
		subcategory_id = insertproduct_form.cleaned_data['SubCategory_id']
		prod_name = insertproduct_form.cleaned_data['Product_name']
		prod_id = insertproduct_form.cleaned_data['Product_id']
 		
		Product.objects.create(sub_cat_id_id=subcategory_id, product_id=prod_id,product_name=prod_name)
		

	return render(request,"Product/insert_prod.html",context)