from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# from django.template import loader

# Create your views here.
class IndexView (generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'
  def get_queryset (self):
    return Question.objects.order_by('-pub_date')[:5]
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # context = {
  #   'latest_question_list': latest_question_list,
  # }
  # return render(request, 'polls/index.html', context)

class DetailView (generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'
  # try:
  #   question = Question.objects.get(pk = question_id)
  #   context = {
  #     'question': question
  #   }
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  # question = get_object_or_404(Question, pk = question_id)
  # context = {
  #   'question': question
  # }
  # return render(request, 'polls/detail.html', context)

class ResultsView (generic.DetailView):
  model = Question
  template_name = 'polls/results.html'
  # question = get_object_or_404(Question, pk = question_id)
  # context = {
  #   'question': question
  # }
  # return render(request, 'polls/results.html', context)
  # response = "You're looking at the results of question %s."
  # return HttpResponse(response % question_id)

def vote (request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
  # return HttpResponse("You're voting on question %s." % question_id)
