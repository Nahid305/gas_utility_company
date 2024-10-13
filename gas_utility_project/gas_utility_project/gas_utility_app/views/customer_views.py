from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Gas Utility Service Portal")

def submit_request(request):
    return HttpResponse("Submit a Service Request")

def track_request(request, request_id):
    return HttpResponse(f"Tracking Request {request_id}")
