from django.shortcuts import render

def getIndex(request):
  return render(request,'index.html')

def getForm(request):
  return render(request,'input.html')