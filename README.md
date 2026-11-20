# Lab Exam

A small Python exercise that builds a student's result card from a tuple of details and a list of class marks.

## What `exam_1.py` does

1. Stores one student's details in a tuple: roll number, name, department and mark.
2. Unpacks the tuple into separate variables and prints them.
3. Works out the grade from the mark using `if / elif / else`.
4. Takes a list of eight class marks and prints the highest, the lowest and the class average.
5. Checks whether the student scored more than the class average.
6. Sorts the marks from highest to lowest, prints them, and prints a rank by looking up the value `68` in the sorted list.
7. Takes a list of departments, removes duplicates with a `set`, and prints the unique departments and how many there are.
8. Prints the final result card.

Concepts practised: tuples and unpacking, conditionals, lists (`max`, `min`, `sum`, `len`, `sort`, `index`), sets, and `print` formatting.

## Grade table

| Marks | Grade |
|-------|-------|
| 80 and above | Grade A |
| 60 to 79 | Grade B |
| 40 to 59 | Grade C |
| Below 40 | Fail |
| Anything else (for example a decimal mark such as 79.5) | Invalid |

## How to run

You need Python 3 installed. From the root of this repository:

```bash
python lab_exam/exam_1.py
```

Or from inside the `lab_exam` folder:

```bash
python exam_1.py
```

On some systems the command is `python3` instead of `python`.

## Sample output

```text
---------------------------------
ROLL NO :  108
NAME :  Neha George
DEPARTMENT :  BCom
MARK :  75
---------------------------------
Grade B
---------------------------------
Highest Mark :  91
Lowest Mark :  38
Class Average :  65.0
---------------------------------
Neha George score more than class average
---------------------------------
[91, 86, 72, 68, 65, 60, 40, 38]
Student Rank :  4
---------------------------------
Unique departments :  {'BCom', 'BBA', 'BCA'}
Length of unique departments :  3
---------------------------------
====================
----Reslut Card----
NAME :  Neha George
ROLL NO :  108
DEPARTMENT :  BCom
MARK :  75
GRADE :  Grade B
====================
```

The order of the departments in the set line can differ between runs, because Python sets are unordered.
