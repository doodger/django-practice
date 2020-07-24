from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail')
	##Other stuff done during tutorial
	#path('', views.index, name='index'),
	#exemple: /polls/5
	#path('<int:question_id>/', views.detail, name='detail'),
	#exemple /polls/5/results
	#path('<int:question_id>/results/', views.results, name='results'),
	#exemple /polls/5/vote
	#path('<int:question_id>/vote/', views.vote, name='vote'),

]