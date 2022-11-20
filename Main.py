import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data()


accepted = accept_var.get()

if accepted == "Accepted":
    # user info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if firstname and lastname:
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combox.get()

        # Course info
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemesters = numsemesters_spinbox.get()

        print("First name: ", firstname, "Last name: ", lastname)
        print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
        print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
        print("Registration status", registration_status)
        print("---------------------------------")

    else:
        tkinter.messagebox.showwarning(
            title="Error", message="First name and last name are required.")
else:
    tkinter.messagebox.showwarning(
        title="Error", message="You have not accepted the terms.")

window = tkinter.Tk()
window.title("Data Entry Form")
