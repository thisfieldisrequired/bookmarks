from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import user_login, dashboard


urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', PasswordChangeDoneView.as_view(), 'password_change_done'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)