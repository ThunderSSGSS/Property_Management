from django.conf.urls import url
from django.urls import path, include
from proprietary import views

urlpatterns=[
	path('owner',views.OwnerList.as_view(),name='owner_list'),
	path('owner/<uuid:pk>',views.OwnerDetail.as_view(),name='owner_detail')
]