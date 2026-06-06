"""
Utility functions for the Student Grade Manager
"""

import os
import sys


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str):
    """
    Print a formatted header
    
    Args:
        title: Title to display
    """
    width = 80
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def display_menu():
    """Display the main menu"""
    menu = """
    ┌─ MAIN MENU ─────────────────────────────────────────────┐
    │ 1. Add New Student                                      │
    │ 2. View All Students                                    │
    │ 3. Add Grade                                            │
    │ 4. View Student Grades                                  │
    │ 5. View Class Statistics                                │
    │ 6. Search Student                                       │
    │ 7. Delete Student                                       │
    │ 8. Exit                                                 │
    └─────────────────────────────────────────────────────────┘
    """
    print(menu)


def print_separator(width: int = 80):
    """Print a separator line"""
    print("-" * width)


def format_grade(grade: float) -> str:
    """
    Format a grade value
    
    Args:
        grade: Numeric grade
    
    Returns:
        Formatted grade string
    """
    return f"{grade:.2f}"


def validate_email(email: str) -> bool:
    """
    Validate email format
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_student_id(student_id: str) -> bool:
    """
    Validate student ID format
    
    Args:
        student_id: Student ID to validate
    
    Returns:
        True if valid, False otherwise
    """
    return len(student_id.strip()) > 0 and len(student_id.strip()) <= 20


def validate_name(name: str) -> bool:
    """
    Validate name format
    
    Args:
        name: Name to validate
    
    Returns:
        True if valid, False otherwise
    """
    return len(name.strip()) > 0 and len(name.strip()) <= 50


def get_yes_no_input(prompt: str) -> bool:
    """
    Get yes/no input from user
    
    Args:
        prompt: Prompt to display
    
    Returns:
        True for yes, False for no
    """
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def get_float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """
    Get float input from user with validation
    
    Args:
        prompt: Prompt to display
        min_val: Minimum allowed value
        max_val: Maximum allowed value
    
    Returns:
        Valid float input
    """
    while True:
        try:
            value = float(input(prompt).strip())
            
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_int_input(prompt: str) -> int:
    """
    Get positive integer input from user
    
    Args:
        prompt: Prompt to display
    
    Returns:
        Valid positive integer
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_success_message(message: str):
    """Print a success message"""
    print(f"\n✓ {message}")


def print_error_message(message: str):
    """Print an error message"""
    print(f"\n✗ {message}")


def print_info_message(message: str):
    """Print an info message"""
    print(f"\nℹ {message}")


def print_warning_message(message: str):
    """Print a warning message"""
    print(f"\n⚠ {message}")
