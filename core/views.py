# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse, render_to_response
from tools import create_validate_code
import StringIO


def check_code(request):
    mstream = StringIO.StringIO()
    validate_code = create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")
    return HttpResponse(mstream.getvalue())


def home(request):
    return render_to_response('index.html')