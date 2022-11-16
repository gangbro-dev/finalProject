from django.urls import path, include


urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls'))
]