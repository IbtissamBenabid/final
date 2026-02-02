import streamlit as st
import pandas as pd

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

# Known suppliers list
known_suppliers = [
    # Tech Giants
    "Microsoft", "Google", "Apple", "Amazon", "Meta (Facebook)", "Tesla", "Netflix", "Uber", "Airbnb",
    # Cloud Providers
    "Amazon Web Services (AWS)", "Google Cloud Platform (GCP)", "Microsoft Azure", "IBM Cloud", "Alibaba Cloud", "Tencent Cloud",
    # Enterprise Software
    "Oracle", "SAP", "Salesforce", "Adobe", "Autodesk", "Intuit", "Workday", "ServiceNow", "Slack", "Zoom",
    # Hardware
    "Cisco", "HP", "Dell", "Lenovo", "ASUS", "Samsung", "LG", "Intel", "Nvidia", "AMD", "Qualcomm",
    # Telecom
    "Verizon", "AT&T", "Vodafone", "Orange", "Telefónica", "Deutsche Telekom", "China Mobile", "NTT",
    # Consulting & Professional Services
    "Accenture", "Deloitte", "PwC", "EY", "KPMG", "Capgemini", "TCS", "Infosys", "Wipro", "McKinsey", "BCG", "Bain",
    # Financial Services
    "JPMorgan Chase", "Goldman Sachs", "HSBC", "Bank of America", "Citigroup", "Wells Fargo", "Barclays",
    # Retail & E-commerce
    "Walmart", "Alibaba", "eBay", "Shopify", "Square", "PayPal",
    # Other
    "VMware", "Red Hat", "Siemens", "GE", "Boeing", "Lockheed Martin", "Pfizer", "Johnson & Johnson"
]

# Supplier selection
supplier_option = st.selectbox("Select Known Supplier or Choose Other", ["Other"] + known_suppliers, help="Choose from known suppliers or select 'Other' to enter custom name")

if supplier_option == "Other":
    supplier_name = st.text_input("Enter Supplier Name", placeholder="e.g., ABC Corp")
else:
    supplier_name = supplier_option

# Advanced mode toggle
advanced_mode = st.checkbox("Advanced Filters", help="Enable detailed risk selection per criterion")

if advanced_mode:
    # Advanced: filters in sidebar with expanders
    with st.sidebar.form("classification_form"):
        st.header("Advanced Risk Selection")
        selected_levels = {}
        for cat_name, criteria_list in categories.items():
            with st.expander(cat_name):
                for crit in criteria_list:
                    key = f"{cat_name}_{crit['Criteria']}"
                    selected_levels[key] = st.selectbox(
                        crit['Criteria'],
                        options=crit['Options'],
                        index=0,
                        key=key,
                        help=f"Select the most appropriate risk level for {crit['Criteria']}"
                    )
        
        submitted = st.form_submit_button("Classify Supplier", type="primary")
else:
    # Normal: filters in main area
    st.header("Select Overall Risk Levels")
    with st.form("classification_form"):
        selected_levels = {}
        st.write("Select overall risk level for each category:")
        for cat_name, criteria_list in categories.items():
            overall_risk = st.selectbox(
                f"Overall Risk for {cat_name}",
                options=risk_levels,
                index=0,
                key=f"overall_{cat_name}",
                help=f"Select the overall risk level for {cat_name}"
            )
            # Set all criteria in this category to the selected overall risk
            for crit in criteria_list:
                key = f"{cat_name}_{crit['Criteria']}"
                selected_levels[key] = crit['Options'][risk_levels.index(overall_risk)]
        
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