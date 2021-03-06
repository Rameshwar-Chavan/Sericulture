from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from smis.models import farmer_registration, form2, form3, form4
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, validators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import unauthorized_user, allowed_users
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['Officer', 'Manager'])
def index(request):
    registration_fetch = farmer_registration.objects.all()
    if request.method == "POST":
        farmer_search = request.POST['search']
        if farmer_search:
            match = farmer_registration.objects.filter(pk=farmer_search)
            return render(request, 'index.html', {'data': match})

        else:
            return HttpResponseRedirect('index')
    else:
        return render(request, 'index.html', {'farmers': registration_fetch})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Officer'])
def registration(request):
    if request.method == "POST":
        fid = form4.objects.filter(farmer_id=request.POST.get(
            'phone')).values_list('id', flat=True)
        if not fid and request.POST.get('farmer_name') and request.POST.get('address') and request.POST.get('gender') and request.POST.get('religion') and request.POST.get('caste') and request.POST.get('state') and request.POST.get('district') and request.POST.get('taluka') and request.POST.get('village') and request.POST.get('pincode') and request.POST.get('phone') and request.POST.get('registration_no') and request.POST.get('year') and request.POST.get('receipt_no') and request.POST.get('area') and request.POST.get('survey_no') and request.POST.get('plant_caste'):
            insert = farmer_registration()
            insert.farmer_name = request.POST.get('farmer_name')
            insert.address = request.POST.get('address')
            insert.gender = request.POST.get('gender')
            insert.religion = request.POST.get('religion')
            insert.caste = request.POST.get('caste')
            insert.state = request.POST.get('state')
            insert.district = request.POST.get('district')
            insert.taluka = request.POST.get('taluka')
            insert.village = request.POST.get('village')
            insert.pincode = request.POST.get('pincode')
            insert.mobile = request.POST.get('phone')
            insert.registration_no = request.POST.get('registration_no')
            insert.year = request.POST.get('year')
            insert.receipt_no = request.POST.get('receipt_no')
            insert.area = request.POST.get('area')
            insert.survey_no = request.POST.get('survey_no')
            insert.plant_caste = request.POST.get('plant_caste')
            insert.save()
            messages.success(
                request, 'Farmer Registration Successfully Completed! ')
            return render(request, 'registration.html')
        else:
            messages.error(request, 'Farmer is already registerd !')
            return render(request, './registration.html')

    return render(request, './registration.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Officer'])
def Form2(request):
    results = farmer_registration.objects.all()
    if request.method == "POST":
        fid = form4.objects.filter(farmer_id=request.POST.get(
            'Reg_no')).values_list('id', flat=True)
        if not fid and request.POST.get('ग्रेनेजचे_नाव') and request.POST.get('अंडीपुंजपावती_क्रमांक') and request.POST.get('दिनांक') and request.POST.get('अंडीपुंज_जात') and request.POST.get('अंडीपुंज_संख्या') and request.POST.get('चॉकी_सेंटरचे_नाव') and request.POST.get('हॅचिंग_तारीख') and request.POST.get('Reg_no'):
            insert = form2()
            insert.Grenege_name = request.POST.get('ग्रेनेजचे_नाव')
            insert.Andipunjpavati_no = request.POST.get(
                'अंडीपुंजपावती_क्रमांक')
            insert.date = request.POST.get('दिनांक')
            insert.Andipunj_jaat = request.POST.get('अंडीपुंज_जात')
            insert.Andipunj_count = request.POST.get('अंडीपुंज_संख्या')
            insert.center_name = request.POST.get('चॉकी_सेंटरचे_नाव')
            insert.hatching_date = request.POST.get('हॅचिंग_तारीख')
            insert.farmer_id = request.POST.get('Reg_no')
            insert.save()
            messages.success(
                request, 'Mulberry Distribution Details Saved Successfully ! ')
            return render(request, './Form2.html', {'reg_no': results})
        else:
            messages.error(
                request, 'Mulberry Distribution Details are already present !')
            return render(request, './Form2.html', {'reg_no': results})

    return render(request, './Form2.html', {'reg_no': results})


def get_form1(request, id):

    output_1 = farmer_registration.objects.filter(pk=id).values_list(
        'farmer_name', 'address', 'village', 'taluka', 'district', 'state', 'area', 'year')

    data = {
        'farmer_name': output_1[0][0],
        'address': output_1[0][1],
        'village': output_1[0][2],
        'taluka': output_1[0][3],
        'district': output_1[0][4],
        'state': output_1[0][5],
        'area': output_1[0][6],
        'year': output_1[0][7]
    }
    return JsonResponse(data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Officer', 'Manager'])
def Form3(request):
    results = farmer_registration.objects.all()
    if request.method == "POST":
        fid = form4.objects.filter(farmer_id=request.POST.get(
            'Reg_no')).values_list('id', flat=True)
        if not fid and request.POST.get('कोष_बाजारपेठ_नाव') and request.POST.get('पावती_क्रमांक') and request.POST.get('दिनांक') and request.POST.get('कोषांचे_वजन') and request.POST.get('इतर_कोष') and request.POST.get('दर_प्रति_कि_ग्रॅ') and request.POST.get('Reg_no'):
            obj3 = form3()
            obj3.कोष_बाजारपेठ_नाव = request.POST.get('कोष_बाजारपेठ_नाव')
            obj3.पावती_क्रमांक = request.POST.get('पावती_क्रमांक')
            obj3.दिनांक = request.POST.get('दिनांक')
            obj3.चांगल्या_कोषांचे_वजन_कि_ग्रॅ = request.POST.get('कोषांचे_वजन')
            obj3.इतर_कोष_कि_ग्रॅ = request.POST.get('इतर_कोष')
            obj3.चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ = request.POST.get(
                'दर_प्रति_कि_ग्रॅ')
            obj3.एकुण_कोष_कि_ग्रॅ = int(
                obj3.चांगल्या_कोषांचे_वजन_कि_ग्रॅ) + int(obj3.इतर_कोष_कि_ग्रॅ)
            obj3.एकुण_रक्कम = int(obj3.चांगल्या_कोषांचे_वजन_कि_ग्रॅ) * \
                int(obj3.चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ)
            obj3.farmer_id = request.POST.get('Reg_no')
            obj3.save()
            messages.success(
                request, 'Production Sales Details Saved Successfully ! ')
            return render(request, './Form3.html')
        else:
            messages.error(
                request, 'Production Sales Details already present !')

    return render(request, './Form3.html', {'reg_no': results})


def get_form2(request, id):

    output_2 = form2.objects.filter(farmer=id).values_list(
        'Grenege_name', 'Andipunjpavati_no', 'date', 'Andipunj_jaat', 'Andipunj_count', 'center_name', 'hatching_date')

    data = {
        'Grenege_name': output_2[0][0],
        'Andipunjpavati_no': output_2[0][1],
        'date': output_2[0][2],
        'Andipunj_jaat': output_2[0][3],
        'Andipunj_count': output_2[0][4],
        'center_name': output_2[0][5],
        'hatching_date': output_2[0][6]

    }
    return JsonResponse(data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Officer'])
def Form4(request):
    results = farmer_registration.objects.all()
    context = {'reg_no': results}
    if request.method == "POST":
        fid = form4.objects.filter(farmer_id=request.POST.get(
            'Reg_no')).values_list('id', flat=True)
        if not fid and request.POST.get('अं_पुं_सरासरी_उत्पादन_कि_ग्रॅ') and request.POST.get('अनुदानास_पात्र_कोषांचे_वजन_कि_ग्रॅ') and request.POST.get('देय_अनुदान_रक्कम_रू'):
            obj4 = form4()
            obj4.sarasari_kosh_kg = request.POST.get(
                'अं_पुं_सरासरी_उत्पादन_कि_ग्रॅ')
            obj4.good_kosh_kg = request.POST.get(
                'अनुदानास_पात्र_कोषांचे_वजन_कि_ग्रॅ')
            obj4.good_kosh_rate = request.POST.get('देय_अनुदान_रक्कम_रू')
            obj4.farmer_id = request.POST.get('Reg_no')

            obj4.save()

            messages.success(
                request, 'Subsidy Distrubition Details Saved Successfully ! ')
            return render(request, 'Form4.html', context)

        else:
            messages.error(request, 'Subsidy Distrubition Already Present!')
            return render(request, 'Form4.html', context)

    return render(request, './Form4.html', context)


@login_required(login_url='login')
def get_form4(request, id):
    form_2 = form2.objects.filter(farmer_id=id).values_list('Andipunj_count')
    form_3 = form3.objects.filter(farmer_id=id).values_list(
        'चांगल्या_कोषांचे_वजन_कि_ग्रॅ', 'चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ')
    data = {
        'a_count': form_2[0][0],
        'good_kosh_kg': form_3[0][0],
        'good_kosh_rate': form_3[0][1],
    }
    return JsonResponse(data)

# User Login View


@unauthorized_user
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect User Name or Password')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)

# Logout user View


def user_logout(request):
    logout(request)
    return redirect('login')

# This is function for Delete Farmes Registration

# def delete_data(request, id):
# if request.method == "POST":
#pi = farmer_registration.objects.get(pk=id)
# pi.delete()
# return HttpResponseRedirect('/', {'farmers': pi})
