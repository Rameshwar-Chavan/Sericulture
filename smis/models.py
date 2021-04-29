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

    def __str__(self):
        return self.farmer_name


class form2(models.Model):

    farmer = models.ForeignKey(farmer_registration, on_delete=models.CASCADE)
    Grenege_name = models.CharField(max_length=255)
    Andipunjpavati_no = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    Andipunj_jaat = models.CharField(max_length=255)
    Andipunj_count = models.IntegerField()
    center_name = models.CharField(max_length=255)
    hatching_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.farmer_id


class form3(models.Model):

    farmer = models.ForeignKey(
        farmer_registration, on_delete=models.CASCADE, default=None)
    kosh_bajarpeth_name = models.CharField(max_length=255)
    pavti_no = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    good_kosh_kg = models.BigIntegerField()
    other_kosh_kg = models.FloatField()
    good_kosh_rate_kg = models.FloatField()
    total_kosh_kg = models.FloatField()
    total_kosh_amount = models.FloatField()

    def __str__(self):
        return self.farmer


class form4(models.Model):
    farmer = models.ForeignKey(
        farmer_registration, on_delete=models.CASCADE)
    sarasari_kosh_kg = models.FloatField(default=None)
    good_kosh_kg = models.FloatField(default=None)
    good_kosh_rate = models.FloatField(default=None)

    def __str__(self):
        return self.farmer_id
