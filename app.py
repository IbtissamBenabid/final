import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from suppliers_data import suppliers_data

# Define the data for each category
categories = {
    "1️⃣ Supplier General Characteristics": [
        {"Criteria": "Supplier criticality", "Options": ["Core business dependency", "Important service", "Support service", "Non-essential"]},
        {"Criteria": "Supplier size", "Options": ["Very small / unstable", "Medium", "Large", "Multinational"]},
        {"Criteria": "Years of activity", "Options": ["< 2 years", "2–5 years", "5–10 years", ">10 years"]},
        {"Criteria": "Dependency level", "Options": ["Single supplier", "Few alternatives", "Multiple suppliers", "Easily replaceable"]}
    ],
    "2️⃣ Geographical Risk Criteria": [
        {"Criteria": "Country risk", "Options": ["Sanctioned / unstable", "Politically sensitive", "Emerging economy", "Stable country"]},
        {"Criteria": "Data hosting location", "Options": ["High-risk country", "Mixed locations", "Regulated region", "Local / EU"]},
        {"Criteria": "Regulatory alignment", "Options": ["No clear regulation", "Partial compliance", "Local compliance", "GDPR / strong laws"]},
        {"Criteria": "Cross-border data flow", "Options": ["Uncontrolled", "Limited control", "Contractual control", "Fully regulated"]}
    ],
    "3️⃣ Sector & Activity Criteria": [
        {"Criteria": "Sector sensitivity", "Options": ["Finance / Health", "Telecom / Gov", "IT services", "Non-sensitive"]},
        {"Criteria": "Service type", "Options": ["Core operations", "Business support", "Technical support", "Administrative"]},
        {"Criteria": "System access", "Options": ["Full privileged access", "High access", "Limited access", "No access"]},
        {"Criteria": "Process outsourcing", "Options": ["Full outsourcing", "Partial", "Limited", "None"]}
    ],
    "4️⃣ Information Security & Cyber Risk": [
        {"Criteria": "Data sensitivity", "Options": ["Highly confidential", "Personal data", "Internal data", "Public data"]},
        {"Criteria": "Security certification", "Options": ["None", "In progress", "Partial", "ISO 27001 / SOC2"]},
        {"Criteria": "Incident history", "Options": ["Repeated incidents", "Major incident", "Minor incidents", "None"]},
        {"Criteria": "Access management", "Options": ["No control", "Weak controls", "Standard controls", "Strong IAM"]}
    ],
    "5️⃣ Business Continuity & Operational Risk": [
        {"Criteria": "BCP / DRP", "Options": ["Not existing", "Informal", "Documented", "Tested & audited"]},
        {"Criteria": "RTO / RPO", "Options": ["Undefined", "Very high", "Moderate", "Optimized"]},
        {"Criteria": "SLA availability", "Options": ["No SLA", "Weak SLA", "Standard SLA", "Strong SLA"]},
        {"Criteria": "Subcontracting", "Options": ["Unknown", "Multiple", "Limited", "Controlled"]}
    ],
    "6️⃣ Financial & Legal Risk": [
        {"Criteria": "Financial stability", "Options": ["Loss-making", "Weak cash flow", "Stable", "Strong growth"]},
        {"Criteria": "Legal compliance", "Options": ["Non-compliant", "Partial", "Mostly compliant", "Fully compliant"]},
        {"Criteria": "Insurance", "Options": ["None", "Limited", "Adequate", "Full coverage"]},
        {"Criteria": "Litigation history", "Options": ["Frequent", "Occasional", "Rare", "None"]}
    ],
    "7️⃣ ESG & Ethical Criteria": [
        {"Criteria": "Ethics policy", "Options": ["None", "Informal", "Documented", "Enforced"]},
        {"Criteria": "Anti-corruption", "Options": ["No controls", "Weak controls", "Internal policy", "Audited program"]},
        {"Criteria": "Environmental impact", "Options": ["Harmful", "Uncontrolled", "Managed", "Sustainable"]},
        {"Criteria": "Social responsibility", "Options": ["Violations", "Weak HR practices", "Basic", "Certified / audited"]}
    ]
}

# Risk levels mapping: lower index is higher risk
risk_levels = ["Critical", "High", "Medium", "Low"]

# Streamlit app
st.title("TPRM Supplier Classification Dashboard")

# Get unique sectors and geographies
all_sectors = sorted(set(supplier["metadata"]["sector"] for supplier in suppliers_data.values() if "metadata" in supplier))
all_geographies = sorted(set(supplier["metadata"]["geography"] for supplier in suppliers_data.values() if "metadata" in supplier))

# Filters
col1, col2 = st.columns(2)
with col1:
    selected_sector = st.selectbox("Filter by Sector", ["All"] + all_sectors, help="Filter suppliers by sector")
with col2:
    selected_geography = st.selectbox("Filter by Geography", ["All"] + all_geographies, help="Filter suppliers by geography")

# Filter suppliers
filtered_suppliers = [name for name, data in suppliers_data.items() 
                     if (selected_sector == "All" or data.get("metadata", {}).get("sector") == selected_sector) and
                        (selected_geography == "All" or data.get("metadata", {}).get("geography") == selected_geography)]

# Show available suppliers in current filter
if filtered_suppliers:
    st.info(f"📋 **Available suppliers in current filter ({len(filtered_suppliers)}):** {', '.join(filtered_suppliers[:10])}{'...' if len(filtered_suppliers) > 10 else ''}")
else:
    st.warning("No suppliers match the current filters.")

# Supplier selection with dropdown and custom input
supplier_selection_method = st.radio(
    "Supplier Selection Method",
    ["Select from dropdown", "Enter custom name"],
    horizontal=True,
    help="Choose how to select or enter the supplier name"
)

if supplier_selection_method == "Select from dropdown":
    if filtered_suppliers:
        supplier_name = st.selectbox(
            "Select Supplier from Database", 
            filtered_suppliers,
            help="Choose from filtered suppliers in the database"
        )
    else:
        st.warning("No suppliers match the current filters. Try adjusting the filters or use 'Enter custom name'.")
        supplier_name = ""
else:
    supplier_name = st.text_input(
        "Enter Supplier Name", 
        placeholder="Enter supplier name...",
        help="Type a supplier name for assessment"
    )

# Show company info if supplier is found
if supplier_name and supplier_name in suppliers_data:
    supplier_info = suppliers_data[supplier_name]["metadata"]
    st.success(f"✅ **{supplier_name}** found in database!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sector", supplier_info["sector"])
    with col2:
        st.metric("Geography", supplier_info["geography"])
    with col3:
        st.metric("Size", supplier_info["size"])
    
    # Load supplier profile if available
    supplier_profile = suppliers_data.get(supplier_name, {}).get("profile", {})
elif supplier_name and supplier_name not in suppliers_data:
    st.info(f"ℹ️ **{supplier_name}** not found in database. Proceeding with manual risk assessment.")
    supplier_profile = {}
else:
    supplier_profile = {}

# Advanced filters in sidebar
with st.sidebar.form("classification_form"):
    st.header("Advanced Risk Selection")
    selected_levels = {}
    for cat_name, criteria_list in categories.items():
        with st.expander(cat_name):
            for crit in criteria_list:
                key = f"{cat_name}_{crit['Criteria']}"
                default_option = supplier_profile.get(key, crit['Options'][0])
                selected_levels[key] = st.selectbox(
                    crit['Criteria'],
                    options=crit['Options'],
                    index=crit['Options'].index(default_option),
                    key=key,
                    help=f"Select the most appropriate risk level for {crit['Criteria']}"
                )
    
    submitted = st.form_submit_button("Classify Supplier", type="primary")

if submitted:
    # Main content
    st.header(f"Risk Classifications for {supplier_name or 'Unnamed Supplier'}")

    # Display selections
    for cat_name, criteria_list in categories.items():
        st.subheader(cat_name)
        for crit in criteria_list:
            key = f"{cat_name}_{crit['Criteria']}"
            selected = selected_levels[key]
            level_index = crit['Options'].index(selected)
            level = risk_levels[level_index]
            st.write(f"**{crit['Criteria']}**: {selected} ({level} Risk)")

    # Optional: Compute overall risk (simple average)
    total_criteria = sum(len(crit_list) for crit_list in categories.values())
    total_risk_score = sum(c['Options'].index(selected_levels[f"{cat}_{c['Criteria']}"]) for cat, crit_list in categories.items() for c in crit_list)
    average_risk_index = total_risk_score / total_criteria
    overall_risk = risk_levels[int(average_risk_index)]

    st.header("Overall Risk Assessment")
    st.write(f"Based on the selections, the overall risk level is: **{overall_risk}**")
    
    # Add a simple visualization
    import matplotlib.pyplot as plt
    risk_counts = {level: 0 for level in risk_levels}
    for cat, crit_list in categories.items():
        for c in crit_list:
            selected = selected_levels[f"{cat}_{c['Criteria']}"]
            idx = c['Options'].index(selected)
            risk_counts[risk_levels[idx]] += 1
    
    fig, ax = plt.subplots()
    ax.bar(risk_counts.keys(), risk_counts.values(), color=['red', 'orange', 'yellow', 'green'])
    ax.set_title('Risk Level Distribution')
    ax.set_xlabel('Risk Level')
    ax.set_ylabel('Number of Criteria')
    st.pyplot(fig)
else:
    st.info("Please select the risk levels for each criterion in the sidebar and click 'Classify Supplier' to view the results.")