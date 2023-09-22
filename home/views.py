from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples=[
        {'name': 'Abhijeet Gupta', 'Age': 26},
        {'name': 'Rohan Sharma', 'Age': 23},
        {'name': 'Vicki Singh', 'Age': 17},
        {'name': 'Radha Rani', 'Age': 16},
        {'name': 'Sandeep Verma', 'Age': 63}
    ]

    text = """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aperiam, eveniet magnam.
        """
    return render(request , "home/index.html" , context = {'page': 'Django 2023 tuturial', 'peoples':peoples, 'text':text} ) 

def about(request):
   context = {'page':'about'}
   return render(request , "home/about.html" , context ) 

def contact(request):
   context = {'page':'contact'}
   return render(request , "home/contact.html" , context) 

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey this is a Success page </h1>")
