📊 Bank Statement PDF to CSV Converter
✨ Made with ❤️ by Shivam Pandey

🚀 Project Overview
A powerful Python Streamlit application that converts bank statement PDFs into structured CSV files with clean, organized transaction data. Perfect for financial analysis, expense tracking, and accounting automation.

https://img.shields.io/badge/Demo-Live_Green?style=for-the-badge&logo=streamlit
https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge&logo=github
https://img.shields.io/badge/Python-3.8%252B-yellow?style=for-the-badge&logo=python

🎯 Key Features
✅ Extracts Tabular Data – Perfect for HDFC, ICICI, SBI, Axis, etc.
✅ Auto-Cleans Transactions – Removes empty rows, formats dates & amounts
✅ CSV Export – Ready for Excel/Google Sheets
✅ Fast Processing – Optimized for large statements
✅ User-Friendly UI – Drag & drop, progress tracking

🛠️ Tech Stack
Category	Technology
Frontend	Streamlit
PDF Processing	pdfplumber
Data Handling	Pandas
OCR (Fallback)	Tesseract
Logging	Python logging
📥 Installation
1. Clone the Repository

git clone https://github.com/shivam-pandey/bank-statement-converter.git
cd bank-statement-converter
2. Install Dependencies

pip install -r requirements.txt
3. Set Up Tesseract OCR (Optional for Scanned PDFs)

# Windows (Download installer)
https://github.com/UB-Mannheim/tesseract/wiki

# Linux (Debian/Ubuntu)
sudo apt install tesseract-ocr
🚦 How to Run

streamlit run main.py
Access the app:
🌐 Open http://localhost:8501 in your browser

🖥️ UI Preview
Upload PDF	Process & Preview	Download CSV
https://via.placeholder.com/300x200/4CAF50/FFFFFF?text=Drag+%2526+Drop+PDF	https://via.placeholder.com/300x200/2196F3/FFFFFF?text=Extracting+Data	https://via.placeholder.com/300x200/FF5722/FFFFFF?text=CSV+Ready
⚙️ How It Works
Upload → Drag & drop your bank statement PDF

Process → AI detects tables & extracts transactions

Download → Get a clean CSV for analysis

📂 Project Structure
text
bank-statement-converter/
├── main.py                # Streamlit UI
├── pdf_processor.py       # Core PDF extraction logic
├── config.py              # Paths & settings
├── utils.py               # Data cleaning functions
├── requirements.txt       # Dependencies
├── README.md              # This file
└── samples/               # Example PDFs for testing
💡 Use Cases
✔ Personal Finance Tracking
✔ Business Accounting
✔ Tax Filing Automation
✔ Bank Reconciliation

📜 License
This project is licensed under MIT License.

👨‍💻 Author
Shivam Pandey
https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github
https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin

🙌 Support
⭐ Star the repo if you find it useful!
🐞 Report issues here

🎨 Color Palette Used
Primary	Secondary	Accent
#1F77B4 (Blue)	#4CAF50 (Green)	#FF5722 (Orange)
🔹 Icons Used
📊 Analytics → For data extraction

🏦 Bank → Represents statements

⚡ Fast → Processing speed

📥 Download → CSV export

🎉 Happy Banking!
Convert PDFs like a pro with this tool. Finance management made easy! 💰📈
