import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# ---------------------------------
# Load Student Dataset
# ---------------------------------

df = pd.read_csv("dataset.csv")

print("\nSTUDENT DATA")
print(df)


# Subjects
subjects = ["Maths", "Python", "Database"]


# ---------------------------------
# Performance Analysis
# ---------------------------------

df["Average_Marks"] = df[subjects].mean(axis=1)

df["Rank"] = df["Average_Marks"].rank(
    ascending=False
).astype(int)


print("\nSTUDENT PERFORMANCE")

print(
    df[
        ["Student", "Average_Marks", "Rank"]
    ].sort_values("Rank")
)


# ---------------------------------
# Weak Subject Detection
# ---------------------------------

print("\nWEAK SUBJECT ANALYSIS")

for index, row in df.iterrows():

    weak_subjects = []

    for subject in subjects:

        if row[subject] < 60:
            weak_subjects.append(subject)

    if weak_subjects:
        print(
            row["Student"],
            "needs improvement in:",
            ", ".join(weak_subjects)
        )

    else:
        print(
            row["Student"],
            "has good performance"
        )


# ---------------------------------
# Performance Visualization
# ---------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Student"],
    df["Average_Marks"]
)

plt.title("Student Average Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()


# ---------------------------------
# Exam Preparation Schedule Planner
# ---------------------------------

print("\nEXAM PREPARATION SCHEDULE")


exam_date = input(
    "Enter exam date (YYYY-MM-DD): "
)

exam_date = datetime.strptime(
    exam_date,
    "%Y-%m-%d"
)


days_left = (
    exam_date - datetime.now()
).days


print(
    "\nDays left for exam:",
    days_left
)


student_name = input(
    "Enter student name: "
)


student = df[
    df["Student"] == student_name
]


if student.empty:

    print("Student not found")

else:

    student = student.iloc[0]

    print(
        "\nPersonal Study Plan for",
        student_name
    )


    current_day = datetime.now()


    for day in range(days_left):

        print(
            "\nDay",
            day + 1,
            "-",
            current_day.strftime("%d-%m-%Y")
        )


        for subject in subjects:

            if student[subject] < 60:

                print(
                    subject,
                    ": 2 hours (Weak Subject)"
                )

            else:

                print(
                    subject,
                    ": 1 hour Revision"
                )


        current_day += timedelta(days=1)


# ---------------------------------
# Study Recommendation
# ---------------------------------

print("\nSTUDY RECOMMENDATION")

for index, row in df.iterrows():

    if row["Study_Hours"] < 4:

        print(
            row["Student"],
            ": Increase daily study hours"
        )

    else:

        print(
            row["Student"],
            ": Good preparation level"
        )


print("\nProject Completed Successfully!")
