from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # homepage
    path('books/', views.book_list, name='books'),  # books page
    path('add_book/', views.add_book, name='add_book'),
    path('members/', views.member_list, name='member_list'),
    path('add_member/', views.add_member, name='add_member'),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('return-book/', views.return_book, name='return_book'),
path('return/<int:id>/', views.return_action, name='return_action'),
]