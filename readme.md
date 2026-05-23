# 🌐 Website Uptime Monitor

A simple Flask web application that checks whether a website is online and measures how quickly it responds.

---

## 🚀 Features

- Check if a website is online
- Display HTTP status codes
- Measure response time
- Handle invalid URLs
- Browser-like request handling using headers
- Simple and clean Bootstrap UI

---

## 🛠️ Technologies Used

- Python
- Flask
- Requests Library
- HTML
- Bootstrap 5

---

## 📸 What This Project Does

The user enters a website URL, and the application:

1. Sends an HTTP request to the website
2. Measures how long the response takes
3. Checks the HTTP status code
4. Displays whether the site is online, restricted, or has issues

---

## 📂 Project Structure

```bash
uptime-monitor/
│
├── app.py
├── templates/
│   └── index.html
├── .gitignore
└── README.md