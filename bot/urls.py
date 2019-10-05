from django.urls import path

from bot import views as bot_views

app_name = 'bot'

urlpatterns = [
    path('reminders/',
         bot_views.ReminderListCreateAPIView.as_view(), 
         name='api-reminder-create'),
    # path('reminders/<uuid:pk>/', blog_views.PostDetailsAPIView.as_view(), name='api-post-details'),
]