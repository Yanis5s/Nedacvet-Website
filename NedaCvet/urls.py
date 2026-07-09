from django.urls import path
from . import views   # better than importing the app by name

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('panels/', views.LaserCutPanels_view, name='panels'),
    path('aluminumRailings/', views.aluminumRailings_view, name='aluminumRailings'),
    path('metalRailings/', views.metalRailings_view, name='metalRailings'),
    path('aluminumPergolas/', views.aluminumPergolas_view, name='aluminumPergolas'),
    path('glassRailings/', views.glassRailings_view, name='glassRailings'),
    path('railings/', views.railings_view, name='railings'),
    path('exteriorDesign/', views.exteriorDesign_view, name='exteriorDesign'),
    path('rollerBlinds/', views.rollerBlinds_view, name='rollerBlinds'),

]
