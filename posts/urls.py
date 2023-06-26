from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('posts/create', views.create_post, name='create_post'),
    path('posts/store', views.save_post, name='store_post'),
    #path('posts/create_coupling', views.create_new, name='create_coupling'),
    path('posts/<int:id>/details', views.get_post, name='post_details'),
    path('posts/<int:id>/edit', views.post_edit, name='edit_post'),
    path('posts/<int:id>/update', views.post_update, name='update_post'),
    path('posts/<int:id>/status-change', views.publish_switch, name='status_switch'),
    path('posts/<int:id>/delete', views.post_delete, name='delete_post')
]
