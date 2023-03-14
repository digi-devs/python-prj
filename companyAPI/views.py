from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from companyAPI.models import CompanyModel
from companyAPI.serializers import CompanySerializer
from companyAPI.tasks import test_func

# Create your views here

def testCelery(request):
    test_func.delay()
    print('Printed result')
    return HttpResponse('Done Process2')



class GetCompany(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self,request):
        if request.method == 'GET':
            com_model = CompanyModel.objects.all()
            com_ser = CompanySerializer(com_model,many=True)
            return JsonResponse({'status':'200','companyData':com_ser.data},safe=False)
        else:
            return JsonResponse('No Data Found',safe=False)

class GetCompanyById(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self,request,company_id=0):
        if request.method == 'GET':
            com_model = CompanyModel.objects.get(company_id=company_id)
            com_ser = CompanySerializer(com_model,many=False)
            return JsonResponse({'status':'200','companyData':com_ser.data},safe=False)
        else:
            return JsonResponse({'status':'404','companyData':'No Company Found'},safe=False)

class PostCompany(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            com_data = JSONParser().parse(request)
            com_ser = CompanySerializer(data=com_data)
            if com_ser.is_valid():
                com_ser.save()      
                return JsonResponse({'status':'200','msg':'Added Sucessfully'},safe=False)
            return JsonResponse('Failed to Add Check company_type',safe=False)
        else:
            return JsonResponse('No Data Found',safe=False)

class PutCompany(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def put(self,request,company_id=0):
        if request.method == 'PUT':
            com_data = JSONParser().parse(request)
            com_model = CompanyModel.objects.get(company_id=com_data['company_id'])
            com_Ser = CompanySerializer(com_model,data=com_data)
            if com_Ser.is_valid():
                com_Ser.save()
                return JsonResponse("Updated Successfully",safe=False)
            return JsonResponse('Failed to Update Check company_type',safe=False)
        else:
            return JsonResponse('No Data Found',safe=False)

class DeleteCompany(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def delete(self,request,company_id=0):
        if request.method == 'DELETE':
            com_data = CompanyModel.objects.get(company_id=company_id)
            com_data.delete()
            return JsonResponse("Deleted Successfully",safe=False)
        else:
            return JsonResponse('No Data Found',safe=False)
