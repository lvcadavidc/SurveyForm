from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .forms import Form
# Create your views here.

class FormPage(generic.FormView):
    form_class = Form
    template_name = 'home.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Form submited")
        return super().form_valid(form)

#def home_page():
#    template_name = 'home.html'
#    return render(request, template_name)

