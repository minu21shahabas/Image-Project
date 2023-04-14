from django.shortcuts import render,redirect
from imgapp.models import imgtable
import os

# Create your views here.
def mainpage(request):
    return render(request,'addproduct.html')
def addtable(request):
    if request.method=='POST':
        pname=request.POST['proname']
        pricep=request.POST['price']
        if request.FILES.get('pic') is not None:
            pimg=request.FILES.get('pic')
        else:
            pimg="/static/images/default.jpg"
        add=imgtable(product=pname,price=pricep,images=pimg)
        print("saved..")
        add.save()
        return redirect('showpage')
def showpage(request):
    img=imgtable.objects.all()
    return render(request,'shows.html',{'show':img})
def editpage(request,id):
    pro=imgtable.objects.get(id=id)
    return render(request,'editproduct.html',{'proedit':pro})
def update(request,id):
    if request.method=='POST':
        pro=imgtable.objects.get(id=id)
        pro.product=request.POST['proname']
        pro.price=request.POST['price']
        if len(request.FILES)!=0:
            if len(pro.images)>0:
                os.remove(pro.images.path)
            pro.images=request.FILES['pic']
        pro.save()
        return redirect('showpage')
    return render(request,'editproduct.html',)
def delete(request,id):
    pr=imgtable.objects.filter(id=id)
    pr.delete()
    return redirect('showpage')