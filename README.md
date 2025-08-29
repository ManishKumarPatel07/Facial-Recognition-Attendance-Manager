# Face Recognition Attendance Manager  

## 📌 Project Overview  
The **Face Recognition Attendance Manager** is a Python-based application that automates the process of marking attendance using facial recognition. Instead of relying on manual roll calls or traditional biometric methods, this system detects and recognizes faces in real time and records attendance efficiently.  

This project leverages **OpenCV, dlib, and face_recognition** libraries to implement facial detection and recognition. Attendance is stored in a CSV file with details like **Name, Date, and Time**.  

---

## ✨ Features  
- ✅ Real-time face detection and recognition using a webcam  
- ✅ Automatic attendance marking in CSV file  
- ✅ User-friendly interface for easy operation  
- ✅ Stores date and time of attendance entry  
- ✅ Ability to add new faces to the dataset  

---

## 🛠️ Technologies Used  
- **Programming Language:** Python 3.10  
- **Libraries & Frameworks:**  
  - OpenCV  
  - dlib  
  - face_recognition  
  - NumPy  
  - Pandas  
- **Database/Storage:** CSV files (Attendance logs)  

---

## 📂 Project Structure  
Face-recognition-Attendance-System/
│── AttendanceProject.py       # Main application script
│── face_recognition.py        # Face recognition logic
│── Images_Attendance/         # Folder containing images of registered users
│── attendance.csv             # Attendance log file



---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/ManishKumarPatel07/Facial-Recognition-Attendance-Manager.git
cd Face-recognition-Attendance-Manager

###2️⃣ Install dependencies
pip install python3 --31011

pip install cmake

pip install dlib face_recognition

###3️⃣ Run the project
python AttendanceProject.py
```

## 🚀 How It Works

- The system uses your **webcam** to capture live video feed.  
- **Faces are detected** and matched against the stored dataset.  
- If a face is recognized, the system **marks attendance** with **Name, Date, and Time** in `attendance.csv`.  
- If a **new face** is found, it can be **added to the dataset** for future recognition.

---

## 📊 Sample Attendance Output

| Name                 | Date       | Time      |
|----------------------|------------|-----------|
| Manish Kumar Patel   | 2025-08-29 | 10:30 AM  |
| Rohit Sharma         | 2025-08-29 | 10:32 AM  |

---

## 📸 Screenshots

> Add screenshots here for better presentation:
- Face detection screen  
- Recognition match screen  
- `attendance.csv` preview

*(Place images in a `/screenshots` folder and reference like: `![Detection](screenshots/detection.png)`)*

---


## 👨‍💻 Author

**Manish Kumar Patel**

