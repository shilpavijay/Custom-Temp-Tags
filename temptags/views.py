from django.shortcuts import render

# Create your views here.
def sampleTemptag(request):
    context = {
        "name": "My name is Agnes.000123",
        "id": "89752358-1234",
        "fullname": "Agnes George Sequera"}
    return render(request,'main.html',context)    