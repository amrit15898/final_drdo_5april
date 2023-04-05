from .models import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def my_context_processor(request):

    dir_objs= Appointment.objects.filter(Q(date__gte = datetime.now()) & Q(final_status= "Pending")).count()
    dir_objs1 = Appointment.objects.filter(Q(date__gte = datetime.now()) & Q(final_status= "Pending"))
    # print(dir_objs1)
    

    context = {}
    context["dir_objs"] = dir_objs
    context["dir_objs1"] = dir_objs1
    context["user"] = request.user
    # print(context)

    return {"data":context}

   
        


