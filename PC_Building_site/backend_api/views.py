# from rest_framework.views import APIView
# from .serializer import ProcessorSerializer
# from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def configurator_index(request):
    return render(request, 'backend_api/configurator-index.html')


def configurator_constructor(request):
    total_price = 0
    post_data = {}
    if request.method == "POST":
        post_data = request.POST
        for item in Processor.objects.all():
            if post_data['processor'] == item.name:
                total_price += item.price

        for item in CoolingSystem.objects.all():
            if post_data['cooling_system'] == item.name:
                total_price += item.price

        for item in Motherboard.objects.all():
            if post_data['motherboard'] == item.name:
                total_price += item.price

        for item in RAM.objects.all():
            if post_data['ram'] == item.name:
                total_price += item.price

        for item in Videocard.objects.all():
            if post_data['videocard'] == item.name:
                total_price += item.price

        for item in HDD.objects.all():
            if post_data['hdd'] == item.name:
                total_price += item.price

        for item in SSD.objects.all():
            if post_data['ssd'] == item.name:
                total_price += item.price

        for item in PowerUnit.objects.all():
            if post_data['power_unit'] == item.name:
                total_price += item.price

    context = {
        "processors": Processor.objects.all(),
        "cooling_systems": CoolingSystem.objects.all(),
        "motherboards": Motherboard.objects.all(),
        "rams": RAM.objects.all(),
        "videocards": Videocard.objects.all(),
        "hdds": HDD.objects.all(),
        "ssds": SSD.objects.all(),
        "power_units": PowerUnit.objects.all(),

        # "form": form,
        "total_price": total_price,
        # "user_choice": user_choice,

    }

    return render(request, 'backend_api/configurator-constructor.html', context=context)


def configurator_help(request):
    context = {
        "processors": Processor.objects.all(),
        "cooling_systems": CoolingSystem.objects.all(),
        "motherboards": Motherboard.objects.all(),
        "rams": RAM.objects.all(),
        "videocards": Videocard.objects.all(),
        "hdds": HDD.objects.all(),
        "ssds": SSD.objects.all(),
        "power_units": PowerUnit.objects.all(),
    }
    return render(request, 'backend_api/configurator-help.html', context=context)

#
# class ProcessorView(APIView):
#
#     def get(self, request):
#         output = [
#             {
#                 "name": output.name,
#                 "firm": output.firm,
#                 "frequency": output.frequency,
#                 "soket": output.soket,
#                 "core_number": output.core_number,
#                 "price": output.price
#             } for output in Processor.objects.all()
#         ]
#         return Response(output)
