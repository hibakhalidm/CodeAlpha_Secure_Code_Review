### Files and Directories

- **`README.md`**: This file. It provides an overview of the project, setup instructions, and a summary of the findings.

- **`app/`**: Contains the source code of the Flask web application.
    - **`app.py`**: The main application file containing the Flask app with intentionally vulnerable code.
    - **`templates/`**: Directory for HTML templates used by the app.
        - **`user_profile.html`**: An HTML template demonstrating secure rendering practices.
    - **`setup_db.py`**: Script to set up a SQLite database with sample data.

- **`requirements.txt`**: Lists the Python dependencies needed to run the application. Install these with:
  ```bash
  pip install -r requirements.txt
  ```

- **`docs/`**: Contains additional documentation related to the secure coding review.
    - **`review_report.md`**: Detailed report of the vulnerabilities found, descriptions, impacts, and recommended fixes.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hibakhalidm/CodeAlpha_Secure_Coding_Review.git
   cd CodeAlpha_Secure_Coding_Review
   ```

2. **Install dependencies:**
   Make sure Python is installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   Initialize the SQLite database with:
   ```bash
   python app/setup_db.py
   ```

4. **Run the application:**
   Start the Flask application using:
   ```bash
   python app/app.py
   ```

   The app will be accessible at `http://localhost:5000`.

## Findings Summary

This project identified several key vulnerabilities:

1. **SQL Injection**:
    - **Issue**: Direct concatenation of user input into SQL queries.
    - **Solution**: Use parameterized queries to prevent injection attacks.

2. **Cross-Site Scripting (XSS)**:
    - **Issue**: Unsanitized user input rendered directly.
    - **Solution**: Use Flask’s templating engine for automatic input escaping.

3. **Insecure Password Storage**:
    - **Issue**: Plaintext password storage in the database.
    - **Solution**: Store passwords using secure hash functions, such as bcrypt.

For detailed information, see the `review_report.md` in the `docs/` directory.

## Conclusion

By following the recommendations and applying secure coding practices, the security posture of the application has been significantly improved. This repository serves as a learning resource for understanding secure coding techniques in the context of web applications.

---
