from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View


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

        return redirect('poll_votes', pk=pk)


class PollVotes(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = get_list_or_404(Choice, poll=pk)
        total_votes = poll.total_votes()

        choices_with_percentage = [
            {'choice_text': choice.choice_text, 'percentage': f'{((choice.votes / total_votes) * 100 if total_votes > 0 else 0):.2f}%'}
            for choice in choices
        ]

        context = {
            'poll': poll,
            'choices': choices_with_percentage
        }
        return render(request, 'polls/pages/poll_votes.html', context)
