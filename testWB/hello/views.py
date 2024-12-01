from django.http import HttpResponse
   
def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request, name, age):
    return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")