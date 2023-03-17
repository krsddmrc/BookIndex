from django.urls import path,include
from .views import ( 
    home,
    hello_world,
    phraseList, # listeleme
    phraseCreate, # oluşturma
    phraseListCreate,  # listeleme oluşturma beraber
    phraseUpdate,  # çekme(get), değiştirme (put), silme beraber
    phraseDelete, #silme
    )

urlpatterns = [
    path('', home),
    #! function-based views
    path('hello/', hello_world),
    path('phraseList/', phraseList), # listeleme
    path('phraseCreate/', phraseCreate),# oluşturma
    path('phraseListCreate/', phraseListCreate),# listeleme oluşturma beraber
    path('phraseUpdate/<int:pk>/', phraseUpdate),# çekme(get), değiştirme (put), silme beraber
    path('phraseDelete/<int:pk>/', phraseDelete),#silme
]
