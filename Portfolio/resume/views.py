
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage




def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myApp/Pithani-sowgandhika_resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="Pithani-sowgandhika_resume.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404 )

def certificates(request):
    return render(request,"certificate.html")

def projects(request):
    projects_show=[
        {
            'title':'Multi Disease Prediction System',
            'path':'images/new1.jpeg',
            'description':'It is a ML based platform that utilizes machine learning algorithms to predict the onset of four major diseases: Heart Disease,Diabetes,Parkinsons Disease,and Breast Cancer.Additionally,the system will include data visualizationto explore relationship between variables.'
        },
        {
            'title':'Stock and Crypto Price Prediction',
            'path':'images/NewVisualization.png',
            'description':'The "Stock and Crypto Price Prediction" project develops a system using LSTM networks for forecasting stocks, cryptocurrencies and commodities.Provides real-time data analysis and predictive modeling to aid informed decision-making for investors.'
        },
        {
            'title':'Digital Subjective Assessment System',
            'path':'images/new3.png',
            'description':'The "Subjective Assessment System" project builds a web app using Django and Bootstrap for users to answer questions.It uses BERT,SBERT,WMD, and TF-IDF Cossine-Similarity techniques for similarity measurement to provide similarity scores and store similarity scores in a database.It also allows downloading all results as a CSV file from the admin panel for easy data handling.'

        },
        {
            'title':'',
            'path':''
        },
        {
            'title':'',
            'path':''
        },

    ]
    return render(request,"projects.html",{"projects_show":projects_show})