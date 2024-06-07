from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

# Create your views here.
def Attendance(request):
    srt=r"path/main.py"
    if not os.path.exists(srt):
        return HttpResponse(f"Error: File not found at {srt}")
    try:
        subprocess.Popen(['python', srt])
        return HttpResponse("<h1>**********************FACE  RECOGNITION  BASED  ATTENDANCE  SYSTEM**********************</h1>")
    except Exception as e:
        return HttpResponse(f"Error: {e}")