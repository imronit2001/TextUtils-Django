from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Hello Ronit</h1> <p> Go to Google : <a href="https://www.google.com/">Google</a></p>''')

def about(request):
    return HttpResponse("About Ronit")