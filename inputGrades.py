#! /usr/local/bin/python3

import re, sys


class Grades:
    ''' A program to input grades into pooler.'''

    def __init__(self):
        try:
            with open('students.txt', 'r') as f:
                self.grades = {}
                for i in f.readlines():
                    id_num = re.match('^\d+', i)
                    id_num = id_num.group()
                    name = re.search(r' (\w+) \w+=$', i)
                    name = name.group(1).split('_')
                    name = (name[0], name[1])
                    self.grades[id_num] = [name, i.rstrip()]
                f.close()
        except FileNotFoundError:
            print('No students file found. It  must be in the curren directory and named students.txt.')
            sys.exit()
        self.graded = []
        try:
            self.output = open('grades.txt', 'x')
        except FileExistsError:
            print('File exists, appending grades...')
            with open('grades.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    key = re.match('^\d+', line)
                    self.graded.append(key.group())

    def save(self, student, grade):
            self.output = open('grades.txt', 'a')
            self.output.write(self.grades[student][1] + grade + '\n')
            self.output.close()


    def grade(self):
        for student in self.grades.keys():
            if not (student in self.graded): 
                try:
                    grade = input(self.grades[student][0][1]+ ' ' + self.grades[student][0][0] + ' grade : ')
                    if grade == '':
                        self.save(student, '10')
                    else:
                        self.save(student,grade)
                except KeyboardInterrupt:
                    print('\nSaving and quitting...')
                    break


if __name__ == '__main__':
    g = Grades()
    g.grade()
