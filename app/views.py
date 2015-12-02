from django.shortcuts import render
import settings 
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def cloud(request):
    content = {
        'project': settings.PROJECT,
        'client_id': settings.CLIENT_ID,
        'api_key': settings.API_KEY,
        'scopes': settings.SCOPES,
        'group': settings.GROUP,

    }
    return render(request, 'app/cloud.html', content)
