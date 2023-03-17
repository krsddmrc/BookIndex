from django.urls import path
from .views import home,phrase_api, phrase_api_get_update_delete
urlpatterns = [
 path('', home),
 path('phrase/', phrase_api),
 path('phrase/<int:pk>/', phrase_api_get_update_delete, name = "detail")
]
