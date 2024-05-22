import os

from django.conf import settings
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import PdfConverterModel
from utliti.pdf_converter import pdf_to_word,convert_url
from docx import Document

class ConverterPdf(APIView):

    def post(self,request):

        pdf=request.data.get("pdf")

        pdf_object=PdfConverterModel.objects.create(
            pdf=pdf,
        )

        object=PdfConverterModel.objects.last()
        path_file=(convert_url(file_path=object.pdf.url,directory_path=str(settings.MEDIA_ROOT)))
        word_name=pdf_to_word(pdf_path=path_file,output_dir=(str(settings.MEDIA_ROOT)+ "/media/word/"))
        pdf_object.word=f"media/word/{word_name}"
        pdf_object.save()
        return Response(
            data="pdf"
        )