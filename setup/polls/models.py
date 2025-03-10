from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Poll(models.Model):
    question_text = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def total_votes(self):
        return self.choice.aggregate(total=Sum('votes'))['total'] or 0


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='choice')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.poll.question_text} - {self.choice_text}'


class VotedPollManager(models.Manager):
    def voted(self, user, poll):
        is_voted = self.filter(user=user, poll=poll).exists()

        return is_voted


class VotedPoll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    objects = VotedPollManager()

    def __str__(self):
        return f'{self.user} votou em {self.poll}'
