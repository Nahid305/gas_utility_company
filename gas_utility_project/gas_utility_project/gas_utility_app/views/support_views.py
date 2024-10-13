from django.shortcuts import render
from django.http import HttpResponse

def list_requests(request):
    return HttpResponse("List of Service Requests")

def resolve_request(request, request_id):
    return HttpResponse(f"Resolving Request {request_id}")
