# terraform-s3-sns-birthday-app
Birthday Reminder Web App built with AWS + Terraform + Docker + Python

# 🎂 AWS Birthday Reminder App

## 📌 Overview
The **AWS Birthday Reminder App** is a Python Flask-based web application that lets users submit their **name**, **email**, and **birthday**.  
The data is stored in **AWS S3**, and users are subscribed to an **AWS SNS** topic to receive email birthday reminders.  
A scheduled script runs daily to check birthdays and send reminder notifications.

---

## 🚀 Features
- 📝 User-friendly web form for entering **name, email, and birthday**
- ☁️ Stores birthday data in **AWS S3 bucket**
- 📩 Automatically subscribes users to **AWS SNS** for notifications
- ⏰ **Daily reminder script** sends birthday wishes at **4 PM IST**
- 🐳 Fully containerized using **Docker**
- ⚙️ Infrastructure provisioned with **Terraform**

---

## 🛠 Tech Stack
| Component       | Technology |
|-----------------|------------|
| Backend         | Python Flask |
| Frontend        | HTML (Flask Templates) |
| Storage         | AWS S3 |
| Notifications   | AWS SNS |
| Hosting         | AWS EC2 |
| Infrastructure  | Terraform |
| Containerization| Docker |

---

## 📂 Project Structure

