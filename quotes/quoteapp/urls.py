from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    # path('', views.main, name='main'),
    # path('author/<str:author>', views.author, name='author'),
    # path('add/author', views.AddAuthorView.as_view(), name='add_author'),
    # # path('quote/', views.quote, name='quote'),
    # path('tag/', views.tag, name='tag'),
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('author/<str:author>', views.author, name='author'),
    path('tag/<str:tag>', views.tag, name='tag'),
    path('tag/<str:tag>/<int:page>', views.tag, name='tag_paginate'),
    path('add/author', views.AddAuthorView.as_view(), name='add_author'),
    path('add/tag', views.AddTagView.as_view(), name='add_tag'),
    path('add/quote', views.add_quote, name='add_quote'),
]
