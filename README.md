# 🚜 Automus Mining Fleet — Gypsum Quarry Operations

**Automus Mining Fleet** is an agentic AI-driven fleet management platform built specifically for heavy quarry operations (Gypsum extraction). It automates data ingestion from WhatsApp groups (diesel receipts, weighbridge bills, breakdown photos) into Google Sheets and provides real-time operational insights across 6 specialized AI agent portals.

---

## 🌟 6 Specialized AI Agent Portals

1. **👷 HR & Onboarding Agent:** Onboard drivers, verify national IDs/Iqamas, and assign operators directly to heavy machinery (trailers, excavators, rock breakers).
2. **💰 Accounts & Fuel Analytics Agent:** Audit daily, weekly, and monthly diesel logs parsed from WhatsApp fuel pump receipts and mobile tanker uploads, and track weighbridge earnings.
3. **🚜 Operations & Dispatch Agent:** Monitor heavy machinery output, track trip counts, and calculate optimal haulage cycle times over 9 km dumper routes.
4. **🔧 Repair & Maintenance (Diagnostic Agent):** Analyze breakdown photos and fault reports posted in WhatsApp, estimate root causes, suggest spare parts, and compute Mean Time to Repair (MTTR).
5. **📦 Store & Inventory Agent:** Manage spare parts catalog, track items issued per machine/work order, and monitor reorder threshold levels.
6. **📊 Executive Strategic Agent:** High-level strategic briefing generator summarizing site availability, MTD tonnage, and unit cost per ton ($\text{Cost/Ton}$).

---

## 🛠️ Core Tech Stack

* **Frontend & UI:** [Streamlit](https://streamlit.io/)
* **AI & Vision Engine:** [Groq API](https://groq.com/) (`llama-3.3-70b-versatile` & `llama-3.2-11b-vision-preview`)
* **Database & Persistence:** Google Sheets API (`gspread` / `st.connection`)
* **Data Processing:** Python / Pandas
* **Deployment:** GitHub & Streamlit Community Cloud

---

## 📊 Google Sheets Multi-Tab Database Schema

The system uses an 8-tab workbook structure designed for single-site Gypsum quarrying:

1. `Assets_Master`: Machine catalog (`Asset ID`, `Type`, `Model`, `Serial No`, `Status`)
2. `Driver_Roster`: Operator credentials & machine allocations
3. `Fuel_Log`: Diesel dispenser receipts & mobile tanker logs
4. `Weighbridge_Earnings`: Net tonnage shipped & daily revenue tracking
5. `Faults_Breakdowns`: Open breakdown tickets, timestamps, & downtime hours
6. `Maintenance_Schedule`: 250-hr/500-hr preventive service schedules
7. `Inventory_Store`: Spare parts inventory, unit costs, & reorder alerts
8. `Production_Log`: Daily trips, operating hours, & tonnage per asset

---

## 🚀 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/automus-mining-fleet.git](https://github.com/your-username/automus-mining-fleet.git)
   cd automus-mining-fleet
