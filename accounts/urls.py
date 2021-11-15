from django.urls import path,include
urlpatterns = [
    path(r'', include('rest_auth.urls')),
    path(r'registration/', include('rest_auth.registration.urls'))
]