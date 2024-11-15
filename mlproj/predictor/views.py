import joblib
from django.shortcuts import render
from .forms import SalaryPredictionForm
from collections import OrderedDict
from  predictor import models
from sklearn.preprocessing import StandardScaler


# Load models and scaler
lr = joblib.load('.\\predictor\\mlmodels\\lr.pkl')
en = joblib.load('.\\predictor\\mlmodels\\en.pkl')
gb = joblib.load('.\\predictor\\mlmodels\\gb.pkl')
rf = joblib.load('.\\predictor\\mlmodels\\rf.pkl')
scaler = joblib.load('.\\predictor\\mlmodels\\scaler.pkl')


def data(request):
    employees = models.Employee.objects.all()
    return render(request, 'predictor/data.html', {'employees': employees})


def predict_salary(request):
    prediction = None
    if request.method == 'POST':
        form = SalaryPredictionForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            category_list =  get_category(form.cleaned_data['job_title'])
            years_of_experience = float(form.cleaned_data['years_of_experience'])
            age = float(form.cleaned_data['age'])
            education_level = float(form.cleaned_data['education_level'])
            gender = float(form.cleaned_data['gender'])
            model = None
            ml_model = float(form.cleaned_data['ml_model'])

            if ml_model == 0.0:
                model = rf
            elif ml_model == 1.0:
                model = lr
            elif ml_model == 2.0:
                model = en
            else:
                model = gb
            
            features_to_scale = [[age, years_of_experience]]  
           # Scale the age and years_of_experience values
            scaled_features = scaler.transform(features_to_scale)  # Scaled only age and years_of_experiences)
            scaled_age, scaled_experience = scaled_features[0]  # Unpack the scaled values
            
            # Transform inputs into a format the model can understand
            input_data = [[scaled_age,gender,education_level,scaled_experience]+category_list]
            # Get the salary prediction
            prediction = round(model.predict( input_data)[0])
    else:
        form = SalaryPredictionForm()

    return render(request, 'predictor/predict_salary.html', {'form': form, 'prediction': prediction})



def get_category(title):
    # Define broad job categories and the keywords associated with each
    job_categories = {
    "Tech": ["Engineer", "Developer", "Data", "Scientist", "Software", "IT", "UX", "Web"],
    "Sales": ["Sales", "Account Manager", "Customer Success", "Representative","Rep", "Business Development"],
    "Marketing": ["Marketing", "Brand", "Social Media", "Content", "Advertising"],
    "Other":[],
    "Management": ["Manager", "Director", "VP", "Executive", "CEO", "Chief"],
    "Support": ["Support", "Help Desk", "Administrative", "Operations", "Analyst", "Coordinator"],
    "Finance": ["Accountant", "Financial Advisor", "Finance"],
    "Design": ["Designer", "Graphic", "Product Designer"],
    "Human Resources": ["HR", "Recruiter", "Human Resources"],
    "Consulting": ["Consultant", "Strategy Consultant"],
    "Training": ["Training Specialist", "Trainer"],
    "Writing": ["Writer", "Copywriter", "Technical Writer"]
    }
    zeroed_ordered_dict = OrderedDict((key, 0) for key in sorted(job_categories))


    if not title:
            zeroed_ordered_dict["Other"] = 1
            return list(zeroed_ordered_dict.values())

    for category, keywords in job_categories.items():
            if any(keyword in title for keyword in keywords):
                zeroed_ordered_dict[category] = 1
                return list(zeroed_ordered_dict.values())



    zeroed_ordered_dict["Other"] = 1
    return list(zeroed_ordered_dict.values())
