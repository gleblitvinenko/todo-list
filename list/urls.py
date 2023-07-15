from django.urls import path

from list.views import (
    IndexView,
    TaskCreateView,
    TaskUpdateView,
    TakDeleteView,
    TaskUpdateDoneView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

app_name = "list"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("task-create/", TaskCreateView.as_view(), name="create-task"),
    path("task-update/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
    path("task-delete/<int:pk>/", TakDeleteView.as_view(), name="delete-task"),
    path("task-update-done/<int:pk>/", TaskUpdateDoneView.as_view(), name="update-task-done"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
