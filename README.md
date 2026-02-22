# Python Auth System

A **secure and minimal authentication system** built with **Python**, **MySQL**, and **bcrypt**.  
Supports **user registration** and **login** with **hashed password storage**.  
The system is **CLI-based** and automatically initializes the database and table if they do not exist.

---

## Table of Contents

- [Features](#features)  
- [Technologies](#technologies)  
- [Installation](#installation)  

---

## Features

- User registration with **unique usernames**  
- Secure password storage using **bcrypt hashing**  
- User login with password verification  
- CLI-based interactive menu  
- Automatic database and table creation  
- Protection against SQL injection via **parameterized queries**  

---

## Technologies

- **Python 3.x** – core programming language  
- **MySQL** – relational database management system  
- **bcrypt** – password hashing library for Python  
- **mysql-connector-python** – Python library to connect to MySQL  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/idkauantrindade/python-auth-system.git
```
2. Install the package

```bash
pip install mysql-connector-python bcrypt
```
