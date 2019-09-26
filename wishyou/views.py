import base64
import urllib
import json
import numpy as np
import cv2
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.db import transaction, IntegrityError
from .forms import PeopleForm
from django.core.mail import send_mail
from django.conf import settings
from wishyou.models import People


class Home(View):
    def get(self, request):
        data = {'name': 'Mayur'}
        people = People.objects.filter(email='q').get()
        a = json.loads(people.images)
        imaegs = []
        for val in a.values():
            image = np.asarray(val)
            success, encoded_image = cv2.imencode('.jpg', image)
            image = encoded_image.tobytes()
            image = base64.b64encode(image)
            imaegs.append(str(image)[2:-1])
        data['image'] = imaegs
        return render(request, 'wishyou/index.html', {'data':data})


class PeopleView(View):
    # template_name = 'wishyou/form.html'
    # model = People
    # form_class = PeopleForm
    # success_url = reverse_lazy("wishyou:home")
    def get(self, request):
        form = PeopleForm
        return render(request, 'wishyou/form.html', {'form': form})

    def post(self, request, **kwargs):
        # import code; code.interact(local=dict(globals(), **locals()))
        # return HttpResponse("Hi")
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    data = {"success": False}

                    form = PeopleForm(request.POST)

                    if form.is_valid():
                        # return HttpResponse("Hi")
                        # check to see if an image was uploaded
                        people = form.save(commit=False)
                        if request.FILES.get("image", None) is not None:
                            # grab the uploaded image
                            images = request.FILES.getlist('image')
                            image_list = {}
                            for index, image_file in enumerate(images):
                                image_list.update({index: self._grab_image(stream=image_file).tolist()})
                            # import code;
                            # code.interact(local=dict(globals(), **locals()))
                            people.images = json.dumps(image_list)
                            people.save()

                        # otherwise, assume that a URL was passed in
                        else:
                            # grab the URL from the request
                            url = request.POST.get("url", None)

                            # if the URL is None, then return an error
                            if url is None:
                                data["error"] = "No URL provided."
                                return JsonResponse(data)

                            # load the image and convert
                            image = self._grab_image(url=url).tolist()
                            # import code;
                            # code.interact(local=dict(globals(), **locals()))
                            people.images = json.dumps(image)
                            people.save()
                        import code;
                        code.interact(local=dict(globals(), **locals()))
                        ### START WRAPPING OF COMPUTER VISION APP
                        # Insert code here to process the image and update
                        # the `data` dictionary with your results
                        ### END WRAPPING OF COMPUTER VISION APP

                        # update the data dictionary
                        data["success"] = True

                    return render(request, 'wishyou/form.html', {'form_errors': form.errors, 'form': form})
            except Exception as e:
                print(str(e))

    def _grab_image(self, path=None, stream=None, url=None):
        # if the path is not None, then load the image from disk
        if path is not None:
            image = cv2.imread(path)

        # otherwise, the image does not reside on disk
        else:
            # if the URL is not None, then download the image
            if url is not None:
                resp = urllib.urlopen(url)
                data = resp.read()

            # if the stream is not None, then the image has been uploaded
            elif stream is not None:
                data = stream.read()

            # convert the image to a NumPy array and then read it into
            # OpenCV format
            # import code;
            # code.interact(local=dict(globals(), **locals()))
            image = np.asarray(bytearray(data), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # return the image
        return image


class AddPeople(View):
    def post(self, request):
        pass


class SendMail(View):
    def get(self, request):
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mvdream02@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return redirect(reverse_lazy("wishyou:home"))
