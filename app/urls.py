from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='index'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('cause/', views.causes, name='cause'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('event/', views.EventListView.as_view(), name='event'),
    path('contact/', views.contact, name='contact'),
    path('cause/detail/<slug:slug>/', views.cause_detail, name='cause-detail'),
    path('blog/<category>/', views.blog_category, name='blog_category'),
    path('program/', views.program, name='abana'),
    path('program/<category>/', views.filter_abana, name='filter_abana'),
    path('comment/create/<str:post_slug>', views.create_comment, name='create_comment'),
    path('program_detail/<slug:slug>/', views.program_detail, name='program_detail'),
]

admin.site.site_header = 'Enfants Mere Admin Adminsitration'                    # default: "Django Administration"
admin.site.index_title = 'Website Features'                 # default: "Site administration"
admin.site.site_title = 'Enfants Mere adminsitration' # default: "Django site admin"
