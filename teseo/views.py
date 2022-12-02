
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def account(request):
    return render(request, 'registration/account.html', {
        'account': User.objects.get(id=request.user.id) 
    })