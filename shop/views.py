from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from shop.models import Contact
from django.contrib import messages

def index(request):
    # params={'product':products, 'slides':range(2), 'images':range(3)}
    return render(request, "shop/index.html")

def contact(request):
    return render(request, "shop/contact_us.html") 
    
def contact_handle(request):
    try:
        if request.method == 'POST':
            UName = request.POST['Name']
            UEmail = request.POST['Email']
            Udesc = request.POST['Discription']
            
            if(len(UName)<2 or len(Udesc)<3):
                messages.warning(request, 'Please fill form correctly.')
                
            # Create the user
            else:
                user= Contact(name=UName, emali=UEmail, desc=Udesc)
                user.save()
                messages.success(request, 'Form submited sucessfully.')
            
            return render(request, "shop/contact_us.html")
        else:
            return HttpResponse('<b> Error 404 : Invalid request </b>') 
    except:
        messages.error(request, 'Error in filling form')
            
def Item(request):
    return render(request, "shop/Product.html")            