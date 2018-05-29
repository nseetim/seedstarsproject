# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from HRapp.forms import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddDetailsSerializer

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def adddetails(request):
    if request.method == 'POST':  # If the form has bee submitted
        form = AddDetailsForm(request.POST)  # A form bound to the post data
        if form.is_valid():  # All validation rules have been passed
            #  process the data in form.cleaned_data
            username = request.POST.get('username', '')  # Using the POST.get method to avoid
            # errors if no input is entered
            emailaddress = request.POST.get('emailaddress', '')  # Using the POST.get method to avoid
            # errors if no input is entered
            try:  # This try catch wont allow wrong email addresses to be stored in the database
                validate_email(emailaddress)
            except ValidationError:
                print ('Sorry wrong email format')
            else:
                pass
            save_object = AddDetails(username=username, emailaddress=emailaddress)  # Getting the data from the form
            # into the Model which moves it to the DB
            save_object.save()  # Save data into the database

            return HttpResponseRedirect(reverse('HRapp:adddetails'))  # Redirect after post
    else:
        form = AddDetailsForm()  # An unbound form

    return render(request, 'adddetails.html', {'form': form, })


def listcontent(request):
    form = AddDetailsForm()
    contents = AddDetails.objects.all()
    return render(request, 'lists.html', {'form': form, 'contents': contents})


class Details(APIView):

    def get(self, request):
        users = AddDetails.objects.all()
        serializer = AddDetailsSerializer(users, many=True)
        return Response(serializer.data)

