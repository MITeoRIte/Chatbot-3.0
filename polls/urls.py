from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('picture', views.picture, name='picture'),
    path('chatting', views.chatting, name='Chatting!'),
    path('chatting2', views.chatting2, name='Chatting2!'),
    path('send/', views.send_message),
    path('sendtochatterbot/',views.send_replyfromChatterbot),
    path('chatting3', views.chatting3, name='Chatting3'),
    path('thinkinggif',views.thinkinggif),
    path('sendamail/', views.sendamail)
    # path('base', views.base, name ='base')
]
