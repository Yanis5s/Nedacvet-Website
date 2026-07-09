from django.shortcuts import render

def home_view(request):
    return render(request, 'NedaCvet/home.html')

def gallery_view(request):
    return render(request, 'NedaCvet/gallery.html')

def contact_view(request):
    return render(request, 'NedaCvet/contact.html')

def LaserCutPanels_view(request):
    return render(request, 'NedaCvet/LaserCutPanels.html')

def aluminumRailings_view(request):
    return render(request, 'NedaCvet/aluminumRailings.html')

def metalRailings_view(request):
    return render(request, 'NedaCvet/metalRailings.html')

def aluminumPergolas_view(request):
    return render(request, 'NedaCvet/aluminumPergolas.html')

def glassRailings_view(request):
    return render(request, 'NedaCvet/glassRailings.html')

def railings_view(request):
    return render(request, 'NedaCvet/railings.html')

def exteriorDesign_view(request):
    return render(request, 'NedaCvet/exteriorDesign.html')

def rollerBlinds_view(request):
    return render(request, 'NedaCvet/rollerBlinds.html')


