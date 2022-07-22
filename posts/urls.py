from django.urls import path, resolvers  #A!

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('delete/<int:post_id>/',views.delete, name ='delete'),
    path('edit/<int:post_id>/',views.edit, name ='edit'),#A!
    path('like/<int:post_id>/',views.LikeView, name ='like_post'), #A!

]