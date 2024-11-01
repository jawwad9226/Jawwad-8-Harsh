import os
import numpy as np
import csv


# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load CSV data
def load_data(filename='Roll list.csv'):
    """Load data from a CSV file."""
    try:
        return np.genfromtxt(filename, delimiter=',', dtype=str, encoding=None)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
data=load_data()
def search_by_roll_number(data):
    """Search for a student by roll number and return their index and information."""
    roll_number = input('Enter your Roll Number: ').strip()
    for entry in data:
        if str(entry[0]) == roll_number:
            return entry  # Return index and entry
    print("No student found with that roll number.")
    return None
def verify_number():
    """Verify the number format and return True if valid."""
    number = input('Enter your number (10 digits): ')
    if len(number) == 10 and number.isdigit():
        return number
    else:
        print('Invalid Number. Please enter a valid 10-digit number.')
        return None

def verify_email():
    """Verify if the email is a valid Gmail email."""
    email = input('Enter your email: ')
    if email.endswith('@gmail.com'):
        return email
    else:
        print('Not a valid Gmail email. Please enter a valid Gmail address.')
        return None

def update_csv(data, filename='Roll list.csv'):
    """Update the CSV file with the modified data."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print('CSV file updated successfully.')
    except Exception as e:
        print(f"Error updating CSV file: {e}")

def edit_info(entry):       
    action = input(f'Do you want to edit your information \n 1.Your number\n 2.parents Number\n 3.your email\n 4.Your student Id \n 5.Exit:: ::  ').strip().lower()
    if action == '1':
        new_number = verify_number()
        if new_number:
            entry[3] = new_number  # Update the number in the original data
                    #edit_info(data, index, 3)
    if action == '2':
        new_number = verify_number()
        if new_number:
            entry[4] = new_number  # Update the number in the original data
                    #edit_info(data, index, 4)   
    elif action == '3':
        new_email = verify_email()
        if new_email:
            entry[5] = new_email  # Update the email in the original data
                    #edit_info(data, index, 5)
    elif action == '5':
        exit
    else:
        print('Invalid option. Please try again.itis')

    update_csv(data)  # Update CSV after editing
    print('Student Info Chaged')

# Load the data
#data = np.genfromtxt('rikami.csv', delimiter=',', dtype=None, encoding=None)

def print_student_info(entry):
   
    """Print the student information in a formatted manner."""
    print('\n' + '*' * 100)
    print('** PADM. DR. V.B. KOLTE COLLEGE OF ENGINEERING MALKAPUR **'.center(100))
    print('*' * 100)
    print('* Student Information *'.center(100))
    print('** BE Second Year' + '-' * 45 + 'Computer Science Engineering Branch **')
    print('**' + ' ' * 96 + '**')
    print(f'** Student Name: {entry[2]:<30} '+ ' '*(80-len(entry[2]))+'**')
    print(f'** Roll Number: {entry[0]:<31} ** Enrollment Number: {entry[1]:<27} **')
    print(f'** Student Contact Number: {entry[3]:<20} ** Parent\'s Contact Number: {entry[4]:<21} **')
    print(f'** Student Email: {entry[5]:<30} ** Student ID: {entry[6]:<30} **')
    print('**' + ' ' * 96 + '**')
    print('*' * 100)
    print('** End of Student Information **'.center(100))
    print('*' * 100 + '\n')
    print('Done')
    if entry[3]=='N.A.' or entry[4]=='N.A.' or entry[5]=='N.A.' or entry[6]=='N.A.':
        edit_info(data)


def search_by_name(data):
    """Search for a student by name and print their information."""
    name = input('Enter what to search: ').strip().lower()
    
    for entry in data:
        if name in str(entry[2]).lower():  # Convert entry[2] to string before comparing
            print_student_info(entry)  # Pass the whole entry
            return  # Exit after finding the first match
            
    print("No student found with that name.")

def search_by_phone(data):
    """Search for a student by phone number and print their information."""
    phone = input('Enter the Phone Number: ').strip()
    for entry in data:
        if phone in str(entry[3]) or phone in str(entry[4]):  # Convert entry[3] and entry[4] to string before comparing
            print_student_info(entry)  # Pass the whole entry
            return
    print("No student found with that number.")

def edit(entry,column):
    if entry[column]=='N.A':
        entry[column]=input('Enter the value: ')
    else:
        print('You Are Not Autherize to Edit The Info')
        return
def search():
    print("1. Search by Name")
    print("2. Search by Phone Number")
    print("3. Search by Roll Number")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        search_by_name(data)
    elif choice == '2':
        search_by_phone(data)
    elif choice == '3':
        entry=search_by_roll_number(data)
        print_student_info(entry)
    elif choice == '4':
        print("Exiting the program.")
        exit
    else:
        print("Invalid choice. Please try again.")
def main():
    """Main function to run the student information system."""
    os.system('cls')
    while True:
        choice=input('Enter 5the choice ')    
    
        if choice=='1':
            search()
        elif choice=='2':
          edit_info(data)
if __name__ == "__main__":
    main()