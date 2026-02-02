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

def risk_assessment_page():
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
        # Enhanced search with autocomplete and case-insensitive matching
        supplier_input = st.text_input(
            "Search Supplier",
            placeholder="Start typing supplier name...",
            help="Type to search suppliers or enter custom name. Search is case-insensitive with autocomplete suggestions."
        )

        # Case-insensitive search and autocomplete
        if supplier_input:
            # Find matching suppliers (case-insensitive)
            input_lower = supplier_input.lower()
            matching_suppliers = [
                name for name in suppliers_data.keys()
                if input_lower in name.lower()
            ]

            # Exact match (case-insensitive)
            exact_matches = [name for name in suppliers_data.keys() if name.lower() == input_lower]

            if exact_matches:
                # Use the exact match from database (preserve original casing)
                supplier_name = exact_matches[0]
            elif matching_suppliers:
                # Show autocomplete suggestions
                st.markdown("**Suggestions:**")
                selected_suggestion = st.selectbox(
                    "Select from suggestions or continue typing:",
                    [""] + matching_suppliers,
                    help="Choose a suggested supplier or keep typing for a custom name"
                )
                if selected_suggestion:
                    supplier_name = selected_suggestion
                else:
                    supplier_name = supplier_input
            else:
                # No matches found, use as custom name
                supplier_name = supplier_input
        else:
            supplier_name = ""

    # Show company info if supplier is found
    if supplier_name and supplier_name in suppliers_data:
        supplier_info = suppliers_data[supplier_name]["metadata"]

        # Enhanced company information display
        st.success(f"**{supplier_name}** - Company Profile Found!")

        # Company overview card
        with st.container():
            st.markdown("### Company Overview")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("**Sector**")
                st.markdown(f"*{supplier_info['sector']}*")
                # Add sector-specific insights
                if supplier_info['sector'] == 'Technology':
                    st.caption("Software & digital solutions")
                elif supplier_info['sector'] == 'Financial Services':
                    st.caption("Banking & financial services")
                elif supplier_info['sector'] == 'Healthcare':
                    st.caption("Medical & pharmaceutical")
                elif supplier_info['sector'] == 'Consulting & Professional Services':
                    st.caption("Business consulting")
                else:
                    st.caption("Industrial & manufacturing")

            with col2:
                st.markdown("**Geography**")
                st.markdown(f"*{supplier_info['geography']}*")
                # Add geographical insights
                if supplier_info['geography'] in ['USA', 'Germany', 'UK']:
                    st.caption("Western markets")
                elif supplier_info['geography'] in ['China', 'India', 'South Korea', 'Japan']:
                    st.caption("Emerging markets")
                else:
                    st.caption("Global operations")

            with col3:
                st.markdown("**Company Size**")
                st.markdown(f"*{supplier_info['size']}*")
                # Add size insights
                if supplier_info['size'] == 'Large':
                    st.caption("Enterprise-level operations")
                elif supplier_info['size'] == 'Multinational':
                    st.caption("Global presence")
                else:
                    st.caption("Growing organization")

        # Risk assessment readiness
        st.markdown("### Risk Assessment Ready")
        st.info("Pre-filled risk profiles available for this supplier. You can adjust the assessments in the sidebar as needed.")

        # Load supplier profile if available
        supplier_profile = suppliers_data.get(supplier_name, {}).get("profile", {})
    elif supplier_name and supplier_name not in suppliers_data:
        st.info(f"**{supplier_name}** not found in database. Proceeding with manual risk assessment.")
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

def system_presentation_page():
    st.title("TPRM System Overview & Presentation")

    # Risk Criteria Overview - Detailed presentation
    st.markdown("## 🔍 Risk Assessment Framework - Detailed Analysis")

    # Create comprehensive criteria table with risk levels
    st.markdown("### Complete Risk Criteria Matrix")

    # Create detailed criteria DataFrame
    detailed_criteria = []
    for category_name, criteria_list in categories.items():
        for criterion in criteria_list:
            # Add risk level mapping for each option
            risk_mapping = {}
            for i, option in enumerate(criterion['Options']):
                risk_mapping[option] = risk_levels[i]

            detailed_criteria.append({
                "Category": category_name.replace("️⃣", "").strip(),
                "Criteria": criterion["Criteria"],
                "Critical Risk": criterion["Options"][0],
                "High Risk": criterion["Options"][1],
                "Medium Risk": criterion["Options"][2],
                "Low Risk": criterion["Options"][3]
            })

    criteria_df = pd.DataFrame(detailed_criteria)
    st.dataframe(criteria_df, use_container_width=True)

   

    # Category breakdown
    st.markdown("### Categories Overview")
    category_data = []
    for cat_name, criteria_list in categories.items():
        category_data.append({
            "Category": cat_name.replace("️⃣", "").strip(),
            "Criteria Count": len(criteria_list),
            "Coverage": f"{len(criteria_list)} criteria"
        })

    cat_df = pd.DataFrame(category_data)
    st.dataframe(cat_df, use_container_width=True)

    st.markdown("---")

   

   

    

# Main navigation
pages = {
    "Risk Assessment": risk_assessment_page,
    "System Presentation": system_presentation_page
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", list(pages.keys()))

# Run the selected page
pages[page]()