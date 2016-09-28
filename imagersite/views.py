from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index_view(request):
    template = loader.get_template('imagersite/home.html')
    # import pdb; pdb.set_trace();
    response_body = template.render()
    return HttpResponse(response_body)

    # return render(request, 'template/path/here')
