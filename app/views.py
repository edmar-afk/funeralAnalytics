from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'forms.html')



def chart(request):
    return render(request, 'charts.html')