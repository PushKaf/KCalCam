from django.shortcuts import render, redirect
from .form import FormImage
from .models import Image
import logging
import yoloClassifier
import nutritionData
# Create your views here.

def index(request):
    img = Image.objects.all()

    if request.method == "POST":
        form = FormImage(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            classified = yoloClassifier.main(obj.userImage.path, obj.userImage.path)
            foodInfo = nutritionData.getFoodInfo(classified[0][0])
            # print(foodInfo)
            return render(request, "main/choices.html", {"food":foodInfo, "obj":obj})
    else:
        form = FormImage()

    return render(request, "main/index.html", {"img": img, "form":form})
