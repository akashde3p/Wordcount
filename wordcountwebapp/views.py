from django.http import HttpResponse
from django.shortcuts import render
import operator
# from bs4 import *
# import lxml
# import requests


def  home(request):
    return render(request, 'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    cnt=fulltext.split()
    wordict={}
    for word in cnt:
        if word in wordict:
            wordict[word] += 1
        else:
            wordict[word] = 1
    sortedwords=sorted(wordict.items(),key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'wordcount':len(cnt),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')


# def dnc(request):
#     fulltext=request.Get['fulltext']
#     url = fulltext
#     r = requests.Get(url)
#     soup = BeautifulSoup(r.content,"lxml")
#     new=[]
#     for link in soup.findAll('a'):
#         c = link.get('href')
#         new.append(c)
#     return render(request, 'dnc', {'fulltext':fulltext,'links':new})
