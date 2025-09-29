# Project Report: Simple Linear Regression Streamlit App

This report details the development process of converting a simple linear regression script into an interactive Streamlit application, including all steps taken and modifications made.

## Project Overview

This project started with a basic Python script (`app.py`) that performed simple linear regression, generated data with noise, trained a model, evaluated it, and visualized the results using `matplotlib`. The primary goal was to transform this script into a dynamic Streamlit web application, allowing users to interactively adjust key parameters for data generation and observe their impact on the regression model and its visualization. Additionally, features like dependency management, logging, and Git integration were implemented.

## Development Log

Below is a detailed log of the development process, outlining each task and sub-task performed:

### Task 1: Initial Setup

*   **1.1. `GEMINI.md` Creation:** Analyzed the directory and created a `GEMINI.md` file with a template for a code project to provide context for future interactions.
*   **1.2. `log.md` Creation:** Created this `log.md` file to record all subsequent actions.
*   **1.3. Log Format Update:** Updated the log format to use a `global_task.local_task` structure as requested.

### Task 2: Logging Convention

*   **2.1. Append for Logging:** Noted the instruction to append to the log file for future entries. To do this, I will read the file, append new content, and write the entire file back.

### Task 3: Running `app.py`

*   **3.1. Attempt to Run `app.py`:** Executed `python app.py` as requested by the user. The script failed with an `ImportError`.
*   **3.2. Identify Missing Dependencies:** Read `app.py` and identified `numpy`, `matplotlib`, and `scikit-learn` as likely missing dependencies causing the `ImportError`.
*   **3.3. Install Dependencies:** Executed `pip install numpy matplotlib scikit-learn` as instructed by the user. The installation completed successfully.
*   **3.4. Second Attempt to Run `app.py`:** Executed `python app.py` again. The script ran and produced output, but then failed with a `UnicodeEncodeError` when printing the R² value.
*   **3.5. Fix UnicodeEncodeError:** Modified `app.py` to replace the `R²` symbol with `R-squared` in the print statement to avoid the `UnicodeEncodeError`.
*   **3.6. Successful Execution of `app.py`:** Executed `python app.py` again. The script ran successfully, printed the output, and displayed the plot.

### Task 4: Managing Dependencies

*   **4.1. Create `requirements.txt`:** Created a `requirements.txt` file containing the identified dependencies (`numpy`, `matplotlib`, `scikit-learn`).

### Task 5: Streamlit Conversion

*   **5.1. Plan Streamlit Conversion:** User requested to convert `app.py` to a Streamlit application, allowing user input for `n`, `a`, and `var`.
*   **5.2. Install Streamlit:** Installed the `streamlit` library using `pip`.
*   **5.3. Create `streamlit_app.py`:** Created `streamlit_app.py` with the Streamlit application code, incorporating user input for `n`, `a`, and `var`.
*   **5.4. Run `streamlit_app.py`:** Executed `streamlit run streamlit_app.py` in the background. The Streamlit application should now be running.
*   **5.5. Rerun Streamlit App:** User reported inability to access the address and requested to kill the original process and rerun `streamlit_app.py`.
*   **5.6. Attempt to Kill and Rerun Streamlit:** Attempted to find and kill the previous Streamlit process (no active `python.exe` processes found). Now re-running `streamlit_app.py` without the background flag.
*   **5.7. Second Rerun of Streamlit App:** Executed `streamlit run streamlit_app.py` in the foreground. The app is running and displaying an email prompt in the terminal.
*   **5.8. Third Rerun of Streamlit App:** Executed `streamlit run streamlit_app.py` again as requested by the user.
*   **5.9. Fourth Rerun of Streamlit App:** Executed `streamlit run streamlit_app.py` again as requested by the user. The app is running and displaying an email prompt in the terminal.
*   **5.10. Review `streamlit_app.py`:** User reported inability to access the Streamlit app, so reviewing the code for potential issues.
*   **5.11. Troubleshooting Streamlit Access:** Reviewed `streamlit_app.py` code and found no issues. Provided troubleshooting steps for the user, including checking terminal output for URLs, ensuring no port conflicts, and trying different browsers.
*   **5.12. Fifth Rerun of Streamlit App:** Executed `streamlit run streamlit_app.py` again as requested by the user. The app is running and displaying an email prompt in the terminal.
*   **5.13. Check Streamlit Process Status:** User asked if the Streamlit app is still running. Attempting to verify process status.
*   **5.14. Streamlit Process Not Found:** Checked for processes listening on port 8501 using `netstat`, but no active processes were found. This indicates the Streamlit application is not currently running.
*   **5.15. Run Streamlit with Headless Flag:** Executed `streamlit run streamlit_app.py --server.headless true` as requested by the user.
*   **5.16. Add Intercept (b) Slider:** User requested to add a slider for the intercept `b` with a range of -10 to 10.
*   **5.17. Modified `streamlit_app.py` for Intercept Slider:** Modified `streamlit_app.py` to include a slider for the intercept `b` and updated the data generation and display accordingly.
*   **5.18. Sixth Rerun of Streamlit App (Headless):** Executed `streamlit run streamlit_app.py --server.headless true` again as requested by the user.
*   **5.19. Label Top 5 Outliers:** User requested to label the top 5 outliers in the Streamlit application.
*   **5.20. Modified `streamlit_app.py` for Outlier Labeling:** Modified `streamlit_app.py` to identify and label the top 5 outliers on the plot based on absolute residuals.
*   **5.21. Seventh Rerun of Streamlit App:** Executed `streamlit run streamlit_app.py` again as requested by the user.
*   **5.22. Eighth Rerun of Streamlit App (Headless):** Executed `streamlit run streamlit_app.py --server.headless true` again as requested by the user.

### Task 6: Git Operations

*   **6.1. Push to GitHub:** User requested to push everything to the provided GitHub repository.
*   **6.2. Initialize Git Repository:** Initialized a new Git repository in the current directory.
*   **6.3. Add All Files:** Added all files to the Git staging area.
*   **6.4. Commit Changes:** Committed the staged changes with the message "Initial commit".
*   **6.5. Add Remote Repository:** Added the GitHub remote repository `git@github.com:luphobia/aiot_HW1.git` as 'origin'.
*   **6.6. Failed Push to GitHub:** Attempted to push changes to `origin/master`, but it failed with a "Permission denied (publickey)" error.
*   **6.7. Update GitHub Repository URL:** User provided a new, correct GitHub repository URL.
*   **6.8. Remove Old Remote:** Removed the old remote named 'origin'.
*   **6.9. **Add New Remote:** Added the new GitHub remote repository `https://github.com/luphobia/aiot_HW1.git` as 'origin'.
*   **6.10. Explain Git Push Issue:** Explained that the `git push` command likely failed due to a lack of credentials for the HTTPS remote, as the agent cannot interact with prompts.
*   **6.11. Attempt Git Push (User Initiated):** Executed `git push -u origin master` as requested by the user. This command will likely prompt for credentials.
*   **6.12. Successful Push to GitHub:** The `git push -u origin master` command executed successfully.

### Task 7: Project Reporting

*   **7.1. Generate Project Report:** User requested a detailed project report to be saved to `README.md`.

## Files Created/Modified

*   `app.py`: Original linear regression script (modified to fix Unicode error).
*   `GEMINI.md`: Project context file for the Gemini AI agent.
*   `log.md`: Detailed log of all development steps.
*   `requirements.txt`: Lists Python dependencies (`numpy`, `matplotlib`, `scikit-learn`, `streamlit`).
*   `streamlit_app.py`: The interactive Streamlit application.

## How to Run the Streamlit App

1.  **Install Dependencies:** Ensure you have Python installed. Then, install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the App:** Navigate to the project directory in your terminal and run the Streamlit application:
    ```bash
    streamlit run streamlit_app.py
    ```
    If you prefer not to have a browser tab automatically open, you can use:
    ```bash
    streamlit run streamlit_app.py --server.headless true
    ```
    The application will typically be accessible at `http://localhost:8501` in your web browser.

## GitHub Repository

The project is hosted on GitHub at: [https://github.com/luphobia/aiot_HW1.git](https://github.com/luphobia/aiot_HW1.git)
