from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from main.models import *


def account (request):
    return render(request,'account/account.html')

from main.models import FaceImage

from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

import face_recognition
import base64

def match(request):
    if request.method == 'POST':
        image_data_base64 = request.POST.get('image_data_base64')
        
        if image_data_base64:
            image_data_base64 = image_data_base64.split(',')[1]
            image_data = base64.b64decode(image_data_base64)
            image = ContentFile(image_data, name='myimage.jpg')
            
            # Load the uploaded image file
            uploaded_image = face_recognition.load_image_file(image)
            
            # Get face encodings for the uploaded image
            try:
                uploaded_face_encoding = face_recognition.face_encodings(uploaded_image)[0]
            except IndexError:
                # If no face is found in the uploaded image
                return redirect('match')
            
            # Iterate through faces in database and find match
            faces = FaceImage.objects.all()
            for face in faces:
                face_image_path = face.image.path
                known_image = face_recognition.load_image_file(face_image_path)
                known_face_encoding = face_recognition.face_encodings(known_image)[0]
                
                # Compare faces
                results = face_recognition.compare_faces([known_face_encoding], uploaded_face_encoding)
                
                if results[0]:
                    # If a match is found, redirect to details page with the matched face details
                    request.session['matched_face_details'] = {
                        'name': face.name,
                        'roll': face.roll,
                        'address': face.address,
                        'image_url': face.image.url
                        
                    }
                    return redirect('details')
                    
    return render(request, 'account/match.html')

def details(request):
    context = {
        'details': request.session.get('matched_face_details')
    }
    return render(request, 'account/details.html', context)

