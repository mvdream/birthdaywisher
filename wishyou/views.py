from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, CreateView

from wishyou.models import People
from .forms import PeopleForm
from django.core.mail import send_mail
from django.conf import settings


class Home(View):
    def get(self, request):
        data = {'name': 'Mayur'}
        return render(request, 'wishyou/index.html', context=data)


class PeopleView(View):
    # template_name = 'wishyou/form.html'
    # model = People
    # form_class = PeopleForm
    # success_url = reverse_lazy("wishyou:home")
    def get(self, request):
        form = PeopleForm
        return render(request, 'wishyou/form.html', {'form': form})

    def post(self, request, **kwargs):
        import code; code.interact(local=dict(globals(), **locals()))
        return HttpResponse("Hi")

class AddPeople(View):
    def post(self, request):
        pass


class SendMail(View):
    def get(self, request):
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mvdream02@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return redirect(reverse_lazy("wishyou:home"))
