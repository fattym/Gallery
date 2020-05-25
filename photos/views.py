from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.db.models import Q


from .models import Images,Location,Category

# Create your views here.
def home(request):
    images= Images.objects.all()
    category= Category.objects.all()
    return render(request, "home.html", {"images":images,"category":category})


def about(request):  
    category= Category.objects.all()
    return render(request, "about.html", {"category":category})
class SearchResultsListView(ListView):
    model = Images
    context_object_name = 'images_list'
    template_name = 'search.html'
    

    def get_queryset(self): 
        query = self.request.GET.get('q')
        if Images.objects.filter(Q(image_category=query)):
            return Images.objects.filter(Q(image_category=query))

class SearchLocationListView(ListView):
    model = Images
    context_object_name = 'images_list'
    template_name = 'location.html'
    

    def get_queryset(self): 
        query = self.request.GET.get('q')
        if Images.objects.filter(Q(image_location=query)):
            return Images.objects.filter(Q(image_location=query))



def get_location(request):
    locations = Location.objects.all()
   
    return render(request,'all-photos/locations.html',{'all_images':location_result,'category_results':category_results,'locations':locations})


