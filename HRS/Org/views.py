import json
from django.shortcuts import render
from django.views import View
from .models import *
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from .forms import *


# Create your views here.

# API for CRUD operations on USER

class UsersApp(View):
    # To Fetch a list of users
    @csrf_exempt
    def get(self, request,phone=None):
        try:
            if request.method == 'GET':
                if phone:
                    user_obj = Users.objects.get(phone=phone)
                    many = False
                else:
                    user_obj = Users.objects.all()
                    many = True
                user_obj = UserSerializer(user_obj, many=many).data
                if user_obj:
                    response = {"code": "200", "message": "Success", "data": user_obj}
                else:
                    response = {"code": "400", "message": "No Data Found", "data": {}}
            else:
                response = {"code": "400", "Please check the method": "False", "data": {}}
        except Exception as e:
            print(e)
            response = {"code": "500", "message": "False", "data": {"error": e}}
        return JsonResponse(response, safe=False)

    # To create a new user
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                password = data.get('password', None)
                data['password'] = make_password(password)
                '''This is one type of method to save the data'''
                # user_obj = Users.objects.create(
                #     first_name=data.get('first_name'),
                #     last_name=data.get('last_name'),
                #     password=password,
                #     is_active=data.get('is_active'),
                #     valid_until=data.get('valid_until')
                #     )
                # user_obj.save()
                # user_obj = Users.objects.get(id=user_obj.id)
                # serializer = UserSerializer(data=user_obj)
                # data1= UsersForm(data)
                # if data1.clean():
                #     print(data1)
                serializer = UserSerializer(data=data)
                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                    response = {"code": "200", "message": "Success", "data": serializer.data}
                else:
                    response = {"code": "400", "message": "False", "data": serializer.errors}
            else:
                response = {"code": "400", "Please check the method": "False", "data": {}}
        except Exception as e:
            print(e)
            response = {"code": "500", "message": "False", "data": {"error": e}}
        return JsonResponse(response, safe=False)

    # To update a user
    @csrf_exempt
    def put(self, request):
        try:
            if request.method == 'PUT':
                payload = json.loads(request.body)
                password = payload.get('password', None)
                if password:
                    payload['password'] = make_password(password)
                user_data = Users.objects.filter(id=payload['id'])
                user_data.update(**payload)
                data = Users.objects.get(id=payload['id'])
                serializer = UserSerializer(data)
                data = serializer.data
                response = {"code": "200", "User Data Updated Successfully": "Success", "data": data}
            else:
                response = {"code": "400", "Please check the method": "False", "data": {}}
        except Exception as e:
            print(e)
            response = {"code": "500", "message": False, "data": {"error": e}}
        return JsonResponse(response, safe=False)
    
    # To delete a user
    @csrf_exempt
    def delete(self, request, phone):
        try:
            if request.method == 'DELETE':
                # payload = json.loads(request.body)
                
                user_data = Users.objects.filter(phone=phone)
                user_data.delete()
                response = {"code": "200", "User Data Deleted Successfully": "Success", "data": {}}
            else:
                response = {"code": "400", "Please check the method": "False", "data": {}}
        except Exception as e:
            print(e)
            response = {"code": "500", "message": "False", "data": {"error": e}}
        return JsonResponse(response, safe=False)
    

# API for CRUD operations on ORGANIZATION
class OrganizationApi(View):

    # To Fetch a list of organizations
    @csrf_exempt
    def get(self, request, org_id=None):
        try:
            if request.method == "GET":
                if org_id:
                    org_obj = Organization.objects.get(org_id= org_id)
                    many = False
                else:
                    org_obj = Organization.objects.all()
                    many = True
                org_obj = OrganizationSerializer(org_obj, many=many).data
                if org_obj:
                    response = {'code': 200, "message": 'Success',"data":org_obj}
                else:
                    response = {'code': 400, "message": 'No Data found', "data": {}}
            else:
                response = {"code": 404, "message": "Method found found", "data":{}}
        except Exception as e:
            print(e)
            response = {'code': 500, "message": False, "data":{"error": e}}
        return JsonResponse(response, safe=True)

    #To Create Organizations Data
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                payload = request.data
                serializer = OrganizationSerializer(data = payload)
                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                    response = {"code": 200, "message": "Data created", "data": serializer.data}
                else:
                    response = {"code": 200, "message": False, "data": serializer.error}
            else:
                response = {"code": 404, "message": "Method found found", "data":{}}
        except Exception as e:
            print(e)
            response = {"code": 500, "message": False, "data":{"error": e}}
        return JsonResponse(response, safe=True)
    

    #To Update Organizations Data
    @csrf_exempt
    def put(self, request):
        try:
            if request.method =='PUT':
                payload =json.loads(request.body)
                org_inst = Organization.objects.filter(org_id = payload['org_id'])
                org_inst.update(**payload)
                org_obj = Organization.objects.get(org_obj = payload['org_id'])
                serializer = OrganizationSerializer(org_obj)
                data = serializer.data
                response = {"code": 200, "message": True, "data": data}
            else:
                response = {"code": 404, "message": "Method found found", "data":{}}
        except Exception as e:
            print(e)
            response = {"code": 500, "message": False, "data": {"error": e}}
        return JsonResponse(response, safe=False)

    #To delete Organization Data
    @csrf_exempt
    def delete(self, request, org_id):
        try:
            if request.method == 'DELETE':
                org_obj = Organization.objects.filter(org_id = org_id)
                org_obj.delete()
                response = {"code": 200, "messgae": "Records delete sucesfully", "data": {}}
            else:
                response = {"code": 400, "messgae": False, "data": {}}
        except Exception as e:
            print(e)
            response = {"code": 500, "message": False, "data": {}}
        return JsonResponse(response, safe=True)


#API for Login
class LoginApi(View):

    @csrf_exempt
    def post(self, request):
        try:
            user = request.user
            print(user)
            if request.method == 'POST':
                payload = json.loads(request.body)
                print(payload)
                username = payload.get('username', None)
                user = Users.objects.get(phone= username)
                if user:
                    if check_password(payload.get('password', None), user.password):
                        serializer = UserSerializer(user)
                        response = {"code": 200, "message": True, "data": serializer.data}
                    else:
                        response = {"code": 400, "message": "Please Check the password", "data": {}}
                else:
                    response = {"code": 404, "message": "User is not found", "data": {}}
            else:
                response = {"code": 404, "message": "Method Not found", "data": {}}
        except Exception as e:
            print(e)
            response = {"code": 500, "message": False, "data": {"error": e}}
        return JsonResponse(response, safe=False)