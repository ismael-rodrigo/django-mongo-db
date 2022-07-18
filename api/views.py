from bson import ObjectId
from django.shortcuts import render
from rest_framework.views import APIView
from api.database import db
from rest_framework.response import Response
import json
from bson import json_util


class ProductView(APIView):
    def post(self,request):
        products_collection = db['products']
        new_product = products_collection.insert_one(request.data)
        return Response(data={"_id":str(new_product.inserted_id)})


    def get(self,request):
        products_collection = db['products']

        #all_products = list(products_collection.find({}, {'_id': False}))   #descoment if not return _id from query
        all_products = list(products_collection.find({}))   
        all_products_json = json.loads(json_util.dumps(all_products))  
        return Response(data=all_products_json)
        