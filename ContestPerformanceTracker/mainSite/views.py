from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from account.models import  Account
import requests



# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'home.html')


@login_required(login_url='login')
def profile(request):

    #codeforces 
    codeforcesid=request.user.account.codeforcesid

    URL = ' https://codeforces.com/api/user.info?'
    PARAMS = {'handles':codeforcesid} 
    codeforces = requests.get(url = URL, params = PARAMS) 
    j=codeforces.json()
    print(j)
    photo= j['result'][0]['titlePhoto']
    handelname=j['result'][0]['handle']
    ratings= j['result'][0]['maxRating']
    currentratings=j['result'][0]['rating']
    maxrank=j['result'][0]['maxRank']
    currentrank=j['result'][0]['rank']

    # uva count 
    '''
    uvaid=request.user.account.uvaid
    URL1='https://uhunt.onlinejudge.org/api/uname2uid/'+''+ uvaid
    PARAMS1=uvaid
    uva= requests.get(url = URL1,params=PARAMS1) 
    x=uva.json()
    URL2='https://uhunt.onlinejudge.org/api/ranklist/'+''+str(x)+'/0'+'/0'
    rank= requests.get(url = URL2) 
    k=rank.json()
    mainrank=k[0]['rank']
    
    '''
    


    context={'handlename':handelname,'ratings':ratings,'currentratings':currentratings,'maxrank':maxrank,'currentrank':currentrank,'photo':photo}

    return render(request,'profile.html',context)

@login_required(login_url='login')
def upcomingcontest(request):
    URL = ' https://codeforces.com/api/contest.list?'
    PARAMS = {'gym':True} 
    #r = requests.get(url = URL, params = PARAMS) 
    #j=r.json()
    #print(j)
    return render(request,'contest.html')