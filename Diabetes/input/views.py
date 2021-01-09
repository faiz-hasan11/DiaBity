from django.shortcuts import render
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from bs4 import BeautifulSoup
import requests
# Create your views here.

reloadModel = joblib.load('./models/ModelDiabetes.pkl')

def home(request):
    return render(request,'home.html')

def input(request):
    return render(request,'input.html')

def more(request):
    return render(request,'more.html')

def consult(request):
    return render(request,'consult.html')

def symptoms(request):
    return render(request,'symptoms.html')

def predictResult(request):
    if request.method == 'POST':
        temp={}
        arr = []
        temp['preg'] = request.POST.get('pregVal')
        temp['plasma'] = request.POST.get('plasmaVal')
        temp['bp'] = request.POST.get('bpVal')
        temp['skin'] = request.POST.get('skinVal')
        temp['insulin'] = request.POST.get('insulinVal')
        temp['bmi'] = request.POST.get('bmiVal')
        temp['pedigree'] = request.POST.get('pedigreeVal')
        temp['age'] = request.POST.get('ageVal')
        arr.append(float(temp['preg']))
        arr.append(float(temp['plasma']))
        arr.append(float(temp['bp']))
        arr.append(float(temp['skin']))
        arr.append(float(temp['insulin']))
        arr.append(float(temp['bmi']))
        arr.append(float(temp['pedigree']))
        arr.append(float(temp['age']))
        scoreval = reloadModel.predict([arr])
        return render(request,'pred.html',{'scoreval':scoreval})

def DocDetail(request):
    print("HELLO")
    if request.method == 'POST':
        temp={}
        temp['city'] = request.POST.get('city')
        city = temp['city']
        print(city)
        error = False
        data = []
        print('here')
        try:
            url = 'https://www.practo.com/'+city+'/endocrinologist'
            print(url)
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text,'lxml')
            names = soup.find_all('h2',class_='doctor-name')
            print(names)
            places = soup.find_all('div',class_='u-bold u-d-inlineblock u-valign--middle')
            print(places)
            for i in range(len(names)):
                val = {'name':names[i].text,'place':places[i].text}
                data.append(val)
        except:
            error = True
        return render(request,'docdisplay.html',{'data':data})
