from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path('<int:book_id>/', views.detail, name='detail'),  # Named pattern for the detail page
    path('feedback/', views.getFeedback, name='feedback'),  # Added path for feedback
    path('findbooks/', views.findbooks, name='findbooks'),  # Added path for findbooks
    path('place_order/', views.place_order, name='place_order'),
    ]
