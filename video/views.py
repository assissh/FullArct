# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create video Here

class videoCreateView(LoginRequiredMixin, CreateView):
    model = models.video
    template_name = 'video/video_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['my_image','owned_by']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.video_Author = self.request.user
        return super().form_valid(form)

# video Details Here


class videoDetailView(LoginRequiredMixin, DetailView):
    model = models.video
    template_name = 'video/video_detail.html'
    login_url = 'login'

# video ListView Here


class videoListView(ListView):
    model = models.video
    template_name = 'video/video_list.html'
    login_url = 'login'

# video Update Here


class videoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.video

    # Decide fields for editing Here

    fields = ['owned_by','my_image']
    template_name = 'video/video_update.html'
    login_url = 'login'

# video Delete here


class videoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.video
    template_name = 'video/video_delete.html'
    success_url = reverse_lazy('video_list')
    login_url = 'login'





# Create your views here.
