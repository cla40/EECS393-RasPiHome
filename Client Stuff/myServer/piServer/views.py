from django.template import Context, loader
from piServer.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user_list = UserProfile.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'user_list': user_list,
    })
    return HttpResponse(t.render(c))