# Student Grade Manager 📚

A professional-grade Python application for managing student records and grades with comprehensive analytics and reporting capabilities.

## ✨ Features

### Core Features
- **Student Management**
  - Add, view, update, and delete student records
  - Search students by ID or name
  - Store student information securely in JSON files
  - Track student status and enrollment date

- **Grade Management**
  - Add and manage grades for multiple subjects
  - Automatic letter grade conversion (A-F)
  - GPA calculation (0.0-4.0 scale)
  - Edit and remove grades as needed

- **Analytics & Reporting**
  - Class-wide statistics (average, median, standard deviation)
  - Grade distribution analysis
  - Individual student performance tracking
  - Top performers identification
  - At-risk students identification

- **Data Export**
  - Export student data to CSV
  - Export grades and statistics to CSV
  - Easy integration with spreadsheet applications

### Advanced Features
- Subject-specific statistics
- Historical grade tracking with timestamps
- Data persistence with JSON storage
- Input validation and error handling
- User-friendly CLI interface
- Comprehensive statistical analysis

## 🔧 System Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library)

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/programmingpioneer/ProgrammingPioneer.git
cd student_grade_manager
```

2. Run the application:
```bash
python main.py
```

## 🚀 Usage

### Starting the Application

```bash
python main.py
```

### Menu Options

#### 1️⃣ Add New Student
- Enter unique student ID
- Enter student's first and last name
- Enter email address
- Student is automatically saved

**Example:**
```
Enter Student ID: STU001
Enter First Name: John
Enter Last Name: Doe
Enter Email: john.doe@school.edu
```

#### 2️⃣ View All Students
- Displays a formatted table of all registered students
- Shows ID, name, and email
- Useful for reviewing entire student roster

#### 3️⃣ Add Grade
- Select a student by ID
- Enter subject name
- Enter grade (0-100)
- Grade is automatically converted to letter grade

**Example:**
```
Enter Student ID: STU001
Enter Subject: Mathematics
Enter Grade: 85
```

#### 4️⃣ View Student Grades
- Enter student ID
- Displays all grades for that student
- Shows subject, grade, letter grade, and GPA
- Displays average across all subjects

#### 5️⃣ View Class Statistics
- Shows class-wide metrics:
  - Total students
  - Class average
  - Highest/lowest grades
  - Standard deviation
  - Median grade
  - Grade distribution histogram

#### 6️⃣ Search Student
- Search by student ID or name
- Case-insensitive search
- Displays all matching students

#### 7️⃣ Delete Student
- Removes student and all associated grades
- Requires confirmation before deletion

#### 8️⃣ Exit
- Safely closes the application

## 📊 Grade Scale

### Letter Grades
| Letter | Range |
|--------|-------|
| **A** | 90-100 |
| **B** | 80-89 |
| **C** | 70-79 |
| **D** | 60-69 |
| **F** | 0-59 |

### GPA Points
| Grade | GPA Point |
|-------|----------|
| **A** | 4.0 |
| **B** | 3.0 |
| **C** | 2.0 |
| **D** | 1.0 |
| **F** | 0.0 |

## 💾 Data Storage

Data is automatically saved in JSON format:

### `students_data.json`
Stores student information:
```json
{
  "STU001": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@school.edu",
    "date_added": "2024-01-15T10:30:00",
    "status": "active"
  }
}
```

### `grades_data.json`
Stores grade information:
```json
{
  "STU001": {
    "Mathematics": {
      "grade": 85.0,
      "date_added": "2024-01-15T10:35:00",
      "letter_grade": "B"
    }
  }
}
```

## 📁 Project Structure

```
student_grade_manager/
├── main.py                  # Main application and menu
├── student_manager.py       # Student operations
├── grade_manager.py         # Grade operations and analytics
├── utils.py                 # Utility functions
├── __init__.py              # Package initialization
├── requirements.txt         # Dependencies
├── README.md                # Documentation
├── students_data.json       # Student data (auto-generated)
└── grades_data.json         # Grades data (auto-generated)
```

## 🏗️ Architecture

### StudentManager Class
Handles all student-related operations:
- `add_student()` - Add new student
- `get_student()` - Retrieve student by ID
- `get_all_students()` - Get all students
- `delete_student()` - Remove student
- `update_student()` - Modify student info
- `search_students()` - Search by ID or name
- `export_to_csv()` - Export student data

### GradeManager Class
Handles all grade-related operations:
- `add_grade()` - Add grade for student
- `get_student_grades()` - Get all grades for student
- `get_letter_grade()` - Convert numeric to letter
- `get_gpa_point()` - Calculate GPA point
- `get_student_average()` - Calculate average
- `get_class_statistics()` - Class-wide analytics
- `get_top_students()` - Identify top performers
- `get_students_below_threshold()` - Identify at-risk students
- `export_to_csv()` - Export grades data

## 📈 Statistical Analysis

### Calculated Metrics
- **Mean**: Average of all grades
- **Median**: Middle value when grades sorted
- **Standard Deviation**: Measure of grade spread
- **Grade Distribution**: Count of each letter grade
- **Class Average**: Overall class performance
- **Range**: Highest and lowest grades

### Performance Tracking
- Individual student GPA calculation
- Subject-wise performance analysis
- Class-wide benchmarking
- Top performer identification (top 5)
- At-risk student detection (below 70% threshold)

## 🎯 Example Workflow

```python
# 1. Add students
python main.py
# Menu > Option 1 > Add students

# 2. Add grades for subjects
# Menu > Option 3 > Add grades

# 3. View student performance
# Menu > Option 4 > View individual grades

# 4. Analyze class performance
# Menu > Option 5 > View class statistics

# 5. Export data
# Use export functions to generate CSV files
```

## ✅ Best Practices

1. **Regular Backups**: Keep copies of JSON files
2. **Data Validation**: All inputs are validated
3. **Error Handling**: Graceful error messages
4. **User Confirmation**: Confirmations for critical operations
5. **Clear Display**: Formatted output for readability
6. **Data Persistence**: Automatic saving after each operation
7. **Type Hints**: Used throughout for better code clarity

## 🔮 Future Enhancements

Potential features for future versions:
- Database integration (SQLite/MySQL)
- Web interface (Flask/Django)
- Advanced grade trend analysis
- Student transcript generation
- Parent/student portal
- Automated grade calculation
- Assignment weight management
- Advanced permission system
- Email notifications
- Data visualization (charts/graphs)
- Batch import functionality

## 🐛 Troubleshooting

### Data file not found
- Application will automatically create JSON files on first run
- Ensure write permissions in the application directory

### Invalid grade error
- Grades must be between 0 and 100
- Use decimal points for fractional grades (e.g., 85.5)

### Student not found
- Check student ID spelling and capitalization
- Use search function to verify student exists

### Cannot delete student
- Confirm you're using the correct student ID
- Confirm deletion when prompted

## 📝 License

This project is open source and available for educational use.

## 👤 Author

Created by **Programming Pioneer** as a professional student management system for educational institutions.

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

## 📞 Support

For issues or questions, please refer to the documentation or open an issue on GitHub.

---

**Happy Grade Managing!** 📚✏️
