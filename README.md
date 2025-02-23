# 🧪 Petstore API Testing Project

This project tests the **Petstore API** using **Pytest**, **Allure Reports**, and **BDD Gherkin-style test cases**.  
It includes manual and automated test cases for the **Pet Section** of the API.

---

## 🚀 **Project Structure**
```plaintext
Petstore-API-Testing
├── automation
│   ├── common_steps_api.py       # Common API steps
│   ├── test_petstore.py          # Automated test cases for Petstore API
│   ├── payloads                  # Test payloads (JSON files and images)
│   └── reports                   # Allure test reports
├── docs
│   ├── Test_Plan.md              # Test plan with scope and objectives
│   ├── Test_Scenarios.md         # Test scenarios with steps and expected results
│   ├── Test_Cases_Manual.md      # Manual test cases with IDs, steps, and assertions
│   ├── Test_Results.md           # Latest test execution results
│   ├── Bugs.md                   # List of known bugs with IDs and reproduction steps
│   └── Traceability_Matrix.md    # Mapping of test cases to requirements
└── README.md                     # This file
```

---

## 📝 **Test Documentation**
- 📋 **[Test Plan](docs/Test_Plan.md)**: Overview of the testing scope, strategy, and schedule.  
- 🗂 **[Test Scenarios](docs/Test_Scenarios.md)**: Detailed scenarios with preconditions, actions, and expected outcomes.  
- 🧪 **[Test Cases](docs/Test_Cases_Manual.md)**: Manual test cases with step-by-step instructions and assertions.  
- 📊 **[Test Results](docs/Test_Results.md)**: Summary of the latest test execution results (including XFAILs).  
- 🐞 **[Bugs](docs/Bugs.md)**: Known bugs with unique IDs, affected endpoints, and reproduction steps.  
- 📏 **[Traceability Matrix](docs/Traceability_Matrix.md)**: Mapping of test cases to project requirements for coverage tracking.  

---

## 💻 **How to Run Automated Tests**
1. **Clone the Repository**  
```bash
git clone https://github.com/oleksovskyi/Petstore-API-Project.git
cd Petstore-API-Project
```

2. **Set Up Virtual Environment**  
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Run Tests With Allure Reporting**  
```bash
pytest automation/test_petstore.py --alluredir=automation/reports/allure-results
```

4. **Generate Allure Report**  
```bash
allure generate automation/reports/allure-results -o automation/reports/allure-report --clean
```

5. **View Allure Report**  
```bash
allure serve automation/reports/allure-report
```

---

## ❗ **Known Issues**
- Some API endpoints return incorrect status codes due to known bugs (tracked in **[Bugs.md](docs/Bugs.md)**).
- Tests related to these bugs are marked as **XFAIL** using Pytest markers.

---

## 📦 **Project Requirements**
- **Python 3.11**  
- **Pytest**  
- **Allure-Pytest**  
- **Requests Library**  

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## ✨ **Author**
**[Yurii Oleksovskyi](https://github.com/oleksovskyi)**  
Quality Assurance Engineer | API & Automation Testing

---
