from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------------
# Gemini Function (FIXED)
# -----------------------------
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-flash-latest')

    response = model.generate_content(
        prompt[0] + "\nUser Question: " + question
    )

    sql = response.text.strip()

    # Clean unwanted formatting
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


# -----------------------------
# SQL Execution Function
# -----------------------------
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        cur.execute(sql)
        rows = cur.fetchall()

        columns = [desc[0] for desc in cur.description]

        conn.close()

        return rows, columns

    except Exception as e:
        return str(e), None


# -----------------------------
# Prompt (Improved)
# -----------------------------
prompt = ["""
You are an expert SQL query generator.

Database Name: STUDENT
Columns:
- NAME
- CLASS
- SECTION
- MARKS

Rules:
- Return ONLY SQL query
- No explanation
- No ``` 
- Use correct SQLite syntax
- Column names must match exactly

Examples:

Q: Show all students
A: SELECT * FROM STUDENT;

Q: Students with marks above 80
A: SELECT * FROM STUDENT WHERE MARKS > 80;

Q: Count total students
A: SELECT COUNT(*) FROM STUDENT;

Q: Show students in AIML class
A: SELECT * FROM STUDENT WHERE CLASS = 'AIML';
"""]


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Text to SQL App", layout="centered")

st.title("📊 Text to SQL - Student Database")
st.write("Ask questions in English and get SQL results instantly!")

# Input
question = st.text_input("💬 Enter your question:")

# Button
if st.button("Run Query"):

    if question:
        # Generate SQL
        sql_query = get_gemini_response(question, prompt)

        st.subheader("🧠 Generated SQL:")
        st.code(sql_query, language="sql")

        # Run SQL
        result, columns = read_sql_query(sql_query, "student.db")

        st.subheader("📋 Result:")

        if columns is None:
            st.error(result)
        else:
            df = pd.DataFrame(result, columns=columns)
            st.dataframe(df)

            # 🔥 BONUS: Chart (boost marks)
            if "MARKS" in df.columns:
                st.subheader("📊 Marks Visualization")
                st.bar_chart(df["MARKS"])

    else:
        st.warning("Please enter a question!")