from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from lots.views import LotListView, LotCreateView, UserProfileTemplateView, LotDetailView

urlpatterns = [
    path('', LotListView.as_view(), name='home'),
    path('add_lot/', LotCreateView.as_view(), name='lot_create'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lot/<int:pk>', LotDetailView.as_view(), name='lot_detail'),
    path('profile/', UserProfileTemplateView.as_view(), name='profile'),
]
