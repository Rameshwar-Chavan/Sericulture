from django.db import models

# Create your models here.


class farmer_registration(models.Model):

    farmer_name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    pincode = models.IntegerField(max_length=7)
    mobile = models.BigIntegerField()
    registration_no = models.IntegerField()
    year = models.DateField(auto_now=False, auto_now_add=False)
    receipt_no = models.IntegerField(max_length=10)
    area = models.CharField(max_length=255)
    survey_no = models.IntegerField(max_length=255)
    plant_caste = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "farmers"

    def __int__(self):
        return self.pk


class form2(models.Model):

    farmer = models.ForeignKey(farmer_registration, on_delete=models.CASCADE)
    Grenege_name = models.CharField(max_length=255)
    Andipunjpavati_no = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    Andipunj_jaat = models.CharField(max_length=255)
    Andipunj_count = models.IntegerField()
    center_name = models.CharField(max_length=255)
    hatching_date = models.DateField(auto_now=False, auto_now_add=False)

    def __int__(self):
        return self.pk


class form3(models.Model):

    farmer = models.ForeignKey(
        farmer_registration, on_delete=models.CASCADE, default=None)
    कोष_बाजारपेठ_नाव = models.CharField(max_length=255)
    पावती_क्रमांक = models.IntegerField()
    दिनांक = models.DateField(auto_now=False, auto_now_add=False)
    चांगल्या_कोषांचे_वजन_कि_ग्रॅ = models.BigIntegerField()
    इतर_कोष_कि_ग्रॅ = models.FloatField()
    चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ = models.FloatField()
    एकुण_कोष_कि_ग्रॅ = models.FloatField()
    एकुण_रक्कम = models.FloatField()

    def __str__(self):
        return self.farmer


class form4(models.Model):

    farmer = models.ForeignKey(farmer_registration, on_delete=models.CASCADE)
    चांगल्या_कोषांचे_वजन_कि_ग्रॅ = models.ForeignKey(
        form3, on_delete=models.CASCADE)

    Andipunj_count = models.ForeignKey(form2, on_delete=models.CASCADE)
    चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ = models.DecimalField(
        decimal_places=3, max_digits=10)

    अं_पुं_सरासरी_उत्पादन_कि_ग्रॅ = models.DecimalField(
        decimal_places=3, max_digits=10)
    अनुदानास_पात्र_कोषांचे_वजन_कि_ग्रॅ = models.DecimalField(
        decimal_places=3, max_digits=10)
    देय_अनुदान_रक्कम_रू = models.DecimalField(decimal_places=3, max_digits=10)

    def __int__(self):
        return self.pk