"""
Student Grade Manager - Main Application
A professional-grade system for managing student grades and academic records.
"""

from student_manager import StudentManager
from grade_manager import GradeManager
from utils import display_menu, clear_screen, print_header


def main():
    """Main application loop"""
    student_manager = StudentManager()
    grade_manager = GradeManager()
    
    while True:
        clear_screen()
        print_header("Student Grade Manager")
        display_menu()
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            add_student(student_manager)
        elif choice == '2':
            view_all_students(student_manager)
        elif choice == '3':
            add_grade(student_manager, grade_manager)
        elif choice == '4':
            view_student_grades(student_manager, grade_manager)
        elif choice == '5':
            view_class_statistics(student_manager, grade_manager)
        elif choice == '6':
            search_student(student_manager)
        elif choice == '7':
            delete_student(student_manager, grade_manager)
        elif choice == '8':
            print("\n✓ Thank you for using Student Grade Manager. Goodbye!")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 8.")
        
        input("\nPress Enter to continue...")


def add_student(student_manager):
    """Add a new student to the system"""
    clear_screen()
    print_header("Add New Student")
    
    try:
        student_id = input("Enter Student ID: ").strip()
        if not student_id:
            print("✗ Student ID cannot be empty.")
            return
        
        if student_manager.get_student(student_id):
            print(f"✗ Student with ID {student_id} already exists.")
            return
        
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        email = input("Enter Email: ").strip()
        
        if not all([first_name, last_name, email]):
            print("✗ All fields are required.")
            return
        
        student_manager.add_student(student_id, first_name, last_name, email)
        print(f"✓ Student {first_name} {last_name} added successfully!")
    
    except Exception as e:
        print(f"✗ Error adding student: {str(e)}")


def view_all_students(student_manager):
    """Display all students in the system"""
    clear_screen()
    print_header("All Students")
    
    students = student_manager.get_all_students()
    
    if not students:
        print("No students found in the system.")
        return
    
    print(f"\n{'ID':<12} {'Name':<30} {'Email':<35}")
    print("-" * 80)
    
    for student_id, student in students.items():
        name = f"{student['first_name']} {student['last_name']}"
        print(f"{student_id:<12} {name:<30} {student['email']:<35}")


def add_grade(student_manager, grade_manager):
    """Add a grade for a student"""
    clear_screen()
    print_header("Add Grade")
    
    try:
        student_id = input("Enter Student ID: ").strip()
        student = student_manager.get_student(student_id)
        
        if not student:
            print(f"✗ Student with ID {student_id} not found.")
            return
        
        subject = input("Enter Subject: ").strip()
        if not subject:
            print("✗ Subject cannot be empty.")
            return
        
        try:
            grade = float(input("Enter Grade (0-100): ").strip())
            if not 0 <= grade <= 100:
                print("✗ Grade must be between 0 and 100.")
                return
        except ValueError:
            print("✗ Invalid grade. Please enter a number.")
            return
        
        grade_manager.add_grade(student_id, subject, grade)
        print(f"✓ Grade added successfully for {student['first_name']} {student['last_name']}!")
    
    except Exception as e:
        print(f"✗ Error adding grade: {str(e)}")


def view_student_grades(student_manager, grade_manager):
    """Display grades for a specific student"""
    clear_screen()
    print_header("Student Grades")
    
    try:
        student_id = input("Enter Student ID: ").strip()
        student = student_manager.get_student(student_id)
        
        if not student:
            print(f"✗ Student with ID {student_id} not found.")
            return
        
        grades = grade_manager.get_student_grades(student_id)
        
        if not grades:
            print(f"No grades found for {student['first_name']} {student['last_name']}.")
            return
        
        print(f"\nGrades for {student['first_name']} {student['last_name']}:")
        print(f"\n{'Subject':<20} {'Grade':<10} {'Letter Grade':<15} {'GPA':<10}")
        print("-" * 60)
        
        total_grade = 0
        for subject, grade in grades.items():
            letter_grade = grade_manager.get_letter_grade(grade)
            gpa = grade_manager.get_gpa_point(grade)
            print(f"{subject:<20} {grade:<10.2f} {letter_grade:<15} {gpa:<10.2f}")
            total_grade += grade
        
        average = total_grade / len(grades)
        print("-" * 60)
        print(f"{'Average':<20} {average:<10.2f} {grade_manager.get_letter_grade(average):<15} {grade_manager.get_gpa_point(average):<10.2f}")
    
    except Exception as e:
        print(f"✗ Error retrieving grades: {str(e)}")


def view_class_statistics(student_manager, grade_manager):
    """Display class-wide statistics"""
    clear_screen()
    print_header("Class Statistics")
    
    try:
        stats = grade_manager.get_class_statistics(student_manager.get_all_students())
        
        if not stats:
            print("No grades found in the system.")
            return
        
        print(f"\nClass Statistics:")
        print(f"{'Metric':<20} {'Value':<15}")
        print("-" * 40)
        print(f"{'Total Students':<20} {stats['total_students']:<15}")
        print(f"{'Class Average':<20} {stats['class_average']:<15.2f}")
        print(f"{'Highest Grade':<20} {stats['highest_grade']:<15.2f}")
        print(f"{'Lowest Grade':<20} {stats['lowest_grade']:<15.2f}")
        print(f"{'Standard Deviation':<20} {stats['std_dev']:<15.2f}")
        print(f"{'Median Grade':<20} {stats['median_grade']:<15.2f}")
        
        if stats['grade_distribution']:
            print(f"\n{'Grade Distribution':<20}")
            print("-" * 40)
            for letter, count in stats['grade_distribution'].items():
                percentage = (count / stats['total_grades']) * 100
                bar = "█" * int(percentage / 5)
                print(f"{letter:<20} {count:<5} ({percentage:>5.1f}%) {bar}")
    
    except Exception as e:
        print(f"✗ Error retrieving statistics: {str(e)}")


def search_student(student_manager):
    """Search for a student by ID or name"""
    clear_screen()
    print_header("Search Student")
    
    try:
        search_term = input("Enter Student ID or Name: ").strip().lower()
        
        results = student_manager.search_students(search_term)
        
        if not results:
            print("No students found matching your search.")
            return
        
        print(f"\nFound {len(results)} student(s):")
        print(f"\n{'ID':<12} {'Name':<30} {'Email':<35}")
        print("-" * 80)
        
        for student_id, student in results.items():
            name = f"{student['first_name']} {student['last_name']}"
            print(f"{student_id:<12} {name:<30} {student['email']:<35}")
    
    except Exception as e:
        print(f"✗ Error searching: {str(e)}")


def delete_student(student_manager, grade_manager):
    """Delete a student and their grades"""
    clear_screen()
    print_header("Delete Student")
    
    try:
        student_id = input("Enter Student ID to delete: ").strip()
        student = student_manager.get_student(student_id)
        
        if not student:
            print(f"✗ Student with ID {student_id} not found.")
            return
        
        confirm = input(f"Are you sure you want to delete {student['first_name']} {student['last_name']}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            student_manager.delete_student(student_id)
            grade_manager.delete_student_grades(student_id)
            print(f"✓ Student and all associated grades deleted successfully!")
        else:
            print("✗ Deletion cancelled.")
    
    except Exception as e:
        print(f"✗ Error deleting student: {str(e)}")


if __name__ == "__main__":
    main()
