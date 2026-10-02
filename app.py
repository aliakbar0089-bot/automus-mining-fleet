import streamlit as st
import pandas as pd
import datetime

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Automus Mining Fleet - Portal",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
st.sidebar.caption("Intelligent Site Operations & Management Platform")

portal = st.sidebar.radio(
    "Select Portal:",
    [
        "1. HR Portal", 
        "2. Accounts Portal", 
        "3. Site Manager Portal", 
        "4. Executive Dashboard",
        "5. Repair & Maintenance Portal"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Automus AI Engine Active**: Automated WhatsApp image parsing enabled for fuel receipts & breakdown logs.")

# ==========================================
# 1. HR PORTAL
# ==========================================
if portal == "1. HR Portal":
    st.title("👷 Automus HR & Operator Management")
    st.markdown("Onboard drivers, allocate heavy equipment, and manage site rosters.")
    
    tab1, tab2 = st.tabs(["Employee Induction & Allocation", "Current Roster"])
    
    with tab1:
        st.subheader("New Employee Induction & Asset Allocation")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name")
            st.text_input("National ID / Iqama Number")
            st.selectbox("Designation", ["Trailer Operator", "Excavator Operator", "Heavy Mechanic", "Site Supervisor"])
        with col2:
            st.selectbox("Assign Machine / Vehicle", ["Trailer 01", "Trailer 02", "Trailer 03", "Excavator 01", "Excavator 02", "Hammer EX-01"])
            st.date_input("Deployment Date", datetime.date.today())
            st.file_uploader("Upload Driver License / Certification", type=["pdf", "png", "jpg"])
        
        if st.button("Save Induction & Allocate Asset", type="primary"):
            st.success("Operator successfully onboarded and assigned in Automus Mining Fleet!")

    with tab2:
        st.subheader("Active Fleet Allocation")
        roster_data = pd.DataFrame({
            "Operator": ["Ali Hassan", "Tariq Mahmood", "Zubair Khan", "Sajid Ahmed"],
            "Role": ["Trailer Driver", "Trailer Driver", "Excavator Operator", "Hammer Operator"],
            "Assigned Asset": ["Trailer 01", "Trailer 02", "Excavator 01", "Hammer EX-01"],
            "Site Location": ["Zone A - Clay Pit", "Zone A - Clay Pit", "Zone B - Gypsum Quarry", "Zone B - Gypsum Quarry"],
            "Status": ["Active", "Active", "Active", "On Leave"]
        })
        st.dataframe(roster_data, use_container_width=True)

# ==========================================
# 2. ACCOUNTS PORTAL
# ==========================================
elif portal == "2. Accounts Portal":
    st.title("💰 Automus Accounts & Fuel Analytics")
    st.markdown("Daily, weekly, and monthly diesel cost logs parsed automatically from WhatsApp receipt updates.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Today's Diesel Cost", "$1,356", "+8%")
    col2.metric("Total Liters (Today)", "1,130 L", "+5%")
    col3.metric("Pump Consumption", "350 L", "Trailers")
    col4.metric("Mobile Tanker Fuel", "780 L", "Excavators/Hammers")
    
    st.markdown("---")
    st.subheader("Diesel Transactions Log")
    period = st.selectbox("View Period", ["Daily", "Weekly Summary", "Monthly Breakdown"])
    st.dataframe(st.session_state.diesel, use_container_width=True)
    
    st.subheader("Cost Distribution by Equipment Type")
    chart_data = pd.DataFrame({
        "Asset Type": ["Trailers (Pump)", "Excavators (Tanker)", "Hammers (Tanker)"],
        "Cost ($)": [1200, 2400, 1100]
    }).set_index("Asset Type")
    st.bar_chart(chart_data)

# ==========================================
# 3. SITE MANAGER PORTAL
# ==========================================
elif portal == "3. Site Manager Portal":
    st.title("🚜 Automus Operations & Site Manager Portal")
    st.markdown("Monitor fleet locations, daily production output, and incoming fault indicators.")
    
    tab1, tab2 = st.tabs(["Active Faults & Equipment Alerts", "Daily Production Logs"])
    
    with tab1:
        st.subheader("⚠ Equipment Fault Indicators (Real-Time from WhatsApp)")
        st.caption("Fault alerts uploaded by operators in WhatsApp groups appear here automatically.")
        
        st.dataframe(st.session_state.faults, use_container_width=True)
        
        st.markdown("### 🛠️ Dispatch Action (Automus Internal Notification)")
        c1, c2, c3 = st.columns(3)
        with c1:
            fault_id = st.selectbox("Select Fault ID", st.session_state.faults["ID"])
        with c2:
            new_status = st.selectbox("Update Status", ["Open", "In Progress", "Resolved"])
        with c3:
            st.write("")
            st.write("")
            if st.button("Update Status & Notify Mechanic"):
                st.session_state.faults.loc[st.session_state.faults["ID"] == fault_id, "Status"] = new_status
                st.success(f"Status for {fault_id} updated to '{new_status}' on the Automus dashboard.")
                st.rerun()

    with tab2:
        st.subheader("Site Production Log")
        prod_data = pd.DataFrame({
            "Date": ["2026-10-02", "2026-10-02", "2026-10-01"],
            "Asset": ["Trailer 01", "Excavator 01", "Hammer EX-01"],
            "Operating Hours": [10.5, 11.0, 8.5],
            "Trips / Output": ["14 Trips", "1,800 Tons", "650 Tons Break"],
            "Site": ["Zone A", "Zone A", "Zone B"]
        })
        st.dataframe(prod_data, use_container_width=True)

# ==========================================
# 4. EXECUTIVE DASHBOARD
# ==========================================
elif portal == "4. Executive Dashboard":
    st.title("📊 Automus Executive KPI Dashboard")
    st.markdown("High-level overview for Operations Managers, Project Managers, and Owners.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Fleet Count", "23 / 23 Assets", "100% Active")
    m2.metric("Total Production Output (MTD)", "42,500 Tons", "+12% vs Target")
    m3.metric("Fleet Availability", "91.3%", "-2% Maintenance")
    m4.metric("Avg Fuel Efficiency", "1.8 L/Ton", "Optimal")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Weekly Fleet Productivity (Tons)")
        prod_chart = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Production (Tons)": [2100, 2300, 2050, 2400, 1900, 2250, 2150]
        }).set_index("Day")
        st.line_chart(prod_chart)
        
    with c2:
        st.subheader("Downtime & Fault Breakdown")
        fault_chart = pd.DataFrame({
            "Category": ["Hydraulics", "Engine / Filters", "Tires & Tracks", "Electrical"],
            "Hours Lost": [14, 8, 5, 2]
        }).set_index("Category")
        st.bar_chart(fault_chart)

# ==========================================
# 5. REPAIR & MAINTENANCE PORTAL
# ==========================================
elif portal == "5. Repair & Maintenance Portal":
    st.title("🔧 Automus Repair & Maintenance Portal")
    st.markdown("Dedicated interface for mechanics and engineering staff to resolve breakdown faults and maintain service history.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Pending Faults", len(st.session_state.faults[st.session_state.faults["Status"] == "Open"]), "Requires Action")
    m2.metric("In Repair", len(st.session_state.faults[st.session_state.faults["Status"] == "In Progress"]), "Work Orders Open")
    m3.metric("Preventive Service Due", "3 Machines", "Next 48 Hours")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Active Fault Queue", "Log New Maintenance / Service", "Work Order History"])
    
    with tab1:
        st.subheader("🚨 Breakdown Fault Queue (Parsed from WhatsApp)")
        st.caption("Mechanics can pick up open issues, assign technicians, and close jobs here.")
        
        st.dataframe(st.session_state.faults, use_container_width=True)
        
        st.markdown("### 📝 Mechanics Update Form")
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_fault = st.selectbox("Select Fault Work Order", st.session_state.faults["ID"], key="maint_fault_id")
        with col2:
            assigned_mechanic = st.text_input("Lead Mechanic Name", "Rashid Khan")
        with col3:
            update_status = st.selectbox("Update Status", ["Open", "In Progress", "Resolved"], key="maint_status")
            
        repair_notes = st.text_area("Repair Action Notes / Spare Parts Used", "Replaced hydraulic seal ring and refilled fluid.")
        
        if st.button("Save Maintenance Action", type="primary"):
            st.session_state.faults.loc[st.session_state.faults["ID"] == selected_fault, "Status"] = update_status
            st.session_state.faults.loc[st.session_state.faults["ID"] == selected_fault, "Assigned Mechanic"] = assigned_mechanic
            st.success(f"Work order {selected_fault} updated to '{update_status}' by {assigned_mechanic}!")
            st.rerun()

    with tab2:
        st.subheader("⚙ Log Scheduled Service / PM Work Order")
        c1, c2 = st.columns(2)
        with c1:
            st.selectbox("Select Asset", ["Trailer 01", "Trailer 02", "Trailer 03", "Excavator 01", "Excavator 02", "Hammer EX-01", "Hammer EX-02"])
            st.selectbox("Service Category", ["Preventive Maintenance (PM)", "Unscheduled Repair", "Overhaul", "Tire/Track Replacement"])
            st.text_input("Technician / Workshop Name")
        with c2:
            st.text_input("Parts / Consumables Used (e.g., Oil Filter, Hydraulic Hose)")
            st.number_input("Parts & Labor Cost ($)", min_value=0, value=250)
            st.date_input("Service Date", datetime.date.today())
            
        if st.button("Log Maintenance Record"):
            st.success("Maintenance record saved to database!")

    with tab3:
        st.subheader("📜 Maintenance & Repair History")
        st.dataframe(st.session_state.maintenance_logs, use_container_width=True)
