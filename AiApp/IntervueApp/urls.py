from django.urls import path
from IntervueApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.auth_page, name="auth"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),

    path('index/', views.index, name='index'),
    path('results/', views.result, name='result'),

    path('play_audio/', views.play_audio, name='play_audio'),
    path('process_text/', views.process_text, name='process_text'),
    path('upload/', views.upload, name='upload')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)