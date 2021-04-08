from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Questions

# Create your views here.

def home(request):
    latest_q_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest': latest_q_list}
    return render(request, 'letters/home.html', context)

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'letters/detail.html', {'question': question})

def result(request, question_id):
    return HttpResponse('Result for Question %s is ' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote count for Question %s: ' % question_id)
    