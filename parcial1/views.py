from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home</h1><p>Bienvenido a la pagina principal.</p>")


def about(request):
    return HttpResponse("<h1>About</h1><p>Esta es la pagina About.</p>")