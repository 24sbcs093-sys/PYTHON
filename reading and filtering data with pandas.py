import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Meena", "Karthik", "Divya"],
    "Age": [19, 21, 22, 20, 23],
    "Department": ["CS", "IT", "CS", "ECE", "IT"],
    "City": ["Chennai", "Coimbatore", "Chennai", "Madurai", "Chennai"],
    "Marks": [85, 78, 92, 67, 88]
}

df = pd.DataFrame(data)

print("\nFULL DATASET")
print(df)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATA INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nSTUDENTS AGE > 20")
print(df[df["Age"] > 20])

print("\nSTUDENTS FROM CHENNAI")
print(df[df["City"] == "Chennai"])

print("\nCS DEPARTMENT STUDENTS")
print(df[df["Department"] == "CS"])

print("\nMARKS GREATER THAN 80")
print(df[df["Marks"] > 80])

print("\nAGE > 20 AND CITY = CHENNAI")
print(df[(df["Age"] > 20) & (df["City"] == "Chennai")])

print("\nONLY NAME AND MARKS")
print(df[["Name", "Marks"]])
