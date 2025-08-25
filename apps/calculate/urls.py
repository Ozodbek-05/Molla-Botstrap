from django.urls import path

from apps.calculate.views import calculate_view

app_name = 'calculator'
urlpatterns = [
    path('calc/',calculate_view, name='calculate')
]