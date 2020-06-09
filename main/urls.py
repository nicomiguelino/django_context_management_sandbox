from django.urls import path
from main.views import IndexView, BuiltinsView, CustomView

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('builtins/', BuiltinsView.as_view(), name='builtins'),
    path('custom/', CustomView.as_view(), name='custom')
]
