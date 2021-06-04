from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Service

def home(request):
    return render(request, 'app/home.html')
def about(request):
    return render(request, 'app/about.html')
def serviceburenie(request):
    return render(request, 'app/service-burenie.html')
def servicesverlenie(request):
    return render(request, 'app/service-sverlenie.html')
def contact(request):
    return render(request, 'app/contact.html')
def ourwork(request):
    return render(request, 'app/ourwork.html') 
class SearchResultsView(ListView):
    model = Service
    template_name = 'app/search.html'

    def get_queryset(self):
        query = (self.request.GET.get('q')).lower()
        object_list = Service.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list

    # def get_queryset(self):
    #     return Service.objects.filter(
    #         name__icontains='е'
    #     ) .exclude(
    #         name__icontains='Бурение'
    #     )
    # def get_queryset(self):
    #     return Service.objects.filter(
    #         Q(name__icontains='Бурение') | Q(description__icontains='разных форм')
    #     )

