# Diabetes Website
This website is a one stop solution for Diabetes. It provides 3 main features =>

* It has a machine learning model integrated with it which helps to predict whether one suffers from diabetes or not. It has a form which takes as input various health condition of the user and predicts the result on the basis of the information given. Various models were made and at the end, RandomForest Classifier with best parameters was selected. It provided an accuracy of 90.9%. The data was taken from Kaggle which was uploaded by UCI Machine Learning.
* It has a facility to get information about the doctors in the given city. It uses web scraping to do so. The data is scraped from [Practo](https://www.practo.com/). It has a form which takes as input the city. A list of names and locality of practice is then displayed. If inforamtion about a city is not available then appropriate message is displayed.
* It also displays the facts and symptoms of Diabates. The data is taken from a verified source of [WHO](https://www.who.int/).

## Built With
* [Django](https://www.djangoproject.com/) - The Web Framework used for backend
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - The Library used for Web Scraping
* [Scikit Learn](https://scikit-learn.org/) - The Library used for building the model
* [Pandas](https://pandas.pydata.org/) - The Library used for handling data

## Installation
* After cloning or downloading this github repo on the local system. 
* Create a Virual Environment on the Desktop.
```bash
~/desktop/virtualenv VirtualEnvironmentName
```
* Now copy the repository inside your virtual environment.
* Activate the virtual environment.
```bash
~/desktop/VirtualEnvironmentName/Scripts/activate
```
* Move inside the virtual environment.
```bash
~/desktop/cd VirtualEnvironmentName
```
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
```bash
pip install -r requirements.txt
```
* Change directory to Diabetes
```bash
~/desktop/VirtualEnvironmentName/Diabetes
```
* Run the following command
```bash
python manage.py runserver
```
An IP address will be shown, copy it and run it on a web browser.

## Using the app
Internet connection is a must to run the app.

The app is now live at localhost.

## Screenshots
* Home Page
![homepage](https://github.com/faiz-hasan11/HeartDiseasePredictionWebsite/blob/master/Screenshots/HomePage.png)
* Prediction Page
![Have Diease](https://github.com/faiz-hasan11/HeartDiseasePredictionWebsite/blob/master/Screenshots/HaveDisease.png)
![Dont Have Diease](https://github.com/faiz-hasan11/HeartDiseasePredictionWebsite/blob/master/Screenshots/DontHaveDisease.png)


