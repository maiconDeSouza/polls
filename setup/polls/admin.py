from django.contrib import admin
from setup.polls.models import Poll, Choice, VotedPoll

# Register your models here.


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'poll',)
    search_fields = ('choice_text', 'poll',)


@admin.register(VotedPoll)
class VotedPollAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll',)
    search_fields = ('user', 'poll',)
