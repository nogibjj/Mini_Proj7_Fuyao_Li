# User_guide

### Author: Fuyao Li

## Overview
This project involves creating a command-line interface (CLI) tool packaged with Python's setuptools. The tool automates interactions with a database, allowing users to execute specific functions, such as querying or modifying data, directly from the command line. It includes essential dependencies for handling SQL connections, environment variable management, and data processing, making it a powerful and flexible utility for managing data-driven tasks efficiently.

## Set up
1. Clone the repository:
``` shell
git clone git@github.com:nogibjj/Mini_Proj7_Fuyao_Li.git
```
2. Install required packages
``` shell
pip install -r requirements.txt
```

## Install 
```shell
python setup.py develop
```

## Usage
Once installed, you can use `proj7_sql` from the command line. The basic syntax is:
```shell
proj7_sql <action> [<args>] 
```

### Actions
1. Extract
```shell
proj7_sql extract
```
![extract](img/extract.png)

2. Load
```shell
proj7_sql load
```
![load](img/load.png)

3. Insert
```shell
proj7_sql insert 10/30/2016 "Durham, NC" Durham NC 35.99 78.89
```
![insert](img/insert.png)


4. Update
```shell
proj7_sql update Durham 10/30/2022
```
![update](img/update.png)


5. Delete
```shell
proj7_sql delete Manchester
```
![delete](img/delete.png)
