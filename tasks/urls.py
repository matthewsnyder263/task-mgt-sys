from django.urls import path
from tasks.views import create_task, show_my_tasks

urlpatterns = [
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
