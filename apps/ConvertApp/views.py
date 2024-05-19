from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from aspose.pdf import Document,DocSaveOptions

class ConverterPdf(APIView):

    def get(self,request):


        return Response(
            data="test"
        )