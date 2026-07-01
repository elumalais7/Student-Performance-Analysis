import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# -------------------------------
# Create Student Dataset
# -------------------------------

data = {
    "Student": ["Arun", "Priya", "Kavin", "Meena", "Rahul"],
    "Maths": [75, 45, 80, 60, 55],
    "Python": [85, 70, 90, 65, 60],
    "Database": [70, 50, 85, 75, 55],
    "Attendance": [90, 80, 95, 85, 75],
    "Study_Hours": [5, 3, 6, 4, 2]
}

df = pd.DataFrame(data)

print("\nSTUDENT DATA")
print(df)


# -------------------------------
# Performance Analysis
# -------------------------------

subjects = ["Maths", "Python", "Database"]

df["Average_Marks"] = df[subjects].mean(axis=1)

print("\nSTUDENT PERFORMANCE")
print(df[["Student", "Average_Marks"]])


# Ranking

df["Rank"] = df["Average_Marks"].rank(
    ascending=False
)

print("\nRANKING")
print(df[["Student","Average_Marks","Rank"]])


# -------------------------------
# Weak Subject Detection
# -------------------------------

print("\nWEAK SUBJECT ANALYSIS")

for index,row in df.iterrows():

    weak = []

    for subject in subjects:
        if row[subject] < 60:
            weak.append(subject)

    print(row["Student"], "needs improvement in:", weak)



# -------------------------------
# Graph Analysis
# -------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Student"],
    df["Average_Marks"]
)

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



# -------------------------------
# Study Schedule Generator
# -------------------------------


print("\nEXAM PREPARATION SCHEDULE")


exam_date = input(
    "Enter exam date (YYYY-MM-DD): "
)

exam_date = datetime.strptime(
    exam_date,
    "%Y-%m-%d"
)


days_left = (exam_date - datetime.now()).days


print("\nDays Left:",days_left)



student = input(
    "Enter student name: "
)


student_data = df[
    df["Student"] == student
]


if student_data.empty:

    print("Student not found")

else:

    marks = student_data.iloc[0]

    print("\nPersonal Study Plan")

    day = datetime.now()


    for i in range(days_left):

        print(
        "\nDay",
        i+1,
        day.strftime("%d-%m-%Y")
        )

        for subject in subjects:

            if marks[subject] < 60:

                print(
                subject,
                " - 2 hours (Weak Subject)"
                )

            else:

                print(
                subject,
                " - 1 hour Revision"
                )

        day += timedelta(days=1)

print("\nSTUDY RECOMMENDATION")

for index,row in df.iterrows():

    if row["Study_Hours"] < 4:

        print(
        row["Student"],
        ": Increase study time"
        )

    else:

        print(
        row["Student"],
        ": Good preparation"
        )