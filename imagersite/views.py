from django.shortcuts import render
# from django.http import HttpResponse
from django.template import loader
from imager_images.models import Photo


def index_view(request):
    # template = loader.get_template('imagersite/home.html')
    photo_filter = ['public']
    if request.user.is_authenticated:
        photo_filter.append('shared')
    photo = Photo.objects.filter(published=photo_filter).order_by('?').first()
    context = {'photo': photo}
    # import pdb; pdb.set_trace();
    # response_body = template.render()
    # response_body.photo = photo
    # return HttpResponse(response_body)
    return render(request, 'imagersite/home.html', context)
