from django.conf.urls import url
from django.urls import path, include
from property import views

urlpatterns=[
	path('type/',views.TypeList.as_view(),name='type_list'),
	path('type/<uuid:pk>',views.TypeDetail.as_view(),name='type_detail'),
	path('patrimony/',views.PatrimonyList.as_view(),name='patrimony_list'),
	path('patrimony/<uuid:pk>',views.PatrimonyDetail.as_view(),name='patrimony_detail'),
	path('image/',views.ImageList.as_view(),name='image_list'),
	path('image/<uuid:pk>',views.ImageDetail.as_view(),name='image_detail')
]