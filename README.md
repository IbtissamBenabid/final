# TPRM Supplier Classification Dashboard

A comprehensive Streamlit-based web application for Third-Party Risk Management (TPRM) supplier classification and risk assessment with advanced filtering and company intelligence features.

## Application Structure

This application consists of two separate pages/windows:

### 1. Risk Assessment Page
The main operational interface for conducting supplier risk assessments.

### 2. System Presentation Page
A dedicated presentation window showcasing the complete TPRM framework, classification criteria, and system capabilities.

## Features

### Smart Supplier Selection
- **Dual Selection Modes**:
  - **Dropdown Selection**: Choose from filtered suppliers in the database
  - **Custom Input**: Enter any supplier name for assessment
- **Company Intelligence**: Instant display of sector, geography, and size for known suppliers
- **Dynamic Filtering**: Sector and geography filters that update available suppliers in real-time

### Comprehensive Risk Classification
- **7 Risk Categories** with **28 individual criteria**:
  1. **Supplier General Characteristics** (Criticality, Size, Activity, Dependency)
  2. **Geographical Risk Criteria** (Country Risk, Data Hosting, Regulatory Alignment, Cross-border Flow)
  3. **Sector & Activity Criteria** (Sector Sensitivity, Service Type, System Access, Process Outsourcing)
  4. **Information Security & Cyber Risk** (Data Sensitivity, Security Certification, Incident History, Access Management)
  5. **Business Continuity & Operational Risk** (BCP/DRP, RTO/RPO, SLA Availability, Subcontracting)
  6. **Financial & Legal Risk** (Financial Stability, Legal Compliance, Insurance, Litigation History)
  7. **ESG & Ethical Criteria** (Ethics Policy, Anti-corruption, Environmental Impact, Social Responsibility)

### Global Supplier Database
- **23 Major Suppliers** from **8 Countries**:
  - **USA**: Microsoft, Google, Apple, Oracle, Cisco, Accenture, JPMorgan Chase, Verizon, Pfizer
  - **Germany**: SAP, Siemens
  - **Ireland**: Salesforce, Accenture
  - **China**: Alibaba, Tencent
  - **India**: Reliance Industries
  - **South Korea**: Samsung
  - **Japan**: Toyota
  - **UK**: Unilever

### Advanced Risk Assessment
- **Pre-filled Profiles**: Automatic risk assessment loading for known suppliers
- **Manual Assessment**: Complete flexibility for custom suppliers
- **Real-time Calculation**: Dynamic risk scoring and visualization
- **Risk Distribution Chart**: Visual breakdown of risk levels across all criteria

### Interactive Dashboard
- **Sector & Geography Filters**: Narrow down suppliers by industry and location
- **Available Suppliers Display**: See which suppliers match your current filters
- **Responsive Design**: Clean, professional interface optimized for risk management workflows

### System Presentation Window
- **Complete Framework Overview**: Detailed presentation of all 7 risk categories and 28 criteria
- **Risk Level Matrix**: Visual breakdown of risk levels for each criterion
- **System Capabilities**: Comprehensive overview of assessment features and technical architecture
- **Usage Instructions**: Step-by-step guidance for both assessment and system administration
- **Professional Presentation**: Enterprise-ready format for compliance and audit purposes

## Installation

1. **Clone or download** the project files to your local machine

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Python environment** (Python 3.7+ recommended)

## Usage

### Navigation
The application features two separate pages/windows accessible via the sidebar navigation:
- **Risk Assessment**: Main operational interface for supplier evaluations
- **System Presentation**: Dedicated presentation window for framework overview and system capabilities

### Getting Started
1. **Launch the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to the provided URL (usually `http://localhost:8501`)

3. **Navigate**: Use the sidebar radio buttons to switch between pages

### Supplier Assessment Workflow

#### Option 1: Database Supplier Selection
1. **Apply Filters** (optional): Use sector and geography filters to narrow down suppliers
2. **Select Mode**: Choose "Select from dropdown"
3. **Pick Supplier**: Select from the filtered dropdown list
4. **Review Company Info**: View sector, geography, and size automatically displayed
5. **Adjust Risk Levels**: Modify pre-filled assessments in the sidebar as needed

#### Option 2: Custom Supplier Assessment
1. **Select Mode**: Choose "Enter custom name"
2. **Type Supplier Name**: Enter any supplier name
3. **Manual Assessment**: Complete all 28 criteria in the sidebar form
4. **Proceed**: Click "Classify Supplier" for results

#### Risk Assessment
1. **Expand Categories**: Use sidebar expanders to access all 7 risk categories
2. **Select Risk Levels**: Choose appropriate risk level for each of the 28 criteria
3. **Generate Results**: Click "Classify Supplier" to view comprehensive analysis

### Understanding Results
- **Detailed Breakdown**: Risk level for each individual criterion
- **Overall Assessment**: Aggregated risk score across all categories
- **Visual Distribution**: Bar chart showing risk level distribution
- **Export Ready**: Results suitable for reporting and documentation

## Project Structure

```
├── app.py                 # Main Streamlit application
├── suppliers_data.py      # Comprehensive supplier database with risk profiles
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── __pycache__/          # Python cache files (auto-generated)
```

## Customization

### Adding New Suppliers
Edit `suppliers_data.py` to add new supplier profiles:

```python
"New Company Name": {
    "metadata": {
        "sector": "Industry Sector",
        "geography": "Country",
        "size": "Company Size"
    },
    "profile": {
        "1️⃣ Supplier General Characteristics_Supplier criticality": "Selected Option",
        "1️⃣ Supplier General Characteristics_Supplier size": "Selected Option",
        # ... complete all 28 criteria
    }
}
```

### Modifying Risk Criteria
Update the `categories` dictionary in `app.py` to modify existing criteria or add new ones.

### Database Expansion
- Add suppliers from new geographical regions
- Include additional industry sectors
- Update risk profiles based on new assessments

## Requirements

- **Python**: 3.7 or higher
- **Streamlit**: Latest stable version
- **pandas**: For data manipulation
- **matplotlib**: For visualization

## Use Cases

- **Risk Management Teams**: Comprehensive supplier risk assessments
- **Procurement Departments**: Pre-qualification of new suppliers
- **Compliance Officers**: Regulatory compliance verification
- **Security Teams**: Third-party security risk evaluation
- **ESG Analysts**: Ethical and sustainability assessments

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Areas for Enhancement
- Additional supplier profiles
- New risk categories or criteria
- Enhanced visualization options
- Export functionality (PDF/Excel reports)
- Integration with external risk databases

## License

This project is for educational and demonstration purposes. Please ensure compliance with your organization's data usage policies when using in production environments.

## Support

For questions or issues:
- Check the troubleshooting section below
- Review the code comments in `app.py`
- Submit an issue on the project repository

## Troubleshooting

### Common Issues
- **App won't start**: Ensure all dependencies are installed (`pip install -r requirements.txt`)
- **No suppliers showing**: Check that filters aren't too restrictive
- **Risk calculation errors**: Verify all 28 criteria have valid selections

### Performance Tips
- The app is optimized for up to 100+ suppliers
- For very large datasets, consider database integration
- Use filters to improve performance with many suppliers

---

Built for comprehensive third-party risk management