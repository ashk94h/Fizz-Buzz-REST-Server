from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ParameterSerializer
from .models import Parameter
from django.db import models

@api_view(['GET'])
def fizz_buzz(request):
    int_1 = request.query_params.get('int1')
    int_2 = request.query_params.get('int2')
    limit = request.query_params.get('limit')
    str_1 = request.query_params.get('str1')
    str_2 = request.query_params.get('str2')
    sr = ParameterSerializer(data=request.query_params)
    if sr.is_valid(raise_exception=True):
        parameter = Parameter.objects.filter(int1=int_1,int2=int_2,limit=limit,str1=str_1,str2=str_2).values()
        if parameter:
            parameter.update(hits=(parameter[0]['hits'] + 1)) 
        else:
            sr.save()

        int_1 = int(int_1)
        int_2 = int(int_2)
        limit = int(limit)

        number_string_list = [i for i in range(1,limit + 1)]

        for i in range(0,limit):
            if number_string_list[i] % int_1 == 0 and number_string_list[i] % int_2 == 0:
                number_string_list[i] = str_1 + str_2
            elif number_string_list[i] % int_1 == 0:
                number_string_list[i] = str_1
            elif number_string_list[i] % int_2 == 0:
                number_string_list[i] = str_2
            else:
                number_string_list[i] = str(number_string_list[i])

        return Response(number_string_list)
    # Code will not reach here as error response will be sent by is_valid() method
    else:
        return Response("Not Valid")
    

@api_view(['GET'])
def statistics(request):
    max_hits = Parameter.objects.aggregate(max_hits=models.Max('hits'))['max_hits']
    max_used_parameter = Parameter.objects.all().filter(hits=max_hits).values()
    return Response({"max_used_parameter":max_used_parameter})
