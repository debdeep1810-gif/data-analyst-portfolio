import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\HR_analysis.csv")

# Show dataset
print("Dataset Preview:")
print(df.head())

# Gender count (instead of attrition)
gender_count = df["Gender"].value_counts()
print("\nGender Count:")
print(gender_count)

# Plot: Gender Count
plt.figure()
gender_count.plot(kind='bar')
plt.title("Employee Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# (Optional) Add Salary plot ONLY if Salary column exists
if "Salary" in df.columns:
    avg_salary = df.groupby("Department")["Salary"].mean()

    plt.figure()
    avg_salary.plot(kind='bar')
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.show()
