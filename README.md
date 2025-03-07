# 🛡️ Intrusion Detection System (IDS) Simulator  

An interactive simulator designed to detect and visualize network intrusions using **pattern matching** and **graph algorithms**. This tool provides insights into different types of cyber threats and enables efficient monitoring of network traffic.

---

## 🚀 Features  
- **Intrusion Detection**: Identifies threats like `PORT_SCAN`, `DDOS_ATTACK`, `SQL_INJECTION`, and `PHISHING`.  
- **Real-Time Visualization**: Displays network activity dynamically using **D3.js**.  
- **Pattern Matching Algorithms**: Uses **Knuth-Morris-Pratt (KMP)** for efficient anomaly detection.  
- **Modern UI**: A sleek, user-friendly interface with a dark theme for better visualization.  
- **Logs & Analysis**: Stores logs for further analysis and review.  

---

## 🛠️ Tech Stack  

| **Component**  | **Technology**  |
|---------------|----------------|
| **Backend**   | Flask (Python)  |
| **Frontend**  | React.js  |
| **Algorithms**  | Knuth-Morris-Pratt (KMP) for pattern matching  |
| **Visualization**  | D3.js for dynamic network graph  |

---

## 🔧 Setup Instructions  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/IDS_Simulator.git
cd IDS_Simulator

2️⃣ Backend Setup
Navigate to the backend folder and install dependencies:

bash
cd backend
pip install -r requirements.txt
Start the Flask server:

bash
python app.py
✅ The backend will run at http://127.0.0.1:5000.

3️⃣ Frontend Setup
Navigate to the frontend folder and install dependencies:

bash
cd ../frontend
npm install
Start the React app:

bash
npm start
✅ The frontend will open at http://localhost:3000.

📌 Usage
1️⃣ Open the React app in your browser.
2️⃣ Enter network traffic logs in the input field (e.g., PORT_SCAN DDOS_ATTACK PORT_SCAN).
3️⃣ Click Simulate to detect and analyze potential intrusions.
4️⃣ View real-time results and network visualization.

📁 Project Structure
IDS_Simulator/
├── backend/                  # Flask backend
│   ├── app.py                # Main Flask app
│   ├── requirements.txt      # Python dependencies
│   └── simulation/           # DSA and simulation logic
│       ├── graph.py          # NetworkGraph class
│       ├── pattern_matching.py  # KMP algorithm
│       └── intrusion_detection.py  # IntrusionDetectionSystem class
├── frontend/                 # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── App.js            # Main React component
│   │   └── index.js          # Entry point
│   ├── package.json          # Frontend dependencies
│   └── README.md
└── README.md                 # Project overview

🏆 Acknowledgments
Knuth-Morris-Pratt Algorithm: For efficient pattern matching.
D3.js: For interactive network graph visualization.
Flask & React: For a powerful backend and responsive frontend.
🔥 Start monitoring intrusions and securing networks today! 🔥
