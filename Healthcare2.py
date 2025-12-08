import csv
import os
def generate_token_for_doctor(doctor_name):
    if not os.path.exists("appointments.csv"):
        return 1
    tokens = []

    with open("appointments.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  

        for row in reader:
            if len(row) < 4:
                continue

            token, name, age, doctor, date = row

         if doctor.strip().lower() == doctor_name.lower():
                tokens.append(int(token))

    if not tokens:
        return 1
    return max(tokens) + 1
def get_input(prompt):
    value = input(prompt).strip()
    while value == "":
        print("❌ This field cannot be empty. Try again.")
        value = input(prompt).strip()
    return value

def create_appointment():
    print("\n---- Create New Appointment ----")

    name = get_input("Enter Patient Name: ")
    age = get_input("Enter Age: ")
    doctor = get_input("Enter Doctor Name: ")
    date = get_input("Enter Appointment Date (DD/MM/YYYY): ")

    
    token = generate_token_for_doctor(doctor)

    file_exists = os.path.isfile("appointments.csv")

    with open("appointments.csv", "a", newline="") as file:
        writer = csv.writer(file)

        
        if not file_exists:
            writer.writerow(["Token", "Name", "Age", "Doctor", "Date"])

        writer.writerow([token, name, age, doctor, date])

    print("\n✅ Appointment Added Successfully!")
    print(f"🎟 Token Number for Dr. {doctor}: {token}")



create_appointment()

