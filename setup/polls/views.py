from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from django.http import HttpResponse

from setup.polls.models import Poll, Choice


# Create your views here.

class Index(View):
    def get(self, request):
        polls = Poll.objects.all()
        context = {
            'polls': polls
        }
        return render(request, 'polls/pages/index.html', context)


class PollDetail(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = get_list_or_404(Choice, poll=pk)
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'polls/pages/poll_detail.html', context)

    def post(self, request, pk):
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()

        return HttpResponse(f'{choice_id} - {choice.choice_text} - {choice.votes}')


class PollVotes(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = get_list_or_404(Choice, poll=pk)
        total_votes = poll.total_votes()

        for choice in choices:
            choice_total_votes = choice.votes
            porcentagem = (choice_total_votes / total_votes) * 100
            print(f'{choice.choice_text} - {porcentagem:.2f}%')

        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'polls/pages/poll_detail.html', context)
