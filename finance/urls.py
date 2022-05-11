from django.conf.urls import url
from django.urls import path, include
from finance import views

urlpatterns=[
	path('valuetion',views.ValuetionList.as_view(),name='valuetion_list'),
	path('valuetion/<uuid:pk>',views.ValuetionDetail.as_view(),name='valuetion_detail')
]