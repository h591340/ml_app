from django import forms

class SalaryPredictionForm(forms.Form):

    job_title = forms.CharField(max_length=100, label="Job Title",widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control mb-2'} ))
    years_of_experience = forms.FloatField(label="Years of Experience" ,widget=forms.NumberInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control mb-2'} ) )
    age = forms.FloatField(label="Age",widget=forms.NumberInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control mb-2'} ) )
    education_level = forms.ChoiceField(
        choices=[(0.0, "Bachelor's"), (1.0, "Master's"), (2.0, "PhD")],
        label="Education Level",
        widget=forms.Select(attrs={'style': 'width: 300px;', 'class': 'form-control mb-2'} )
        
    )
    gender = forms.ChoiceField(
        choices=[(0.0, "Female"), (1.0, "Male")],
        label="Gender",
        widget=forms.Select(attrs={'style': 'width: 300px;', 'class': 'form-control mb-2'} )
    )

    ml_model = forms.ChoiceField(
        choices=[(0.0, "RandomForestRegressor"), (1.0, "LinearRegression"),
        (2.0,"ElasticNet"),
        (3.0,"GradientBoostingRegressor")
        ],
        label="ML Model",
        widget=forms.Select(attrs={'style': 'width: 300px;', 'class': 'form-control mb-2'} )
    )