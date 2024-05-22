
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import PdfConverterModel
from utliti.pdf_converter import pdf_to_word,convert_url
from .serializers import PdfConverterSerializers
class ConverterPdf(APIView):

    def post(self,request):

        pdf=request.data.get("pdf")

        PdfConverterModel.objects.create(pdf=pdf)
        object=PdfConverterModel.objects.last()
        path_file=(convert_url(file_path=object.pdf.url,directory_path=str(settings.MEDIA_ROOT)))
        word_name=pdf_to_word(pdf_path=path_file,output_dir=(str(settings.MEDIA_ROOT)+ "/media/word/"))
        object.word=f"media/word/{word_name}"
        object.save()
        serializer=PdfConverterSerializers(object)
        return Response(data=serializer.data)