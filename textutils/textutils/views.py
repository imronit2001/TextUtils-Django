from django.http import HttpResponse

def index(request):
    return HttpResponse('''Hello Ronit''')

def about(request):
    return HttpResponse("About Ronit")