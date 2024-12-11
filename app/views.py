from django.shortcuts import render

# Create your views here.

d={'a':10,'b':20}
def jinjaprint(request):
    return render(request,'new.html',context=d)
