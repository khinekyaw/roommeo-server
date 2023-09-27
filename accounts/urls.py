from django.urls import path

from accounts.views import GoogleLoginView

urlpatterns = [
    path('google/', GoogleLoginView.as_view(), name="google")
]
