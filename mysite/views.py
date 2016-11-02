from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from river.models import State

from mysite.models import MyModel


def test(request):
    my = MyModel.objects.get(pk=2)
    user = User.objects.get(username=request.user)
    my.proceed(user)
    # my.proceed(user, next_state=State.objects.get(label='start'))
    return render(request, "test.html", {"test1": my})
