#include <stdio.h>
#include <string.h>

// Maximum number of students
#define MAX_STUDENTS 100

// Structure to hold student information
typedef struct {
    char name[50];
    int marks;
} Student;

// Function declarations
void addStudent(Student students[], int *count);
void displayStudents(Student students[], int count);
void calculateAverage(Student students[], int count);
void searchStudent(Student students[], int count);
void updateMarks(Student students[], int count);
void deleteStudent(Student students[], int *count);

// Main function
int main() {
    Student students[MAX_STUDENTS];
    int count = 0;
    int choice;

    while (1) {
        // Display menu
        printf("\n=== Enhanced Student Marks Management System ===\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Calculate Average Marks\n");
        printf("4. Search Student\n");
        printf("5. Update Marks\n");
        printf("6. Delete Student\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(students, &count);
                break;
            case 2:
                displayStudents(students, count);
                break;
            case 3:
                calculateAverage(students, count);
                break;
            case 4:
                searchStudent(students, count);
                break;
            case 5:
                updateMarks(students, count);
                break;
            case 6:
                deleteStudent(students, &count);
                break;
            case 7:
                printf("Exiting the program. Goodbye!\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
}

// Function to add a student
void addStudent(Student students[], int *count) {
    if (*count >= MAX_STUDENTS) {
        printf("Cannot add more students. Maximum limit reached.\n");
        return;
    }

    printf("Enter student name: ");
    scanf(" %[^\n]", students[*count].name);
    printf("Enter marks: ");
    scanf("%d", &students[*count].marks);
    (*count)++;
    printf("Student added successfully!\n");
}

// Function to display all students
void displayStudents(Student students[], int count) {
    if (count == 0) {
        printf("No students to display.\n");
        return;
    }

    printf("\n=== Student List ===\n");
    int i;
    for (i = 0; i < count; i++) {
        printf("Student %d: Name: %s, Marks: %d\n", i + 1, students[i].name, students[i].marks);
    }
}

// Function to calculate and display the average marks
void calculateAverage(Student students[], int count) {
    if (count == 0) {
        printf("No students available to calculate average.\n");
        return;
    }

    int total = 0;
	int i;
    for (i = 0; i < count; i++) {
        total += students[i].marks;
    }

    float average = (float)total / count;
    printf("The average marks of %d students is: %.2f\n", count, average);
}

// Function to search for a student by name
void searchStudent(Student students[], int count) {
    if (count == 0) {
        printf("No students available to search.\n");
        return;
    }

    char searchName[50];
    printf("Enter the name of the student to search: ");
    scanf(" %[^\n]", searchName);

    for (int i = 0; i < count; i++) {
        if (strcmp(students[i].name, searchName) == 0) {
            printf("Student found: Name: %s, Marks: %d\n", students[i].name, students[i].marks);
            return;
        }
    }

    printf("Student not found.\n");
}

// Function to update marks of a student
void updateMarks(Student students[], int count) {
    if (count == 0) {
        printf("No students available to update marks.\n");
        return;
    }

    char updateName[50];
    printf("Enter the name of the student to update marks: ");
    scanf(" %[^\n]", updateName);

    for (int i = 0; i < count; i++) {
        if (strcmp(students[i].name, updateName) == 0) {
            printf("Current marks of %s: %d\n", students[i].name, students[i].marks);
            printf("Enter new marks: ");
            scanf("%d", &students[i].marks);
            printf("Marks updated successfully!\n");
            return;
        }
    }

    printf("Student not found.\n");
}

// Function to delete a student by name
void deleteStudent(Student students[], int *count) {
    if (*count == 0) {
        printf("No students available to delete.\n");
        return;
    }

    char deleteName[50];
    printf("Enter the name of the student to delete: ");
    scanf(" %[^\n]", deleteName);

    for (int i = 0; i < *count; i++) {
        if (strcmp(students[i].name, deleteName) == 0) {
            // Shift remaining students left
            for (int j = i; j < *count - 1; j++) {
                students[j] = students[j + 1];
            }
            (*count)--;
            printf("Student deleted successfully.\n");
            return;
        }
    }

    printf("Student not found.\n");
}
