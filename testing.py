import pandas as pd

data = {
    "Name": ["Khizer", "Rahul", "Ayesha", "Arjun", "Sara"],
    "Python": [85, 72, 92, 65, 88],
    "SQL": [90, 68, 95, 70, 84],
    "Pandas": [88, 75, 91, 60, 93],
}

df = pd.DataFrame(data)

df["Average"] = df[["Python", "SQL", "Pandas"]].mean(axis=1)

df["Grade"] = df["Average"].apply(
    lambda marks: "A" if marks >= 85 else "B" if marks >= 70 else "C"
)

print("Student Results:")
print(df)

print("\nClass Average:", round(df["Average"].mean(), 2))

topper = df.loc[df["Average"].idxmax()]
print("\nTopper:", topper["Name"])
print("Topper's Average:", round(topper["Average"], 2))

print("\nStudents scoring above 80:")
print(df[df["Average"] > 80][["Name", "Average"]])
