import random

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CustomerApp.models import StatusCatalogs, Customers, Groups
from CustomerApp.serializers import StatusCatalogSerializer, CustomerSerializer, GroupSerializer

from django.core.files.storage import default_storage


# Create your views here.
@csrf_exempt
def groupApi(request, id=0):
    if request.method == 'GET':
        groups = Groups.objects.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse("Registro Guardado", safe=False, status=201)
        return JsonResponse("Fallo al guardar Registro", safe=False, status=422)

    elif request.method == 'PUT':
        group_data = JSONParser().parse(request)
        group = Groups.objects.get(GroupsId=group_data['GroupsId'])
        group_serializer = GroupSerializer(group, data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse("Registro Actualizado", safe=False, status=200)
        return JsonResponse("Fallo al Actualizar", safe=False)

    elif request.method == 'DELETE':
        group = Groups.objects.get(GroupsId=id)
        group.delete()
        return JsonResponse("Registro Eliminado Exitosamente", safe=False)

@csrf_exempt
def statuscatalogsApi(request, id=0):
    if request.method == 'GET':
        catalogs = StatusCatalogs.objects.all()
        catalogs_serializer = StatusCatalogSerializer(catalogs, many=True)
        return JsonResponse(catalogs_serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        catalogs_data = JSONParser().parse(request)
        catalogs_serializer = StatusCatalogSerializer(data=catalogs_data)
        if catalogs_serializer.is_valid():
            catalogs_serializer.save()
            message = 'Registro creado correctamente'
            return JsonResponse(message, safe=False, status=201)
        return JsonResponse("Fallo al guardar Registro", safe=False, status=200)

    elif request.method == 'PUT':
        catalogs_data = JSONParser().parse(request)
        catalog = StatusCatalogs.objects.get(CatalogId=catalogs_data['CatalogId'])
        catalogs_serializer = StatusCatalogSerializer(catalog, data=catalogs_data)
        if catalogs_serializer.is_valid():
            catalogs_serializer.save()
            message = 'Registro actualizado correctamente'
            return JsonResponse(message, safe=False, status=200)
        return JsonResponse("Fallo al Actualizar", safe=False, status=204)

    elif request.method == 'DELETE':
        catalog = StatusCatalogs.objects.get(catalogId=id)
        catalog.delete()
        message = 'Registro eliminado correctamente'
        return JsonResponse(message, safe=False, status=200)


@csrf_exempt
def customerApi(request, id = 0):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_serializer.data, safe=False)

    elif request.method == 'POST':
        customers_data = JSONParser().parse(request)
        print(customers_data)
        customer_serializer = CustomerSerializer(data=customers_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            message = 'Registro creado correctamente'
            return JsonResponse(message, safe=False, status=201)

        print(customer_serializer.errors)
        return JsonResponse("Fallo al guardar Registro", safe=False, status=200)

    elif request.method == 'PUT':
        customers_data = JSONParser().parse(request)
        customer = Customers.objects.get(CustomerId=customers_data['CustomerId'])
        customer_serializer = CustomerSerializer(customer, data=customers_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            message = 'Registro actualizado correctamente'
            return JsonResponse(message, safe=False, status=200)
        print(customer_serializer.errors)
        return JsonResponse("Fallo al Actualizar", safe=False, status=204)

    elif request.method == 'DELETE':
        customer = Customers.objects.get(CustomerId=id)
        customer.delete()
        message = 'Registro eliminado correctamente'
        return JsonResponse(message, safe=False, status=200)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


@csrf_exempt
def checkBC(request, id=0):
    if request.method == 'PUT':
        if request.method == 'PUT':
            customer = Customers.objects.filter(CustomerId=id).update(StatusBC=1)
            if customer:
                message = 'BC Favorable'
                return JsonResponse(message, safe=False, status=204)
            else:
                message = 'BC no se pudo consultar'
                return JsonResponse(message, safe=False, status=204)


@csrf_exempt
def checkPLD(request, id=0):
     if request.method == 'PUT':
         customer = Customers.objects.filter(CustomerId=id).update(StatusPLD=1)
         if customer:
             message = 'PLD Favorable'
             return JsonResponse(message, safe=False, status=204)
         else:
             message = 'PLD no se pudo consultar'
             return JsonResponse(message, safe=False, status=204)


@csrf_exempt
def checkWL(request, id=0):
     if request.method == 'PUT':
        customer = Customers.objects.filter(CustomerId=id).update(StatusWL=1)
        if customer:
            message = 'WL Favorable'
            return JsonResponse(message, safe=False, status=204)
        else:
            message = 'WL no se pudo consultar'
            return JsonResponse(message, safe=False, status=204)


@csrf_exempt
def leadToCustomer(request, id=0):
    if request.method == 'PUT':
        customer = Customers.objects.filter(CustomerId=id, StatusBC=1, StatusWL=1, StatusPLD=1).update(Status=1)
        if customer:
            message = 'Cliente creado correctamente'
            return JsonResponse({'status': customer, 'description': message}, status=204)
        else:
            message = 'El prospecto no supero las validaciones'
            return JsonResponse({'status': customer, 'description': message}, status=204)


@csrf_exempt
def validateLead(request, id=0):
    if request.method == 'PUT':
        res = random.choice([True, False])
        if res:
            message = 'Prospecto validado correctamente'
            Customers.objects.filter(CustomerId=id).update(StatusBC=1, StatusWL=1, StatusPLD=1)
            return JsonResponse({'status': 'true', 'description': message}, status=201)
        else:
            message = 'Prospecto no viable'
            Customers.objects.filter(CustomerId=id).update(StatusBC=0, StatusWL=0, StatusPLD=0, Status=0)
            return JsonResponse({'status': 'true', 'description': message}, status=200)
