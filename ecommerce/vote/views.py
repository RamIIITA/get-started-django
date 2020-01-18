from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name='vote/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name= 'vote/detail.html'

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'vote/detail.html', {'question':question})


class ResultsView(generic.DetailView):
    model =Question
    template_name='vote/results.html'


#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'vote/results.html', {'question':question})

def voting(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNot.Exist):
        content = { 'question': question, 'error_message': 'You didn\'t select a choice '}
        return render(request, 'vote/detail.html', content)
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('vote:results', args=(question.id,)))