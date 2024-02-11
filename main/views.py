from django.shortcuts import render

# Create your views here.


def main (request):
    return render(request,'home/main.html ')


from django.shortcuts import render, redirect

import base64
from django.core.files.base import ContentFile


from django.core.files.base import ContentFile
import base64
from .models import FaceImage

def datasetup(request):
    if request.method == 'POST':
        image_data_base64 = request.POST.get('image_data_base64')
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        address = request.POST.get('address')
        
        if image_data_base64:
            # Decode the base64 image data
            image_data_base64 = image_data_base64.split(',')[1]  # Remove data:image/jpeg;base64,
            image_data = base64.b64decode(image_data_base64)
            
            # Save the decoded image to the database
            image = ContentFile(image_data, name='myimage.jpg')  # Give a name to the image file
            FaceImage.objects.create(name=name, roll=roll, address=address, image=image)
            
    return render(request, 'home/datasetup.html')


