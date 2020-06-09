from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')

class BuiltinsView(View):
    def get(self, request):
        return render(request, 'main/builtins.html')

class CustomView(View):
    def get(self, request):
        return render(request, 'main/custom.html')
