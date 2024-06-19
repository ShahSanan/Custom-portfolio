from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signup')
def index(request):

    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is home page now")
def home(request):
    return render(request, 'about.html',)
    #return HttpResponse("This is about page")
def services(request):
    return render(request, 'services.html',)
def test(request):
    return render(request, 'test.html')

    #return HttpResponse("This is service page")
def register(request):
    return render(request, 'register.html',)
def customize(request):
    return render(request, 'customize.html',)
def order(request):
    return render(request,  'order.html')
def checkout(request):
    return render(request, "checkout.html")

def base(request):
    return render(request, 'index.html')
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm




from django.shortcuts import render, HttpResponse
from .models import Customization
from django.views.decorators.csrf import csrf_exempt  # Import the decorator

 # Add this decorator to exempt CSRF protection for this view (for demonstration purposes only)

from datetime import datetime
from home.models import Contact, Customization
from django.contrib import messages

def handle_customization(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        pages = request.POST.get('pages')
        budget = request.POST.get('budget')
        payment = request.POST.get('payment')
        delivery = request.POST.get('delivery')
        email = request.POST.get('email')  # Corrected field name       
        description = request.POST.get('details')   # Corrected field name
       
        # Create a new Customization instance with the form data
        customization = Customization(pages=pages, budget=budget, payment_option=payment, delivery_option=delivery, name=name,email=email, description=description,)  # Corrected field name
        
        # Set the name of the customization form dynamically based on the user's input
        customization_name = f"{name}'s"
        customization.name = customization_name
        
        # Save the customization instance
        customization.save()
        
        # Redirect to a success page or render a template
        return HttpResponse('Details submitted successfully!')
    else:
        # Handle GET requests or invalid requests
        return HttpResponse('Invalid request')
    
def kaam(request):
    return render(request, 'kaam.html')
def review(request):
    return render(request, 'review.html')
def internship(request):
    return render(request, 'internship.html')
def terms(request):
    return render(request, 'terms.html')
def privacy(request):
    return render(request, 'privacy.html')
# views.py
from django.shortcuts import render
from django.http import JsonResponse


# views.py
from django.shortcuts import render

def order_placed(request):
    return render(request, 'order_placed.html')



def save_order(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment')
        cc_name = request.POST.get('cc-name')  
        # ... extract other order data from request.POST

        # Create a new Order instance
        new_order = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            payment=payment_method,
            cc_name=cc_name, 
            # ... other order fields
        )

        # Save the order instance
        new_order.save()

        return HttpResponse('Order submitted successfully!')
    else:
        # Handle invalid requests (optional)
        return HttpResponse('Invalid request method')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get( 'desc' )
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Form has been submitted.")
         # Redirect to the contact page to clear the form after submission
       
    return render(request, 'contact.html',)
   # return HttpResponse("This is contact page")
from .models import Order
from django.http import JsonResponse
from django.shortcuts import render
# Import the Order model at the top of your views.py file
def signup(request):
    return render(request, 'signup.html')

from django.shortcuts import redirect


from .models import Order

def process_checkout(request):
    if request.method == 'POST':
        try:
            # Retrieve form data
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            email = request.POST.get('email')
            country = request.POST.get('country')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip')
            payment_method = request.POST.get('paymentMethod')
            cc_name = request.POST.get('cc-name')
            cc_number = request.POST.get('cc_number')
            cc_expiration = request.POST.get('cc-expiration')
            cc_cvv = request.POST.get('cc-cvv')
            
            # Create a new order instance and save it to the database
            order = Order(
                first_name=first_name,
                last_name=last_name,
                email=email,
                country=country,
                state=state,
                zip_code=zip_code,
                payment_method=payment_method,
                cc_name=cc_name,
                cc_number=cc_number,
                cc_expiration=cc_expiration,
                cc_cvv=cc_cvv,
            )
            
            # Add success message
            order.save()
            messages.success(request, 'New Order!')
            return redirect('order_placed')
            # Redirect to the order placed page if the order is saved successfully
            
        except Exception as e:
            # Handle the error gracefully, you can return an error message or render a specific template
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'checkout')

    # Redirect to the checkout page if the request method is not POST
    return redirect('checkout')
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

def login_user(request):
    if request.method == 'POST':
        usern = request.POST.get('msd_username')  # Corrected syntax
        pass1 = request.POST.get('kohli_password')  # Corrected syntax
        halwa = authenticate(request, username=usern, password=pass1)
        if halwa is not None:
            login(request, halwa)
            return redirect('home')  # Redirect to home page after successful login
        else:
           return render(request, 'register.html')




    
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('naam')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        # Check if passwords match
      

        # Create a new user
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        
        # Redirect to a success page or any other desired page
        return redirect('register')

    return render(request, 'signup.html')

