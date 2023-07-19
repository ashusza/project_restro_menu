from django.urls import path
from app_restapi.views import MenuApiView,CategoryApiView,CategoryApiIdView

urlpatterns = [
    path('categories/',CategoryApiView.as_view()),
    path('categories/<int:id>/',CategoryApiIdView.as_view()),
    path('menus/',MenuApiView.as_view()),
    
]
