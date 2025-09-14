from django.shortcuts import render,redirect
from vege.models import *
from django.http import HttpResponse
# Create your views here.
def receipes(request):
    if request.POST:
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        print(receipe_description)
        print(receipe_image)
        print(receipe_name)
        Receipe.objects.create(
            receipe_description = receipe_description,
            receipe_name = receipe_name,
            receipe_image = receipe_image
        )
        return redirect('/receipes')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains= request.GET.get('search'))
    context = {'receipes':queryset}
    return render(request,'receipes.html',context)



def delete_receipe(request,id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    return redirect('/receipes')



def update_receipe(request,id):
    querySet = Receipe.objects.get(id = id) 
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description
        if receipe_image:
            querySet.receipe_image = receipe_image
        querySet.save()
        return redirect('/receipes')
    context = {'receipe':querySet}
    return render(request,'update_receipes.html',context)