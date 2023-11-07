[![Python CI](https://github.com/software-students-fall2023/3-python-package-exercise-random-seed-2/actions/workflows/python-package.yml/badge.svg?branch=lara)](https://github.com/software-students-fall2023/3-python-package-exercise-random-seed-2/actions/workflows/python-package.yml)

# Python Package Exercise

The Math RandomSeed Python package is a lightweight library designed to bring a bit of fun to math operations. With simple addition, subtraction, multiplication, division functions and quirky mathematical facts, the package is both entertaining and auxiliary. The project follows conventional software engineering practices with testing, proper packaging, and clear instructions for easy distribution.
documentation for all functions

## Group Members 
[Lara Kim](https://github.com/larahynkim) <br>
[Andrew Huang](https://github.com/andrewhuanggg) <br>
[Ahmed Omar](https://github.com/ahmed-o-324) <br>
[Henry Wang](https://github.com/fishlesswater) <br>

## Documentations of functions
1. add(x, y):<br>
Adds two numbers together.
2. subtract(x, y):<br>
Subtracts the second number from the first.
3. multiply(x, y):<br>
Multiplies two numbers.
4. divide(x, y):<br>
Divides the first number by the second. Raises a ValueError for division by zero.
5. get_math_fact():<br>
Returns a fun math fact as a string.
<br>
See [examples](./example.py) for the details of using them.

## Python Package Link
https://pypi.org/project/math-randomseed/0.1.3/

## Setting up Virtual Env, Installing Dependencies, and Building and Testing 

1. Install `pipenv`
```
pip install pipenv 
```

2. Install all dependencies from `Pipfile.lock`
```
pipenv --python $(which python3) install
```
If you are using powershell:
```
pipenv --python $(where.exe python3) install
```

3. Activate the virtual environment
```
pipenv shell 
```

4. Install the package
```
pipenv install -e . 
```

5. Run tests
```
pip install -U pytest

pytest
```
If the pytest shows ImportError, try to install python 3.8 and start from beginning

6. Run example program
```
python3 example.py
```

