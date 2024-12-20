# Full Project Documentation
The full formatted [project documentation file](https://github.com/m-riley04/EECS-510-Final-Project/blob/main/EECS%20510%20Final%20Project.pdf) is located in the PDF in the root repo folder. It has all of this documentation and more required for the project.

# Dependencies
Project is built on python 3.12.1

- `pillow` 10.3.0 ([docs](https://pillow.readthedocs.io/en/stable/), [PyPi](https://pypi.org/project/pillow/))
- `automathon` 0.0.15 ([GitHub](https://github.com/rohaquinlop/automathon), [PyPi](https://pypi.org/project/automathon/))
- [Graphviz](https://graphviz.org/download/) (optional)

# Building/Running
First, clone the repository to the desired folder and navigate to `/EECS-510-Final-Project/`. After that is complete, follow these next sections to complete setup:

## Virtual Environment Setup
Use of a virtual environment is recommended such as `venv` environment or a Conda environment if installing dependencies is not wanted on the root system. If one does not care about dependencies on their root system, you can skip this section.
### Conda
```bash
> conda create --name myenv python=3.12.1
```
```bash
> conda activate myenv
```
### Venv
```bash
> python -m venv venv
```
activate venv on Mac/Linux:
```bash
> source venv/bin/activate
```
On Windows:
```bash
> venv\Scripts\activate
```

## Installing Dependencies
To install dependencies, you can run one of the following commands depending on your Python setup:
### Conda
```bash
> conda install pillow automathon
```
### venv
```bash
> pip install pillow automathon
```

## Running 
To run our program, execute the following command:
```bash
> python src/main.py
```

You will then be prompted to enter an input string. Enter a string and hit enter. You should see the acceptance result, a path/trace (if accepted), and a formatted recipe (if accepted).

### Alphabet

- A-C : Pastas (Spaghetti, fettuccini, and Macaroni)
- D-F : Sauces (Marina, Alfredo, and Pesto)
- G-J : Addons (Ground meat, Chicken, Olive oil, Garlic, Onions, and Broccoli)
