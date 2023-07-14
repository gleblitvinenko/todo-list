from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View, generic

from list.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TakDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:index")


class TaskUpdateDoneView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        # Update the 'done' field
        task.done = not task.done
        task.save()

        return HttpResponseRedirect(reverse("list:index"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")