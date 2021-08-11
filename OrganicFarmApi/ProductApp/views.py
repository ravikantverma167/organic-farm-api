from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ProductApp.models import Categories,Products
from ProductApp.serializers import CategorySerializer,ProductSerializer


# Create your views here.
@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        if id != 0:
          category=Categories.objects.get(id=id)
          category_serializer = CategorySerializer(category)
          return JsonResponse(category_serializer.data, safe=False)
          
        categories = Categories.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        category_data = JSONParser().parse(request)
        category=Categories.objects.get(id=id)
        category_serializer=CategorySerializer(category,data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        category=Categories.objects.get(id=id)
        category.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        if id != 0:
          product=Products.objects.get(id=id)
          product_serializer = ProductSerializer(product)
          return JsonResponse(product_serializer.data, safe=False)

        products = Products.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product=Products.objects.get(id=id)
        product_serializer=ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        product=Products.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
