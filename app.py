import streamlit as st
import pandas as pd
import datetime
import os
from groq import Groq

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Automus Mining Fleet - Gypsum Site Portal",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GROQ CLIENT INITIALIZATION ---
groq_api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))

def get_groq_response(prompt, system_instruction, model="openai/gpt-oss-120b"):
    """Helper function to route tasks to specific AI agents via Groq API."""
    if not groq_api_key:
        return "⚠️ **Groq API Key missing.** Please configure GROQ_API_KEY in Streamlit Secrets."
    try:
        client = Groq(api_key=groq_api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ **Agent Error:** {str(e)}"

# --- MOCK DATA INITIALIZATION ---
if 'faults' not in st.session_state:
    st.session_state.faults = pd.DataFrame([
        {"ID": "FLT-101", "Asset": "Trailer 04", "Issue": "Hydraulic Pressure Low", "Severity": "High", "Status": "Open", "Reported": "10 Mins ago", "Assigned Mechanic": "Unassigned"},
        {"ID": "FLT-102", "Asset": "Hammer EX-02", "Issue": "Chisel Wear & Leak", "Severity": "Medium", "Status": "In Progress", "Reported": "2 Hours ago", "Assigned Mechanic": "Rashid Khan"}
    ])

if 'maintenance_logs' not in st.session_state:
    st.session_state.maintenance_logs = pd.DataFrame([
        {"Work Order": "WO-201", "Asset": "Excavator 01", "Service Type": "500-Hr Service", "Parts Replaced": "Engine Oil, Filters", "Technician": "Rashid Khan", "Date": "2026-09-28", "Cost ($)": 450},
        {"Work Order": "WO-202", "Asset": "Trailer 02", "Service Type": "Brake Shoe Repair", "Parts Replaced": "Brake Pads", "Technician": "Tariq Mahmood", "Date": "2026-09-30", "Cost ($)": 320}
    ])

if 'diesel' not in st.session_state:
    st.session_state.diesel = pd.DataFrame([
        {"Date": "2026-10-02", "Asset": "Trailer 01", "Source": "Diesel Pump", "Liters": 350, "Cost ($)": 420},
        {"Date": "2026-10-02", "Asset": "Excavator 01", "Source": "Mobile Tanker", "Liters": 500, "Cost ($)": 600},
        {"Date": "2026-10-01", "Asset": "Hammer EX-01", "Source": "Mobile Tanker", "Liters": 280, "Cost ($)": 336}
    ])

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/color/96/dump-truck.png", width=64)
st.sidebar.title("Automus Mining Fleet")
st.sidebar.caption("Gypsum Operations Platform")

portal = st.sidebar.radio(
    "Select Operational Portal:",
    [
        "1. HR Portal (Onboarding Agent)", 
        "2. Accounts Portal (Fuel Analytics Agent)", 
        "3. Operations Portal (Dispatch Agent)", 
        "4. Maintenance Portal (Diagnostic Agent)",
        "5. Store & Inventory Portal",
        "6. Executive Dashboard (Strategic Agent)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("🤖 **AI Agents Active**\n- Gypsum Logistics\n- Fuel Audit\n- Dispatch Agent\n- Diagnostic Agent\n- Inventory Agent\n- Executive Agent")

# ==========================================
# 1. HR PORTAL
# ==========================================
if portal == "1. HR Portal (Onboarding Agent)":
    st.title("👷 HR Portal & Onboarding Agent")
    st.markdown("Automated driver verification and equipment allocation at the Gypsum Site.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Operator Induction")
        emp_name = st.text_input("Full Name", "Ahmad Hassan")
        iqama = st.text_input("Iqama / National ID", "2489012345")
        role = st.selectbox("Designation", ["Trailer Operator", "Excavator Operator", "Heavy Mechanic", "Hammer Specialist"])
        exp_years = st.number_input("Years of Experience", min_value=1, max_value=40, value=6)
        assigned_asset = st.selectbox("Target Equipment", ["Trailer 01", "Trailer 02", "Excavator 01", "Hammer EX-01"])

    with col2:
        st.subheader("🤖 AI Agent Assessment")
        if st.button("Run Agent Evaluation", type="primary"):
            system_prompt = "You are the Automus Onboarding AI Agent for Gypsum Quarry Operations. Evaluate operator details, safety compliance, and confirm equipment match."
            user_prompt = f"Evaluate candidate: Name: {emp_name}, Role: {role}, Experience: {exp_years} years, Assigned Asset: {assigned_asset} for single-site Gypsum operations."
            
            with st.spinner("Logistics Agent evaluating operator..."):
                agent_response = get_groq_response(user_prompt, system_prompt)
                st.info(agent_response)

# ==========================================
# 2. ACCOUNTS PORTAL
# ==========================================
elif portal == "2. Accounts Portal (Fuel Analytics Agent)":
    st.title("💰 Accounts Portal & Fuel Analytics Agent")
    st.markdown("Gypsum site diesel audit, weighbridge earnings, and cost tracking.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Today's Diesel Cost", "$1,356", "+8%")
    col2.metric("Total Liters (Today)", "1,130 L", "+5%")
    col3.metric("Pump Consumption", "350 L", "Trailers")
    col4.metric("Mobile Tanker Fuel", "780 L", "Excavators/Hammers")
    
    st.markdown("---")
    st.dataframe(st.session_state.diesel, use_container_width=True)
    
    st.subheader("🤖 AI Fuel Anomaly Audit")
    if st.button("Run Fuel Audit", type="primary"):
        system_prompt = "You are the Automus Fuel Analytics AI Agent for Gypsum quarry operations. Audit diesel consumption and flag abnormal burn rates."
        log_json = st.session_state.diesel.to_json(orient="records")
        user_prompt = f"Audit these Gypsum site diesel transactions: {log_json}."
        
        with st.spinner("Fuel Agent auditing logs..."):
            audit_result = get_groq_response(user_prompt, system_prompt)
            st.success(audit_result)

# ==========================================
# 3. OPERATIONS PORTAL
# ==========================================
elif portal == "3. Operations Portal (Dispatch Agent)":
    st.title("🚜 Operations & Production Portal")
    st.markdown("Gypsum haulage monitoring, trip counts, and daily productivity logs.")
    
    tab1, tab2 = st.tabs(["Daily Production Logs", "🤖 AI Dispatch Advisor"])
    
    with tab1:
        prod_data = pd.DataFrame({
            "Date": ["2026-10-02", "2026-10-02", "2026-10-01"],
            "Asset": ["Trailer 01", "Excavator 01", "Hammer EX-01"],
            "Operating Hours": [10.5, 11.0, 8.5],
            "Trips / Output": ["14 Trips", "1,800 Tons", "650 Tons Break"]
        })
        st.dataframe(prod_data, use_container_width=True)

    with tab2:
        st.subheader("Request Haulage & Production Plan")
        target_tons = st.number_input("Target Gypsum Production (Tons/Day)", value=2000)
        
        if st.button("Generate Strategy", type="primary"):
            system_prompt = "You are the Automus Operations AI Agent for Gypsum extraction. Calculate 40-ton dumper trip cycles over a 9km haulage route to reach target tonnage."
            user_prompt = f"Plan extraction and haulage strategy for {target_tons} Tons/Day at the Gypsum quarry."
            
            with st.spinner("Dispatch Agent computing fleet cycle times..."):
                plan = get_groq_response(user_prompt, system_prompt)
                st.markdown(plan)

# ==========================================
# 4. MAINTENANCE PORTAL
# ==========================================
elif portal == "4. Maintenance Portal (Diagnostic Agent)":
    st.title("🔧 Repair & Maintenance Portal")
    st.markdown("Breakdown diagnostics, hydraulic hammer maintenance, and work order tracking.")
    
    st.dataframe(st.session_state.faults, use_container_width=True)
    
    st.subheader("🤖 AI Technical Diagnostics")
    selected_fault = st.selectbox("Select Breakdown Ticket", st.session_state.faults["ID"])
    fault_details = st.session_state.faults[st.session_state.faults["ID"] == selected_fault].to_dict(orient="records")[0]
    
    if st.button("Diagnose Fault", type="primary"):
        system_prompt = "You are the Automus Mechanical Diagnostic AI Agent for heavy Gypsum quarry equipment (rock breakers, excavators, tractor trailers)."
        user_prompt = f"Diagnose this breakdown log: {fault_details}. Provide: 1. Root Cause, 2. Required Spare Parts, 3. Estimated Downtime."
        
        with st.spinner("Diagnostic Agent analyzing issue..."):
            diag_output = get_groq_response(user_prompt, system_prompt)
            st.warning(diag_output)

# ==========================================
# 5. STORE & INVENTORY PORTAL
# ==========================================
elif portal == "5. Store & Inventory Portal":
    st.title("📦 Store & Inventory Management")
    st.markdown("Track spare parts, lubricants, filters, and issued machine components.")
    
    inv_data = pd.DataFrame([
        {"Part ID": "PRT-01", "Part Name": "Hydraulic Oil Filter", "Stock On Hand": 14, "Unit Cost ($)": 45, "Reorder Level": 5},
        {"Part ID": "PRT-02", "Part Name": "Rock Breaker Chisel Tip", "Stock On Hand": 3, "Unit Cost ($)": 650, "Reorder Level": 2},
        {"Part ID": "PRT-03", "Part Name": "Trailer Brake Shoe Set", "Stock On Hand": 8, "Unit Cost ($)": 120, "Reorder Level": 4}
    ])
    st.dataframe(inv_data, use_container_width=True)

# ==========================================
# 6. EXECUTIVE DASHBOARD
# ==========================================
elif portal == "6. Executive Dashboard (Strategic Agent)":
    st.title("📊 Executive Dashboard")
    st.markdown("High-level Gypsum quarry KPIs, fleet availability, and cost per ton.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Fleet", "23 / 23 Assets", "100% Active")
    m2.metric("MTD Production", "42,500 Tons Gypsum", "+12% vs Target")
    m3.metric("Fleet Availability", "91.3%", "-2% Maintenance")
    m4.metric("Avg Efficiency", "1.8 L/Ton", "Optimal")
    
    st.markdown("---")
    
    if st.button("Generate Strategy Briefing", type="primary"):
        system_prompt = "You are the Automus Strategic AI Operations Advisor for executive leadership managing a single-site Gypsum quarry operation."
        user_prompt = "Synthesize fleet availability (91.3%), production output (42,500 Tons MTD), and fuel efficiency (1.8 L/Ton). Provide 3 concise operational recommendations."
        
        with st.spinner("Strategic Agent compiling executive brief..."):
            exec_brief = get_groq_response(user_prompt, system_prompt)
            st.markdown(exec_brief)
