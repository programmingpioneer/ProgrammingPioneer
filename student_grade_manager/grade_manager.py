"""
Grade Manager Module - Handles grade operations and analytics
"""

import json
import os
import statistics
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class GradeManager:
    """Manages student grades and grade analytics"""
    
    # Grade scale mapping
    GRADE_SCALE = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }
    
    # GPA points mapping
    GPA_SCALE = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    def __init__(self, data_file: str = "grades_data.json"):
        """
        Initialize GradeManager
        
        Args:
            data_file: Path to JSON file storing grades data
        """
        self.data_file = data_file
        self.grades = self._load_grades()
    
    def _load_grades(self) -> Dict:
        """Load grades from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def _save_grades(self) -> None:
        """Save grades to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.grades, f, indent=4)
    
    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Add a grade for a student
        
        Args:
            student_id: Student identifier
            subject: Subject name
            grade: Grade value (0-100)
        
        Returns:
            True if grade added successfully, False otherwise
        """
        if not (0 <= grade <= 100):
            return False
        
        if student_id not in self.grades:
            self.grades[student_id] = {}
        
        self.grades[student_id][subject] = {
            'grade': grade,
            'date_added': datetime.now().isoformat(),
            'letter_grade': self.get_letter_grade(grade)
        }
        
        self._save_grades()
        return True
    
    def get_student_grades(self, student_id: str) -> Dict[str, float]:
        """
        Get all grades for a student
        
        Args:
            student_id: Student identifier
        
        Returns:
            Dictionary of subjects and their grades
        """
        if student_id not in self.grades:
            return {}
        
        return {
            subject: data['grade']
            for subject, data in self.grades[student_id].items()
        }
    
    def get_letter_grade(self, grade: float) -> str:
        """
        Convert numeric grade to letter grade
        
        Args:
            grade: Numeric grade (0-100)
        
        Returns:
            Letter grade (A-F)
        """
        for letter, (min_score, max_score) in self.GRADE_SCALE.items():
            if min_score <= grade <= max_score:
                return letter
        return 'F'
    
    def get_gpa_point(self, grade: float) -> float:
        """
        Convert numeric grade to GPA point
        
        Args:
            grade: Numeric grade (0-100)
        
        Returns:
            GPA point (0.0-4.0)
        """
        letter = self.get_letter_grade(grade)
        return self.GPA_SCALE.get(letter, 0.0)
    
    def get_student_average(self, student_id: str) -> Optional[float]:
        """
        Calculate average grade for a student
        
        Args:
            student_id: Student identifier
        
        Returns:
            Average grade or None if no grades exist
        """
        grades = self.get_student_grades(student_id)
        
        if not grades:
            return None
        
        return sum(grades.values()) / len(grades)
    
    def get_student_gpa(self, student_id: str) -> Optional[float]:
        """
        Calculate GPA for a student
        
        Args:
            student_id: Student identifier
        
        Returns:
            GPA (0.0-4.0) or None if no grades exist
        """
        grades = self.get_student_grades(student_id)
        
        if not grades:
            return None
        
        gpa_points = [self.get_gpa_point(grade) for grade in grades.values()]
        return sum(gpa_points) / len(gpa_points)
    
    def delete_student_grades(self, student_id: str) -> bool:
        """
        Delete all grades for a student
        
        Args:
            student_id: Student identifier
        
        Returns:
            True if deleted successfully, False otherwise
        """
        if student_id not in self.grades:
            return False
        
        del self.grades[student_id]
        self._save_grades()
        return True
    
    def get_class_statistics(self, students: Dict) -> Dict:
        """
        Calculate class-wide statistics
        
        Args:
            students: Dictionary of all students
        
        Returns:
            Dictionary containing class statistics
        """
        all_grades = []
        grade_by_student = {}
        
        # Collect all grades
        for student_id in students.keys():
            grades = self.get_student_grades(student_id)
            if grades:
                grade_by_student[student_id] = grades
                all_grades.extend(grades.values())
        
        if not all_grades:
            return {}
        
        # Calculate statistics
        total_grades = len(all_grades)
        class_average = sum(all_grades) / total_grades
        highest_grade = max(all_grades)
        lowest_grade = min(all_grades)
        std_dev = statistics.stdev(all_grades) if len(all_grades) > 1 else 0
        median_grade = statistics.median(all_grades)
        
        # Grade distribution
        grade_distribution = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0
        }
        for grade in all_grades:
            letter = self.get_letter_grade(grade)
            grade_distribution[letter] += 1
        
        return {
            'total_students': len(students),
            'total_grades': total_grades,
            'class_average': class_average,
            'highest_grade': highest_grade,
            'lowest_grade': lowest_grade,
            'std_dev': std_dev,
            'median_grade': median_grade,
            'grade_distribution': grade_distribution
        }
    
    def get_top_students(self, students: Dict, limit: int = 5) -> List[Tuple]:
        """
        Get top performing students by average
        
        Args:
            students: Dictionary of all students
            limit: Number of top students to return
        
        Returns:
            List of tuples (student_id, name, average_grade)
        """
        student_averages = []
        
        for student_id, student in students.items():
            average = self.get_student_average(student_id)
            if average is not None:
                name = f"{student['first_name']} {student['last_name']}"
                student_averages.append((student_id, name, average))
        
        # Sort by average grade in descending order
        student_averages.sort(key=lambda x: x[2], reverse=True)
        
        return student_averages[:limit]
    
    def get_students_below_threshold(self, students: Dict, threshold: float = 70.0) -> List[Tuple]:
        """
        Get students with average grade below threshold
        
        Args:
            students: Dictionary of all students
            threshold: Grade threshold
        
        Returns:
            List of tuples (student_id, name, average_grade)
        """
        at_risk_students = []
        
        for student_id, student in students.items():
            average = self.get_student_average(student_id)
            if average is not None and average < threshold:
                name = f"{student['first_name']} {student['last_name']}"
                at_risk_students.append((student_id, name, average))
        
        return at_risk_students
    
    def get_subject_statistics(self, subject: str) -> Dict:
        """
        Get statistics for a specific subject
        
        Args:
            subject: Subject name
        
        Returns:
            Dictionary containing subject statistics
        """
        subject_grades = []
        
        for student_id, grades in self.grades.items():
            if subject in grades:
                subject_grades.append(grades[subject]['grade'])
        
        if not subject_grades:
            return {}
        
        return {
            'subject': subject,
            'count': len(subject_grades),
            'average': sum(subject_grades) / len(subject_grades),
            'highest': max(subject_grades),
            'lowest': min(subject_grades),
            'std_dev': statistics.stdev(subject_grades) if len(subject_grades) > 1 else 0
        }
    
    def export_to_csv(self, students: Dict, filename: str = "grades_export.csv") -> bool:
        """
        Export grades to CSV
        
        Args:
            students: Dictionary of all students
            filename: Output CSV filename
        
        Returns:
            True if exported successfully, False otherwise
        """
        try:
            import csv
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Collect all subjects
                all_subjects = set()
                for student_id in self.grades.keys():
                    all_subjects.update(self.grades[student_id].keys())
                
                all_subjects = sorted(list(all_subjects))
                
                # Write header
                header = ['Student ID', 'Name'] + all_subjects + ['Average', 'GPA']
                writer.writerow(header)
                
                # Write student data
                for student_id, student in students.items():
                    row = [student_id, f"{student['first_name']} {student['last_name']}"]
                    
                    grades = self.get_student_grades(student_id)
                    for subject in all_subjects:
                        row.append(grades.get(subject, '-'))
                    
                    average = self.get_student_average(student_id)
                    gpa = self.get_student_gpa(student_id)
                    
                    row.append(f"{average:.2f}" if average else '-')
                    row.append(f"{gpa:.2f}" if gpa else '-')
                    
                    writer.writerow(row)
            
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {str(e)}")
            return False
