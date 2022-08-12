from django.urls import path, include
from .views import todo_list, todo_detail, todo_create, todo_update, todo_delete

urlpatterns = [
    path('', todo_list),
    path('todo_create/', todo_create),
    path('<id>/todo_update/', todo_update),
    path('<id>/todo_delete/', todo_delete),
    path('<id>/', todo_detail),
]