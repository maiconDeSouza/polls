from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views import View


from setup.polls.models import Poll, Choice, VotedPoll


# Create your views here.

class Index(View):
    def get(self, request):
        polls = Poll.objects.all()
        context = {
            'polls': polls
        }
        return render(request, 'polls/pages/index.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class PollDetail(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = get_list_or_404(Choice, poll=poll)
        voted = VotedPoll.objects.filter(user=request.user, poll=poll).exists()

        if voted:
            return redirect('poll_votes', pk=pk)

        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'polls/pages/poll_detail.html', context)

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()

        VotedPoll.objects.create(user=request.user, poll=poll)

        return redirect('poll_votes', pk=pk)


@method_decorator(login_required(login_url='login'), name='dispatch')
class PollVotes(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        choices = get_list_or_404(Choice, poll=pk)
        total_votes = poll.total_votes()

        choices_with_percentage = sorted(
            [
                {'choice_text': choice.choice_text,
                 'percentage': f'{((choice.votes / total_votes) * 100 if total_votes > 0 else 0):.2f}%'}
                for choice in choices
            ],
            key=lambda x: float(x['percentage'].strip('%')),
            reverse=True  # Ordena do maior para o menor
        )

        context = {
            'poll': poll,
            'choices': choices_with_percentage
        }
        return render(request, 'polls/pages/poll_votes.html', context)


@method_decorator(user_passes_test(lambda user: user.is_staff, login_url='login'), name='dispatch')
class NewPoll(View):
    def get(self, request):
        return render(request, 'polls/pages/new_poll.html')

    def post(self, request):
        question_text = request.POST.get('question_text')

        choices = request.POST.getlist('choices')

        if not question_text or len(choices) < 2:
            return render(request, 'polls/pages/new_poll.html', {'error': 'A enquete deve ter pelo menos duas opções.'})

        poll = Poll.objects.create(
            question_text=question_text, created_by=request.user)

        for choice_text in choices:
            Choice.objects.create(poll=poll, choice_text=choice_text)

        return redirect('poll_detail', pk=poll.pk)
