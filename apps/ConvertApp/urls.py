from django.urls import  path
from . import  views
app_name="ConvertApp"
urlpatterns=[
    path("",views.ConverterPdf.as_view(),name="convertApp"),
]