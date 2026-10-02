# 🚜 Automus Mining Fleet

**Automus Mining Fleet** is an intelligent site operations and fleet management portal designed for mining, quarrying, and heavy equipment operations. It automates data intake from WhatsApp group uploads (diesel receipts, mobile tanker logsheets, breakdown photos) using **Groq AI (Llama Vision)** and provides a multi-role dashboard built with **Streamlit**.

---

## 🌟 Key Features & Role Portals

1. **👷 HR & Operator Management:** Onboard drivers, track certifications, and allocate operators to specific heavy equipment assets across site zones.
2. **💰 Accounts & Fuel Analytics:** Track daily, weekly, and monthly diesel consumption and costs automatically parsed from fuel pump receipts and mobile tanker logs.
3. **🚜 Operations & Site Manager Portal:** Monitor active equipment status, review real-time fault indicators extracted from WhatsApp messages, update maintenance statuses without manual messaging, and log daily production metrics.
4. **📊 Executive KPI Dashboard:** High-level operational metrics for Project Managers and Owners, including fleet availability, MTD production tonnage, and downtime trend analysis.

---

## 🛠️ Tech Stack

* **Frontend & Dashboard:** [Streamlit](https://streamlit.io/)
* **AI & Vision Parsing Engine:** [Groq API](https://groq.com/) (`llama-3.2-11b-vision-preview`)
* **Data Processing:** Python / Pandas
* **Database / Backend:** Google Sheets API (`gspread`) / Streamlit Connections
* **Hosting & Deployment:** GitHub & Streamlit Community Cloud

---

## 🚀 Local Setup Instructions

1. **Clone or download the repository:**
   ```bash
   git clone [https://github.com/your-username/automus-mining-fleet.git](https://github.com/your-username/automus-mining-fleet.git)
   cd automus-mining-fleet
