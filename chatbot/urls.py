from django.urls import path, include

urlpatterns = [
    path('chatbot/', include('apichatbot.urls')),
]
   