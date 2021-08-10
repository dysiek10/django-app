from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.shortcuts import render, get_object_or_404

# viewsy służą do wyciągania konkretnych danych do konkretnego endpointa i formatowaniu ich


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'if_test': "success",
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = f"You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    print("POST: ", request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("Choice nr: ", request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print("var - selected_choice: ", selected_choice)
        print("var - selected_choice votes: ", selected_choice.votes)
        selected_choice.votes += 1
        selected_choice.save()
        print("var - selected_choice votes - after: ", selected_choice.votes)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))