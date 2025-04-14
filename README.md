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

### 1. Clone the Repository

```bash
git clone https://github.com/MokshadaRaibagkar/text_to_sql.git
```

### 2. Navigate to the Project Folder

```bash
cd text_to_sql
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

> ⚠️ The `venv/` folder is excluded via `.gitignore`, so make sure to create your own virtual environment before running the app.

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Add Your API Key

This app requires a valid API key (e.g., Google Generative AI).  

1. Create a `.env` file in the root of the project.
2. Add the following line with your actual API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 7. Run the Streamlit App

```bash
streamlit run app.py
```
## Author

**Mokshada Raibagkar**  
[GitHub](https://github.com/MokshadaRaibagkar)