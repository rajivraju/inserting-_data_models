from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter a value')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    return HttpResponse('inserted data suceessfully')