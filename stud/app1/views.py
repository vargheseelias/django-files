from django.shortcuts import render
from app1.models import Students
# Create your views here.
def gethome(request):
    return render(request, "app1/home.html")

def getregister(request):
    return render(request, "app1/register.html")

def insertvalues(request):
    na=request.POST.get("sname")
    mrk=request.POST.get("mark")
    print(na)
    print(mrk)
    try:
        obj=Students(name=na,mark=mrk)
        obj.save()
    except Exception as e:
        print("errr",e.args)
        msg = e.args
        return render(request, "app1/register.html", {"msg": msg})
    return getview(request)
    return

def getview(request):
    obj = Students.objects.all()
    return render(request, 'app1/view.html', {"object_list": obj})