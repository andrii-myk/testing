from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic import ListView

from .models import Test, Question
from .forms import QuestionForm

# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        tests = Test.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        tests = Test.objects.all()
    

    return render(request, 'testing/index.html', context={'tests': tests})

# def questions(request):
#     questions_list = Question.objects.all()
#     return render(request, 'testing/questions.html', context={'questions': questions_list})

# def test_detail(request, slug):
#     test = Test.objects.get(slug__iexact=slug)
#     return render(request, 'testing/test_detail.html', context={'test': test})

class TestDetail(ListView):
    def get(self, request, slug):
        test = get_object_or_404(Test, slug__iexact=slug)
        return render(request, 'testing/test_detail.html', context={'test': test})

class QuestionsView(ListView):
    def get(self, request):
        questions = Question.objects.all()
        return render(request, 'testing/questions.html', context={'questions': questions})


class QuestionCreate(ListView):
    def get(self, request):
        form = QuestionForm()
        return render(request, 'testing/question_create.html', context={'form': form})

    def post(self, request):
        bound_form = QuestionForm(request.POST)
        if bound_form.is_valid:
            new_question = bound_form.save()
            return redirect(reverse('testing:questions_url'))
        return render(request, 'testing/question_create.html', context={'form': bound_form})

class QuestionUpdate(ListView):
    def get(self, request, id):
        question = Question.objects.get(id__exact = id)
        bound_form = QuestionForm(instance=question)
        return render(request, 'testing/question_update.html', context={'form': bound_form, 'question': question,})

    def post(self, request, id):
        question = Question.objects.get(id__exact = id)
        bound_form = QuestionForm(request.POST, instance=question)

        if bound_form.is_valid():
            updated_question = bound_form.save()
            return redirect(reverse('testing:questions_url'))
        return render(request, 'testing/question_update.html', context={'form': bound_form, 'question': question})


class QuestionDelete(ListView):
    def get(self, request, id):
        question = Question.objects.get(id__exact = id)
        return render(request, 'testing/question_delete.html', context={'question': question})

    def post(self, request, id):
        question = Question.objects.get(id__exact = id)
        question.delete()
        return redirect(reverse('testing:questions_url'))