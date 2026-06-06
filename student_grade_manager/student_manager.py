"""
Student Manager Module - Handles student data operations
"""

import json
import os
from datetime import datetime
from typing import Dict, Optional, List


class StudentManager:
    """Manages student records and operations"""
    
    def __init__(self, data_file: str = "students_data.json"):
        """
        Initialize StudentManager
        
        Args:
            data_file: Path to JSON file storing student data
        """
        self.data_file = data_file
        self.students = self._load_students()
    
    def _load_students(self) -> Dict:
        """Load students from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def _save_students(self) -> None:
        """Save students to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.students, f, indent=4)
    
    def add_student(self, student_id: str, first_name: str, last_name: str, email: str) -> bool:
        """
        Add a new student
        
        Args:
            student_id: Unique identifier for the student
            first_name: Student's first name
            last_name: Student's last name
            email: Student's email address
        
        Returns:
            True if student added successfully, False otherwise
        """
        if student_id in self.students:
            return False
        
        self.students[student_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'date_added': datetime.now().isoformat(),
            'status': 'active'
        }
        
        self._save_students()
        return True
    
    def get_student(self, student_id: str) -> Optional[Dict]:
        """
        Get a student by ID
        
        Args:
            student_id: The student's ID
        
        Returns:
            Student dictionary or None if not found
        """
        return self.students.get(student_id)
    
    def get_all_students(self) -> Dict:
        """
        Get all students
        
        Returns:
            Dictionary of all students
        """
        return self.students.copy()
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student
        
        Args:
            student_id: The student's ID
        
        Returns:
            True if deleted successfully, False otherwise
        """
        if student_id not in self.students:
            return False
        
        del self.students[student_id]
        self._save_students()
        return True
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        Update student information
        
        Args:
            student_id: The student's ID
            **kwargs: Fields to update
        
        Returns:
            True if updated successfully, False otherwise
        """
        if student_id not in self.students:
            return False
        
        allowed_fields = {'first_name', 'last_name', 'email', 'status'}
        for key, value in kwargs.items():
            if key in allowed_fields:
                self.students[student_id][key] = value
        
        self._save_students()
        return True
    
    def search_students(self, search_term: str) -> Dict:
        """
        Search for students by ID or name
        
        Args:
            search_term: Search term (case-insensitive)
        
        Returns:
            Dictionary of matching students
        """
        search_term = search_term.lower()
        results = {}
        
        for student_id, student in self.students.items():
            if (search_term in student_id.lower() or
                search_term in student['first_name'].lower() or
                search_term in student['last_name'].lower()):
                results[student_id] = student
        
        return results
    
    def get_student_count(self) -> int:
        """Get total number of students"""
        return len(self.students)
    
    def get_active_students(self) -> Dict:
        """Get all active students"""
        return {
            sid: s for sid, s in self.students.items()
            if s.get('status') == 'active'
        }
    
    def export_to_csv(self, filename: str = "students_export.csv") -> bool:
        """
        Export student data to CSV
        
        Args:
            filename: Output CSV filename
        
        Returns:
            True if exported successfully, False otherwise
        """
        try:
            import csv
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Student ID', 'First Name', 'Last Name', 'Email', 'Status', 'Date Added'])
                
                for student_id, student in self.students.items():
                    writer.writerow([
                        student_id,
                        student['first_name'],
                        student['last_name'],
                        student['email'],
                        student.get('status', 'active'),
                        student.get('date_added', '')
                    ])
            
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {str(e)}")
            return False
