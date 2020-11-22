from django.urls import path
from post.views import index, NewPost, PostDetails, like


urlpatterns = [
   	path('', index, name='index'),
   	path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike')
]