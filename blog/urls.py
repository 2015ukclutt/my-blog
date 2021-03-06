from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('about/', views.about, name='about'),

    path('cv/', views.cv, name='cv'),

    path('projects/', views.projects, name='projects'),
    path('projects/portfolio/', views.projects_portfolio, name='projects_portfolio'),
    path('projects/epq/', views.projects_epq, name='projects_epq'),

    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft_list, name='post_draft_list'),
    path('blog/post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('blog/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('blog/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('blog/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
