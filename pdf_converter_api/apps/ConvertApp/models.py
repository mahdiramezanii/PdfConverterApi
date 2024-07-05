from django.db import models

class PdfConverterModel(models.Model):

    pdf=models.FileField(upload_to="media/pdf/")
    word=models.FileField(upload_to="media/word/",null=True,blank=True)




