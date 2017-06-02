from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404

# Create your views here.
from .models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    latest_question_list = get_list_or_404(
        Question.objects.order_by('-pub_date')[:5]
    )
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)

    # question.choice_set.
    # Choice.objects.filter(question=question)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "youre looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    context={
        'question':question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            messages.add_message(request, messages.ERROR, "You didn't select a choice")
            return redirect('polls:detail')

    else:
        return HttpResponse("You're voting on question %s." % question_id)
