from rest_framework import serializers


class PdfConverterSerializers(serializers.Serializer):
    pdf=serializers.FileField()
    word=serializers.FileField()