# Automation-testing
This Python script automates the login process for the Quantum University Management System (QUMS) using Selenium WebDriver.

✅ Features
Opens the QUMS login page using Microsoft Edge.

Automatically enters:

Q-ID (username)

Password

Pauses for manual Captcha input.

Logs in after Captcha is entered.

Navigates to the Dashboard.

Clicks on "Today's Attendance" button.

Scrolls to the attendance section for visibility.

🚀 How It Works
Launches the Edge browser.

Opens the QUMS website.

Maximizes the browser window.

Inputs login credentials.

Waits for manual Captcha entry.

Submits the login form.

Navigates to the dashboard and fetches attendance.

🔧 Requirements
Python

Selenium

Microsoft Edge WebDriver (compatible with your Edge version)

📌 Note
⚠️ Captcha needs to be entered manually — the script waits 10 seconds before and after Captcha input for this reason.
