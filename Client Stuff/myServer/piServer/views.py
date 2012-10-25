from django.template import Context, loader
from piServer.models import User
from django.http import HttpResponse

def index(request):
    user_list = User.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'user_list': user_list,
    })
    return HttpResponse(t.render(c))