import os

# ---------- FILE NAMES ----------
ADMIN_FILE = "admins.txt"
STUDENT_FILE = "students.txt"
TRAINING_FILE = "training.txt"

# ---------- BASE CLASS ----------
class FileManager:
    def write_data(self, filename, data):
        with open(filename, "a") as file:
            file.write(data + "\n")

    def read_data(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return file.readlines()

    def overwrite_data(self, filename, lines):
        with open(filename, "w") as file:
            file.writelines(lines)


# ---------- ADMINISTRATION MODULE ----------
class Administration(FileManager):
    def add_staff(self):
        staff_id = input("Enter Staff ID: ")
        name = input("Enter Staff Name: ")
        role = input("Enter Role: ")
        self.write_data(ADMIN_FILE, f"{staff_id},{name},{role}")
        print("✅ Staff added successfully.")

    def view_staff(self):
        data = self.read_data(ADMIN_FILE)
        if not data:
            print("No staff records found.")
            return
        print("\n--- Staff Records ---")
        for line in data:
            staff_id, name, role = line.strip().split(",")
            print(f"ID: {staff_id}, Name: {name}, Role: {role}")

    def delete_staff(self):
        staff_id = input("Enter Staff ID to delete: ")
        lines = self.read_data(ADMIN_FILE)
        new_lines = [line for line in lines if not line.startswith(staff_id + ",")]
        self.overwrite_data(ADMIN_FILE, new_lines)
        print("❌ Staff deleted (if ID existed).")


# ---------- ADMISSION MODULE ----------
class Admission(FileManager):
    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        self.write_data(STUDENT_FILE, f"{student_id},{name},{course}")
        print("✅ Student admitted successfully.")

    def view_students(self):
        data = self.read_data(STUDENT_FILE)
        if not data:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        for line in data:
            student_id, name, course = line.strip().split(",")
            print(f"ID: {student_id}, Name: {name}, Course: {course}")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        lines = self.read_data(STUDENT_FILE)
        new_lines = [line for line in lines if not line.startswith(student_id + ",")]
        self.overwrite_data(STUDENT_FILE, new_lines)
        print("❌ Student record deleted (if ID existed).")


# ---------- TRAINING & PLACEMENT MODULE ----------
class TrainingPlacement(FileManager):
    def add_training(self):
        program_id = input("Enter Program ID: ")
        program_name = input("Enter Program Name: ")
        company = input("Enter Company Name: ")
        self.write_data(TRAINING_FILE, f"{program_id},{program_name},{company}")
        print("✅ Training/Placement record added.")

    def view_training(self):
        data = self.read_data(TRAINING_FILE)
        if not data:
            print("No training records found.")
            return
        print("\n--- Training & Placement Records ---")
        for line in data:
            pid, pname, company = line.strip().split(",")
            print(f"ID: {pid}, Program: {pname}, Company: {company}")

    def delete_training(self):
        program_id = input("Enter Program ID to delete: ")
        lines = self.read_data(TRAINING_FILE)
        new_lines = [line for line in lines if not line.startswith(program_id + ",")]
        self.overwrite_data(TRAINING_FILE, new_lines)
        print("❌ Training record deleted (if ID existed).")


# ---------- MAIN MENU ----------
def main():
    admin = Administration()
    admission = Admission()
    training = TrainingPlacement()

    while True:
        print("\n========== VPN SYSTEM FOR COLLEGE CAMPUS ==========")
        print("1. Administration Operations")
        print("2. Admission Operations")
        print("3. Training & Placement Operations")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Administration Module ---")
            print("1. Add Staff")
            print("2. View Staff")
            print("3. Delete Staff")
            sub = input("Choose option: ")
            if sub == "1":
                admin.add_staff()
            elif sub == "2":
                admin.view_staff()
            elif sub == "3":
                admin.delete_staff()

        elif choice == "2":
            print("\n--- Admission Module ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            sub = input("Choose option: ")
            if sub == "1":
                admission.add_student()
            elif sub == "2":
                admission.view_students()
            elif sub == "3":
                admission.delete_student()

        elif choice == "3":
            print("\n--- Training & Placement Module ---")
            print("1. Add Training")
            print("2. View Training")
            print("3. Delete Training")
            sub = input("Choose option: ")
            if sub == "1":
                training.add_training()
            elif sub == "2":
                training.view_training()
            elif sub == "3":
                training.delete_training()

        elif choice == "4":
            print("🚪 Exiting VPN System. Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    main()
