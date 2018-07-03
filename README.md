# Calculus1
Some tools for inputing grades into pooler.

## inputGrades

Assumes the existence of a file named *students.txt* containing a list of students from pooler with no grades.
e.g.
```
1234567 ------------------ John_Doe grade=
3456789 ------------------ Jane_Doe grade=
 ...
```

### Usage

When run, the script will look for a file named *grades.txt* if it does not exist it will create it, if it does exist the program will prompt you to continue at the last grade added. Input grades and strike enter, if no grade is entered the grade will be recorded as 10.
