from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth import views #搭配登入、登出
# 構建應用程序時，添加模式的地方

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), # Added for challenge
    
    # path('account/logout/', views.LogoutView.as_view()),
    # path(r'^accounts/logout/$',auth_views.logout,name='logout'),
    # 首頁點選登出無法導向logged_out.html，因為被設定過在首頁旁登入、出還是會在首頁


    # 第六章
    # path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]

# 第九章驗證
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# 第九章
#加入Authors資料表的list清單網頁的url mapping
urlpatterns += [  
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# 導向首頁的意思，會跟html檔做連結去導入到首頁
# BookListView.as_view() 此函式是將names參數導入到該頁(若books是參數，將會導到books那頁)
# pk 為主鍵 參數為書本ID（必須為整數）