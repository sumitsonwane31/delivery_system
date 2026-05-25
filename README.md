# 🚀 Delivery System Simulation (Python)

## 📌 Overview

This project simulates a logistics delivery system where multiple agents pick up packages from warehouses and deliver them to their destinations.

The system processes multiple test cases and generates reports showing:

* Packages delivered by each agent
* Total distance traveled
* Efficiency of each agent
* Best performing agent

---

## 🧠 Key Features

* 📦 Nearest-agent package assignment
* 🚚 Dynamic delivery simulation (agent movement)
* 📏 Euclidean distance calculation
* 📊 Efficiency-based performance evaluation
* 📁 Supports multiple test cases
* 💾 JSON input and output handling

---

## ⚙️ Tech Stack

* Python 3.x
* Standard Libraries (json, math, os)

---

## 🗂️ Project Structure

```
delivery-system/
│
├── main.py                # Main simulation script
├── test_case_1.json
├── test_case_2.json
├── test_case_3.json
├── ...
├── report_1.json
├── report_2.json
└── README.md
```

---

## 🧠 How It Works

### 1️⃣ Assignment Phase

* Each package is assigned to the **nearest agent**
* Based on **initial agent location**
* Ensures stable and correct mapping

---

### 2️⃣ Simulation Phase

For each assigned package:

* Agent travels → Warehouse
* Warehouse → Destination
* Agent location is updated dynamically

---

### 3️⃣ Reporting Phase

For each agent:

* Total packages delivered
* Total distance traveled
* Efficiency = distance / packages

👉 Best agent = **lowest efficiency**

---

## ▶️ How to Run

### Step 1: Navigate to project folder

```bash
cd delivery-system
```

---

### Step 2: Run the program

```bash
python main.py
```

---

## 📊 Output

* Results will be printed in terminal
* Reports will be saved as:

```
report_1.json
report_2.json
...
```

---

## 🧪 Testing

The system automatically runs all test cases:

* `test_case_1.json`
* `test_case_2.json`
* ...
* `test_case_10.json`

Each test case represents a different logistics scenario.

---

## 📥 Sample Input (Test Case)

```json
{
  "warehouses": {
    "W1": [0, 0]
  },
  "agents": {
    "A1": [5, 5]
  },
  "packages": [
    {
      "id": "P1",
      "warehouse": "W1",
      "destination": [10, 10]
    }
  ]
}
```

---

## 📤 Sample Output

```json
{
  "A1": {
    "packages_delivered": 1,
    "total_distance": 14.14,
    "efficiency": 14.14
  },
  "best_agent": "A1"
}
```

---

## 🧠 Design Decisions

* 🔹 Separated assignment and simulation phases
* 🔹 Used greedy nearest-agent strategy
* 🔹 Maintained dynamic agent movement
* 🔹 Used initial position snapshot to avoid mutation issues

---

## ⚠️ Edge Cases Handled

* Agents with no assigned packages
* Multiple agents and warehouses
* Variable dataset sizes
* Large coordinate values

---

## 🚀 Future Improvements

* 📊 Route visualization
* ⚡ Performance optimization
* 🧪 Unit testing with pytest
* 🌐 Convert to API (FastAPI / Flask)

---

## 👨‍💻 Author

**Sumit Sonwane**
Python Developer

---

## 💡 Interview Highlight

> “Built a logistics simulation system using Python that assigns packages using a nearest-agent strategy and simulates real-world delivery movement across multiple dynamic test cases.”

---
