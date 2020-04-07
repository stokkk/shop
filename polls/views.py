from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice

#dop
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.



def index(request, search_params=None):
	if search_params is not None:
		latest_question_list = Question.objects.filter(question_text__icontains=search_params)
	else:
		latest_question_list = Question.objects.all()	
	return render(request, 'polls/index.html', {'latest_question_list' : latest_question_list})

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	return HttpResponse("You're looking at the results")

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))