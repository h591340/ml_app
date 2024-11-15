import pandas as pd
from django.contrib.auth.models import User
from predictor.models import Employee
import math
# Read CSV file into a DataFrame
csv_file_path = '..\\mlproj\\predictor\\data\\salary_data.csv'
df = pd.read_csv(csv_file_path)

Employee.objects.all().delete()

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
   
    employee, created = Employee.objects.get_or_create(
        age= row['Age'] if not math.isnan(row['Age']) else 0,
        gender=row['Gender']  ,
        jobTitle=row['Job Title']  ,
        educationLevel=row['Education Level'],
        yearsOfExperience=row['Years of Experience'] if  not  math.isnan(row['Years of Experience']) else 0,
        salary=row['Salary'] if not math.isnan(row['Salary']) else 0,

    )

  
    employee.save()

print("CSV data has been loaded into the Django database.")