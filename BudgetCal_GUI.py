import tkinter as tk
import pyinputplus as pyip


def calculate_remaining_salary():
    try:
        this_month_salary = float(salary_entry.get())
        rent_or_mortgage = float(rent_entry.get())
        food = float(food_entry.get())

        car_payments = car_payments_var.get()
        if car_payments == 1:
            car_payment = float(car_payment_entry.get())
            car_insurance = float(car_insurance_entry.get())
        else:
            car_payment = 0.0
            car_insurance = 0.0

        entertainment = float(entertainment_entry.get())
        other_expenses = float(other_expenses_entry.get())
        family_support = float(family_support_entry.get())

        total_expenses = (
            rent_or_mortgage +
            food +
            car_payment +
            car_insurance +
            entertainment +
            family_support +
            other_expenses
        )

        remaining_salary = this_month_salary - total_expenses
        remaining_salary_label.config(text=f"Remaining Salary: ${remaining_salary:.2f}", fg='red')

    except ValueError:
        remaining_salary_label.config(text="Invalid input. Please enter numeric values.", fg='black')


# Create the main window
window = tk.Tk()
window.title("Salary and Expenses Calculator")
window.geometry("300x350")  # Set the window size

# Center the window title
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage())  # Remove the default window icon

# Customize the title font
title_font = ("Arial", 14, "bold")
title_label = tk.Label(window, text="Salary and Expenses Calculator", font=title_font)
title_label.pack(pady=10)

# Salary Input
salary_label = tk.Label(window, text="Enter this month's salary:")
salary_label.pack()
salary_entry = tk.Entry(window)
salary_entry.pack()

# Expenses Input
expenses_frame = tk.Frame(window)
expenses_frame.pack()

rent_label = tk.Label(expenses_frame, text="Rent/Mortgage:")
rent_label.pack()
rent_entry = tk.Entry(expenses_frame)
rent_entry.pack()

food_label = tk.Label(expenses_frame, text="Food Expenses:")
food_label.pack()
food_entry = tk.Entry(expenses_frame)
food_entry.pack()

car_payments_var = tk.IntVar()
car_payments_label = tk.Label(expenses_frame, text="Car Payments:")
car_payments_label.pack()
car_payments_yes_radio = tk.Radiobutton(expenses_frame, text="Yes", variable=car_payments_var, value=1)
car_payments_yes_radio.pack()
car_payments_no_radio = tk.Radiobutton(expenses_frame, text="No", variable=car_payments_var, value=0)
car_payments_no_radio.pack()

car_payment_label = tk.Label(expenses_frame, text="Car Payment:")
car_payment_label.pack()
car_payment_entry = tk.Entry(expenses_frame)
car_payment_entry.pack()

car_insurance_label = tk.Label(expenses_frame, text="Car Insurance:")
car_insurance_label.pack()
car_insurance_entry = tk.Entry(expenses_frame)
car_insurance_entry.pack()

entertainment_label = tk.Label(expenses_frame, text="Entertainment Expenses:")
entertainment_label.pack()
entertainment_entry = tk.Entry(expenses_frame)
entertainment_entry.pack()

family_support_label = tk.Label(expenses_frame, text="Family Support:")
family_support_label.pack()
family_support_entry = tk.Entry(expenses_frame)
family_support_entry.pack()

other_expenses_label = tk.Label(expenses_frame, text="Other Expenses:")
other_expenses_label.pack()
other_expenses_entry = tk.Entry(expenses_frame)
other_expenses_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_remaining_salary, bd=2)
calculate_button.pack(pady=10)

remaining_salary_label = tk.Label(window, text="Remaining Salary:", font=("Arial", 12, "bold"), fg="black")
remaining_salary_label.pack()

# Start the GUI event loop
window.mainloop()
