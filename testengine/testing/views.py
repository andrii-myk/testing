from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from .models import Test

# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        tests = Test.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        tests = Test.objects.all()
    

    return render(request, 'testing/index.html', context={'tests': tests})

def test_detail(request, slug):
    test = Test.objects.get(slug__iexact=slug)
    return render(request, 'testing/test_detail.html', context={'test': test})