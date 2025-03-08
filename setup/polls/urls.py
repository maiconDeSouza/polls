from django.urls import path

from setup.polls import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/detail/', views.PollDetail.as_view(), name='poll_detail'),
    path('detail/error', views.PollDetailError.as_view(),
         name='poll_detail_error'),
    path('<int:pk>/votes/', views.PollVotes.as_view(), name='poll_votes'),
    path('newpoll/', views.NewPoll.as_view(), name='newpoll'),
]
