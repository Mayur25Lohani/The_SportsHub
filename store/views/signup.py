from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.products import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self , request):
        return render(request , 'signup.html')
    def post(self , request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # cpassword = postData.get('cpassword')
        value = {'first_name' : first_name, 'last_name' : last_name , 'phone' : phone , 'email' : email}

        customer = Customer(first_name = first_name , last_name = last_name , phone = phone , email = email , password = password)
        error_message = self.validateCustomer(customer) 

        if  not error_message:
            print(first_name , last_name , phone , email , password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error' : error_message, 'values' : value}
            return render(request , "signup.html" , data)    
    def validateCustomer(self , customer):
        error_message = None

        if(not customer.first_name):
            error_message = "First Name Required!!"
        elif len(customer.first_name) > 25:
            error_message = "First Name can't be more than 25 letters!!"
        elif(not customer.last_name):
            error_message = "Last Name Required!!"
        elif len(customer.last_name) > 25:
            error_message = "Last Name can't be more than 25 letters!!"
        elif (not customer.phone):
            error_message = "Phone Number Required!!"
        elif len(customer.phone) <10:
            error_message = "Phone Number must be of 10 digits!!"   
        elif (not customer.email):
            error_message = "Email Required!!"
        elif (not customer.password):
            error_message = "Password Required!!" 
        elif len(customer.password) < 8:
            error_message = "Password must be of 8 characters!!" 
        # elif (password != cpassword):
        #   error_message = "Passwords don't match!!"  
        elif customer.isExist():
            error_message = 'Email Address already Registered!!' 

        return error_message     


        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # cpassword = postData.get('cpassword')
        value = {'first_name' : first_name, 'last_name' : last_name , 'phone' : phone , 'email' : email}

        customer = Customer(first_name = first_name , last_name = last_name , phone = phone , email = email , password = password)
        error_message = validateCustomer(customer) 

        if  not error_message:
            print(first_name , last_name , phone , email , password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error' : error_message, 'values' : value}
            return render(request , "signup.html" , data) 