
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of video : video_list

    path('', views.videoListView.as_view(), name='video_list'),

    # Path to create new video : video_new

    path('new/', views.videoCreateView.as_view(), name='video_new'),

    # Path to edit video : edit_list

    path('<int:pk>/edit', views.videoUpdateView.as_view(), name='video_edit'),

    # Path to delete video : video_delete

    path('<int:pk>/delete', views.videoDeleteView.as_view(), name='video_delete'),

    # Path to detail view of video : video_details

    path('<int:pk>', views.videoDetailView.as_view(), name='video_details')
]
