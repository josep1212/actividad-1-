from django.shortcuts import render

def desplegarTemplate(request):
    return render(request, 'templatesApp1/ejemplo1.html')

def desplegarTemplate2(request):
    data = {"nombre" : "CastroncioPocoHuevo"} 
    return render(request, 'templatesApp1/ejemplo1.html',data)


def infoUsuario(request):
    data = {"ID" : "217523658-9","NOMBRE" : "JAYCE","EMAIL" : "jayce.sierra@inacapmail.cl"}
    return render(request, 'templatesApp1/ejemplo2.html',data)