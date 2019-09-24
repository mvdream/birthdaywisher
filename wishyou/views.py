from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from .forms import PeopleForm
from django.core.mail import send_mail
from django.conf import settings
class Home(View):
    def get(self,request):
        data = {'name':'Mayur'}
        return render(request,'wishyou/index.html',context=data)
    
class PeopleView(FormView):
    template_name = 'wishyou/form.html'
    form_class = PeopleForm
    success_url = reverse_lazy("wishyou:home")
    def form_valid(self, form):
        return super().form_valid(form)

class AddPeople(View):
    def post(self,request):
        pass
class SendMail(View):
    def get(self,request):
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mvdream02@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
        return redirect(reverse_lazy("wishyou:home"))