from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import RentalInfoView, BookRentalView
from django.views.generic import TemplateView

app_name = 'books' # 앱 네임스페이스 지정 (프로젝트 내에서 이름이 겹치지 않도록 하기 위함)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'), # books/로 접속하면 이 뷰함수가 실행되도록 구성
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'), 
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('rental-info/', RentalInfoView.as_view(), name='rental_info'),
    path('rental/', BookRentalView.as_view(), name='book_rental'),
    path('rental/success/', TemplateView.as_view(template_name='books/rental_success.html'), name='rental_success'),
]