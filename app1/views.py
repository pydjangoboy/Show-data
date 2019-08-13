from django.shortcuts import render
# Create your views here.

def ShowDetails(request):
    dict = {
        'id': 101,
        'name': 'jai',
        'rollno':159,
        'address':'USA',
        'mob_no':123456788
    }
    return render(request,'index.html',dict)
