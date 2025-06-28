
# 🌿 Agri Fund Assist – Smart Rural Banking Assistant

**Agri Fund Assist** is a digital assistant designed to improve financial inclusion for farmers in Africa. It enables users to open accounts, request agricultural credit, and access financial education — in both Portuguese and local languages (Kimbundu, Umbundu, Kikongo), with English support included.

---

## 📦 Features

### ✅ Backend (FastAPI + IBM Granite)
- Receives requests and generates responses using IBM's Granite LLM
- OCR document upload with Tesseract
- Multilingual prompt generation (PT, EN, Kimbundu, Umbundu, Kikongo)

### ✅ Frontend (Vue 3 SPA)
- Fully responsive and mobile-friendly
- Language switcher with real-time UI adjustments
- Upload documents and receive extracted text
- Real-time assistant responses with visual formatting

---

## 🚀 Project Structure

```
Agri Fund-assist/
│
├── backend/
│   ├── main.py                  # FastAPI entrypoint
│   ├── prompts/
│   │   └── prompt_generator.py  # Language-aware prompt templates
│   ├── utils/
│   │   └── watsonx_client.py    # IBM Granite API integration
│   └── temp/                    # Uploaded files for OCR
│
├── ui/
│   └── (Vue 3 SPA project)      # SPA with multilingual support
│
└── README.md
```

---

## 🛠️ Setup Instructions

### 🔁 Prerequisites
- Python 3.10+
- Node.js 18+
- IBM Cloud API credentials (for Watsonx/Granite)

---

### 🐍 Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

> ℹ️ Make sure to create a `.env` file with your Watsonx credentials in `utils/watsonx_client.py`.

---

### 🌐 Frontend Setup (Vue 3 + Vite)

```bash
cd frontend
npm install
npm run dev
```

> 🌍 Visit `http://localhost:5173` to access the interface.

---

## 🌍 Language Support

- 🇦🇴 **Portuguese**
- 🗣️ **Kimbundu**
- 🗣️ **Umbundu**
- 🗣️ **Kikongo**
- 🌐 **English**

> Language selection affects both UI and assistant responses.

---

## 📂 Endpoints Overview

| Endpoint                 | Purpose                             |
|--------------------------|-------------------------------------|
| `/presentation/`         | Shows greeting and welcome message  |
| `/open-account/`         | Account opening prompt              |
| `/agri-credit/`          | Agricultural credit prompt          |
| `/financial-education/`  | Financial education info            |
| `/upload-documento/`     | OCR file processing (image/pdf)     |
| `/process-simulation/`   | Business logic + flow mock          |

---

## 🤝 Contributing

Want to help translate to more African languages?  
Feel free to fork and submit pull requests!

---

## 🔐 License

MIT © 2025 – Agri Fund Hackathon Team found by Estima E.C Sahuma
