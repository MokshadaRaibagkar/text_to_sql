# Text-to-SQL Application

This application allows users to convert natural language queries into SQL queries. It leverages advanced natural language processing (NLP) and machine learning techniques to understand and translate user inputs into SQL code. The app is designed to make interacting with databases easier for people who may not be familiar with SQL.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

---

## About

The **Text-to-SQL** application translates natural language text into SQL queries, allowing users to easily interact with databases without needing to learn SQL syntax. Users simply type in a query in plain English (or other supported languages), and the app generates the corresponding SQL query.

This app is perfect for:
- Beginners learning SQL
- Non-technical users needing to interact with databases
- Automation of simple SQL query generation

---

## Features

- Converts user input (in plain English) into SQL queries.
- Supports basic SQL operations (SELECT, INSERT, UPDATE, DELETE).
- Provides an intuitive and user-friendly interface.
- Built using Python and various NLP libraries.

---

## Installation

To run the app locally, follow these steps:

### Prerequisites

- Python 3.10
- pip (Python package manager)
- Git

### Steps

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/MokshadaRaibagkar/text_to_sql.git
    ```

2. Navigate to the project directory:

    ```bash
    cd text-to-sql
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   - **Windows:**
   
     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux:**
   
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Running the Application

After installation, you can run the application locally by using the following command:

```bash
streamlit run app.py
