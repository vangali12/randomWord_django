# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
	request.session['count'] = 0
	return render(request, 'randomWord_app/index.html')

def getVal(request):
	randomFourteen = request.session['randomFourteen'] = get_random_string(length=14)
	request.session['count'] += 1
	context = {
		'randomFourteen': randomFourteen,
	}
	return render(request, 'randomWord_app/index.html', context)