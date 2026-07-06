#importing library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("students.csv")
#main function which will contain analysis of the csv file
def main():
    print("========== Student Performance Analysis ==========")
    print()
    
    print("Datasest Information")
    print("--------------------")
    print("Total Students:",len(df))
    print("Rows X Columns:",df.shape)
    print()
    
    print("Attendance Statistics")
    print("--------------------")
    print('Average attendance: ',df["Attendance"].mean())
    print('Highest attendance: ',df["Attendance"].max())
    print('Lowest attendance: ',df["Attendance"].min())
    print()

    print("Top Scorer(s)")
    print("--------------------")
    print(df[df["Marks"]==df["Marks"].max()])
    print()

    print("Students Scoring Above 90")
    print("--------------------")
    print(df[df["Marks"]>90])
    print()

    print("Summary Statistics")
    print("--------------------")
    print(df.describe())
    print()
if __name__=="__main__":
    main()


#creating graphs
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.savefig("charts/marks_bar.png")
plt.show()
plt.close()

plt.plot(df["Name"], df["Attendance"])
plt.title("Attendance")
plt.savefig("charts/attendance_line.png")
plt.show()
plt.close()
