from django.views.generic.base import TemplateResponseMixin, View
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

class IndexView(TemplateResponseMixin,View):
    template_name = "career/index.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        template_values = {'form': form}
        return self.render_to_response(template_values)

    def post(self, request,  *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            from_email = form.cleaned_data['from_email']
            text = form.cleaned_data['message']
            message = "Hi, there is a message from :", fname, " ", lname, " ", text
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            template_values = {'success':1,'form':form}
        return self.render_to_response(template_values)