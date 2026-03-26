# E-Commorce-Customer-Churn-Mitigation
Developed a machine learning system to predict customers likely to churn on an e-commerce platform and provided actionable insights for targeted retention strategies, helping improve customer engagement, loyalty, and overall retention.

Rroject Structure
e-commorceCustomerChurn/
│── app.py
│── best_model.pkl
│── test_dataset.xlsx
│── result.txt
│── requirements.txt
│── templates/
│    └── index.html

🧩 Step-by-Step: Install Libraries from requirements.txt
✅ Step 1: Install Python
Download from: https://www.python.org
Make sure to check ✅ "Add Python to PATH"

Verify installation:

python --version
✅ Step 2: Navigate to Project Folder

Open terminal / command prompt:

cd path/to/your/project
✅ Step 3: Create Virtual Environment (Recommended)
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python3 -m venv venv
source venv/bin/activate

👉 This keeps dependencies isolated.

✅ Step 4: Install Dependencies

Run:

pip install -r requirements.txt or
python -m pip install -r requirements.txt

This will install:

flask
pandas
joblib
openpyxl
scikit-learn

✅ Step 5: Verify Installation
pip list

You should see all required packages.

🚀 Step 6: Run the Project
python app.py

Output:

Running on http://127.0.0.1:5000/

Open in browser:
👉 http://127.0.0.1:5000/

🧪 Step 7: Test the App
Enter a Customer ID
Fetch data
Click Predict
View churn result

⚠️ Common Errors & Fixes
❌ ModuleNotFoundError

👉 Fix:

pip install -r requirements.txt
❌ Excel file not loading

👉 Fix:

pip install openpyxl
❌ Model not found

👉 Ensure:

best_model.pkl is in same folder as app.py
❌ Wrong Python version

👉 Use Python 3.8–3.11 for best compatibility

🌟 Bonus Improvements (If You Want to Upgrade)
Add login system
Deploy on Heroku / Render
Use React frontend
Add real-time analytics dashboard
Store predictions in database (MySQL / MongoDB)
