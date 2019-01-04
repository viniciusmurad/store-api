from django.urls import path
from stores.views import StoreList, StoreDetail

urlpatterns = [
    path('', StoreList.as_view()),
    path('<int:pk>', StoreDetail.as_view())
]