from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index_view(request):
    template = loader.get_template('imagersite/home.html')
    photo_filter = ['public']
    if request.user.is_authenticated:
        photo_filter.append('shared')
    photo = Photograph.objects.filter(published=photo_filter).order_by('?').first()
    # import pdb; pdb.set_trace();
    response_body = template.render()
    return HttpResponse(response_body)


    # return render(request, 'template/path/here')
