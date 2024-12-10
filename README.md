# EECS-510-Final-Project
> Checkmarks and Xs are to show what is already done and what still needs to be clarified or worked on.

# Full Project Documentation
The full formatted [project documentation file](https://github.com/m-riley04/EECS-510-Final-Project/blob/main/EECS%20510%20Final%20Project.pdf) is located in the PDF in the root repo folder. It has all of this documentation and more required for the project.

# Dependencies
- `pillow` 10.3.0 ([docs](https://pillow.readthedocs.io/en/stable/), [PyPi](https://pypi.org/project/pillow/))
- `automathon` 0.0.15 ([GitHub](https://github.com/rohaquinlop/automathon), [PyPi](https://pypi.org/project/automathon/))
- [Graphviz](https://graphviz.org/download/) (optional)

# Building/Running
1. Install dependencies.
2. Navigate to the root directory of the repository
3. Run the following command:
```bash
> python src/main.py
```
You will then be prompted to enter an input string. Enter a string and hit enter.



## Project Description

### Part 1 - Design a Formal Language ✅

The langauge is based on ingredients for pasta dishes, currently just spaghetti pasta with any choice of sauces and or different addons. 

**Language Rules**

For the language to be accepted the first ingredent must be a pasta.Then any other ingredients may follow after or none at all.

Example:
```
A : Spaghetti Pasta
B : Marinara Sauce
C : Garlic
```
Input:
``` 
ABC ✅ - Accepted

ACB ✅ - Accepted

A ✅ - Accepted

CBA ❌ - Rejected
```

### Part 2 - Grammar ✅

### Part 3 - Automaton ❌

### Part 4 - Data Structure ❌

### Part 5 - Testing ❌
