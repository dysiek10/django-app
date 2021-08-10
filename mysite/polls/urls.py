from django.urls import path

from . import views

<<<<<<< HEAD
app_name = 'polls'
=======
>>>>>>> 594c981aaeaa34f90cd490c4394176766ef1591e
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]