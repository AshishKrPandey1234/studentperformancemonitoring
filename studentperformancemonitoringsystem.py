from tkinter import *
import tkinter.messagebox as tmsg

def calculate_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return 'O'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    elif 50 <= marks < 60:
        return 'P'
    else:
        return 'F'

def calculate_cgpa(total_marks):
    return round(total_marks / len(subjects_list), 2) / 10

def show_report_card(data):
    report_window = Toplevel(root)
    report_window.title("Report Card")
    report_window.geometry("600x400")

    Label(report_window, text="Report Card", font="comicsansms 16 bold", pady=20).pack()

    details_frame = Frame(report_window)
    details_frame.pack(pady=10)
    Label(details_frame, text=f"Name: {data['Enter Your Name']}", font="comicsansms 12").grid(row=0, column=0, sticky='w')
    Label(details_frame, text=f"Roll No: {data['Enter Your Roll No']}", font="comicsansms 12").grid(row=1, column=0, sticky='w')

    table_frame = Frame(report_window)
    table_frame.pack(pady=10)

    subjects = ["Subject", "Marks", "Grade"]
    for i, subject in enumerate(subjects):
        Label(table_frame, text=subject, font="comicsansms 12 bold", borderwidth=1, relief="solid", padx=10, pady=5).grid(row=0, column=i)

    total_marks = 0
    for i, subject in enumerate(subjects_list):
        marks = data[subject]
        grade = calculate_grade(marks)
        total_marks += int(marks)

        Label(table_frame, text=subject, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i+1, column=0)
        Label(table_frame, text=marks, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i+1, column=1)
        Label(table_frame, text=grade, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i+1, column=2)

    cgpa = calculate_cgpa(total_marks)
    Label(report_window, text=f"Total Marks: {total_marks}", font="comicsansms 12 bold", pady=10).pack()
    Label(report_window, text=f"CGPA: {cgpa}", font="comicsansms 12 bold", pady=10).pack()

    Button(report_window, text="Close", command=report_window.destroy).pack(pady=20)

def getvals():
    # Validate inputs
    for subject, var in variables.items():
        if not var.get():
            tmsg.showerror("Error", f"Please enter the {subject.lower()}.")
            return

    # Collect data
    data = {subject: var.get() for subject, var in variables.items()}

    # Save data to dictionary
    student_data[data["Enter Your Roll No"]] = data

    # Clear the entries
    for var in variables.values():
        var.set("")

    tmsg.showinfo("Success", "Marks submitted successfully")

def retrieve_student_details():
    roll_no = retrieve_roll_no_var.get()
    if roll_no in student_data:
        show_report_card(student_data[roll_no])
    else:
        tmsg.showerror("Error", "Student not found")

# Initialize main window
root = Tk()
root.geometry("658x600")
root.title("Student Performance Monitoring System")

# Heading
Label(root, text="Enter Your Internal Marks", font="comicsansms 13 bold", pady=20).grid(row=0, column=3)

# Subjects
subjects_list = [
    "BEEE",
    "EM II",
    "DSA",
    "OOPS",
    "CBM",
    "DM"
]

# Labels and Entries
variables = {}
Label(root, bg="grey", text="Enter Your Name", pady=10, relief=SUNKEN).grid(row=1, column=2)
variables["Enter Your Name"] = StringVar()
Entry(root, textvariable=variables["Enter Your Name"]).grid(row=1, column=3)

Label(root, bg="grey", text="Enter Your Roll No", pady=10, relief=SUNKEN).grid(row=2, column=2)
variables["Enter Your Roll No"] = StringVar()
Entry(root, textvariable=variables["Enter Your Roll No"]).grid(row=2, column=3)

for i, subject in enumerate(subjects_list):
    Label(root, bg="grey", text=subject, pady=10, relief=SUNKEN).grid(row=i+3, column=2)
    variables[subject] = StringVar()
    Entry(root, textvariable=variables[subject]).grid(row=i+3, column=3)

# Checkbox
confirmation = Checkbutton(root, text="Confirm your marks")
confirmation.grid(row=len(subjects_list)+3, column=3)

# Submit button
Button(root, text="Submit Your Internal Marks", command=getvals).grid(row=len(subjects_list)+4, column=3)

# Retrieve student details section
Label(root, text="Retrieve Student Details", font="comicsansms 13 bold", pady=20).grid(row=len(subjects_list)+5, column=3)
Label(root, text="Enter Roll No", bg="grey", pady=10, relief=SUNKEN).grid(row=len(subjects_list)+6, column=2)
retrieve_roll_no_var = StringVar()
Entry(root, textvariable=retrieve_roll_no_var).grid(row=len(subjects_list)+6, column=3)
Button(root, text="Retrieve Details", command=retrieve_student_details).grid(row=len(subjects_list)+7, column=3)

# Dictionary to store student data
student_data = {}

root.mainloop()
