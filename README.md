# 🎓 HSTU Student Complaint Management System

**🔴 Live Demo:** [https://student-complaint-management-system2.onrender.com](https://student-complaint-management-system2.onrender.com)

A comprehensive, web-based complaint management portal designed specifically for the students of **Hajee Mohammad Danesh Science and Technology University (HSTU)**. This platform bridges the gap between students and the administration by providing a streamlined, transparent way to report and track academic, residential, or administrative issues.

---

## ✨ Features & Sub-Features

### 👨‍🎓 Student Portal (Public Access)
* **Submit Complaints Easily:**
  * Students can submit issues by providing their Full Name, Student ID, Department (via dropdown), and a detailed description.
* **Automated Tracking ID Generation:**
  * Upon successful submission, the system auto-generates a unique alphanumeric tracking ID (e.g., `HSTU-A1B2C3`) for the user.
* **Real-time Status Tracking:**
  * Students can search for their complaint using their Tracking ID.
  * Displays real-time status updates: 🟡 **Pending**, 🔵 **In Progress**, or 🟢 **Resolved**.
* **Admin Feedback Visibility:**
  * Students can read detailed responses/feedback left by the administration regarding their specific issue.

### 🛡️ Administrator Portal (Secure Access)
* **Secure Login System:**
  * Protected route to ensure only authorized personnel can access sensitive student data.
* **Centralized Admin Dashboard:**
  * View all submitted complaints in a clean, tabulated format.
  * Complaints are automatically sorted by the most recent submission first.
* **Complaint Management & Updates:**
  * Update the status of any complaint via a dropdown menu.
  * Add or edit written responses/feedback to communicate directly with the student.
  * One-click "Update Status" button for seamless workflow.

---

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **Database:** SQLite (Local Development) / PostgreSQL (Production via Render)
* **ORM:** Flask-SQLAlchemy
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
* **Typography:** Google Fonts (Poppins)
* **Deployment:** Render Cloud Hosting (Gunicorn)

---

## 🚀 Local Installation & Setup

Follow these steps to run the project on your local machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/hstu-complaint-system.git](https://github.com/yourusername/hstu-complaint-system.git)
cd hstu-complaint-system
