from django.urls import path
from .views import ( 
    home,
    #PhraseList, 
    #PhraseDetail,
    #PhraseListCreate,
    #PhraseGetUpdateDelete, #for concreate view
    PhraseMVS
    )
from rest_framework import routers

router=routers.DefaultRouter()
router.register('phrase', PhraseMVS)  #! iki paremetre 1. prefix, 2. Viewset
 
urlpatterns = [
    path('', home),
    #path('list/', PhraseList.as_view()),  # for class_based and generic view
    #path('detail/<int:pk>/', PhraseDetail.as_view()),  # for class_based
    #path ('list/', PhraseListCreate.as_view()), #for concreate view
    #path ('get/<int:id>', PhraseGetUpdateDelete.as_view()), #for concreate view
]
urlpatterns+=router.urls
