from django.shortcuts import render



# Create your views here.
def main_page_view(request):
    context = {
    }
    return render(request, "mainpage.html", context)

