from django.shortcuts import render, redirect
from .models import BasicQuestion
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def userLogout(request):
    logout(request)  # Logs out the user
    messages.success(request, 'You have successfully logged out.')  # Add a logout message
    return redirect('login')  # Redirect to the login page



def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('chart') 
        else:
          
            messages.error(request, 'Invalid email or password')

    
    return render(request, 'login.html')



def homepage(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        awareness1 = request.POST.get('awareness1')
        awareness2 = request.POST.get('awareness2')
        awareness3 = request.POST.get('awareness3')
        financial1 = request.POST.get('financial1')
        financial2 = request.POST.get('financial2')

        # Validate and save the data
        if age and gender:  # Add more validation rules as needed
            BasicQuestion.objects.create(
                age=age,
                gender=gender,
                awareness1=awareness1,
                awareness2=awareness2,
                awareness3=awareness3,
                financial1=financial1,
                financial2=financial2
            )
            messages.success(request, 'Your form has been successfully submitted!')
        else:
            messages.error(request, 'Please fill in all required fields.')

   
    return render(request, 'forms.html')



@login_required
def chart(request):
    age_18_30 = BasicQuestion.objects.filter(age='18-30').count()
    age_31_45 = BasicQuestion.objects.filter(age='31-45').count()
    age_46_60 = BasicQuestion.objects.filter(age='46-60').count()
    age_61_plus = BasicQuestion.objects.filter(age='61-above').count()
    
    gender_male = BasicQuestion.objects.filter(gender='male').count()
    gender_female = BasicQuestion.objects.filter(gender='female').count()
    
    awareness_1_1 = BasicQuestion.objects.filter(awareness1='yes').count()
    awareness_1_2 = BasicQuestion.objects.filter(awareness1='no').count()

    awareness_2_1 = BasicQuestion.objects.filter(awareness2='yes').count()
    awareness_2_2 = BasicQuestion.objects.filter(awareness2='no').count()
    
    awareness_3_1 = BasicQuestion.objects.filter(awareness3='yes').count()
    awareness_3_2 = BasicQuestion.objects.filter(awareness3='no').count()
    
    financial_1_1 = BasicQuestion.objects.filter(financial1='Yes, I have a dedicated fund.').count()
    financial_1_2 = BasicQuestion.objects.filter(financial1='Yes, I have funeral insurance.').count()
    financial_1_3 = BasicQuestion.objects.filter(financial1='No, but I am planning to.').count()
    
    financial_2_1 = BasicQuestion.objects.filter(financial2='Personal savings').count()
    financial_2_2 = BasicQuestion.objects.filter(financial2='Life insurance').count()
    financial_2_3 = BasicQuestion.objects.filter(financial2='Funeral insurance').count()
    
    # Total count of BasicQuestion entries
    total_count = BasicQuestion.objects.count()
    context = {
        'age_18_30': age_18_30,
        'age_31_45': age_31_45,
        'age_46_60': age_46_60,
        'age_61_plus': age_61_plus,
        'gender_male': gender_male,
        'gender_female': gender_female,
        
        'awareness_1_1': awareness_1_1,
        'awareness_1_2': awareness_1_2,
        
        'awareness_2_1': awareness_2_1,
        'awareness_2_2': awareness_2_2,
        
        'awareness_3_1': awareness_3_1,
        'awareness_3_2': awareness_3_2,
        
        'financial_1_1': financial_1_1,
        'financial_1_2': financial_1_2,
        'financial_1_3': financial_1_3,
        
        'financial_2_1': financial_2_1,
        'financial_2_2': financial_2_2,
        'financial_2_3': financial_2_3,
        
        'total_count': total_count,
    }
    
    return render(request, 'charts.html', context)