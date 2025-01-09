from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return render(request, 'second_task/index.html')

def fbv(request):
    return render(request, 'second_task/func_template.html')


class CBV(TemplateView):
    template_name = 'second_task/class_template.html'
