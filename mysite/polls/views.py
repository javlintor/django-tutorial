from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    latest_question_list = latest_question_list[:10]
    context = {
        "latest_question_list": latest_question_list
    }
    response = render(request, "polls/index.html", context)
    return response


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {
        "question": q
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    response = "Your are looking at results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "Your are voting on question %s"
    return HttpResponse(response % question_id)
