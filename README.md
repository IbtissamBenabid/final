# TPRM Supplier Classification Dashboard

A Streamlit-based web application for Third-Party Risk Management (TPRM) supplier classification and risk assessment.

## Features

### Supplier Selection
- Dropdown list of over 70 well-known suppliers across various industries
- Option to enter custom supplier names
- Pre-loaded risk profiles for major suppliers (Microsoft, Google, AWS, etc.)

### Risk Classification
- **7 Categories** of risk assessment based on industry standards:
  1. Supplier General Characteristics
  2. Geographical Risk Criteria
  3. Sector & Activity Criteria
  4. Information Security & Cyber Risk
  5. Business Continuity & Operational Risk
  6. Financial & Legal Risk
  7. ESG & Ethical Criteria

### Filter Modes
- **Normal Mode**: Quick assessment with overall risk selection per category
- **Advanced Mode**: Detailed selection for each of the 28 individual criteria

### Dynamic Features
- Filters automatically pre-fill based on selected supplier's known risk profile
- Real-time risk calculation and visualization
- Bar chart showing risk level distribution

### Results
- Detailed breakdown of selected risk levels
- Overall risk assessment
- Visual risk distribution chart

## Installation

1. Clone or download the project files
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to the provided local URL (usually http://localhost:8501)

3. Select a supplier from the dropdown or choose "Other" to enter a custom name

4. Choose between Normal or Advanced filtering mode

5. Adjust risk levels as needed

6. Click "Classify Supplier" to view results

## File Structure

- `app.py`: Main Streamlit application
- `suppliers_data.py`: Contains pre-assessed risk profiles for known suppliers
- `requirements.txt`: Python dependencies
- `README.md`: This file

## Customization

### Adding New Suppliers
Edit `suppliers_data.py` to add risk profiles for new suppliers:

```python
"New Supplier": {
    "Category_Criterion": "Selected Option",
    # ... all 28 criteria
}
```

### Modifying Risk Criteria
Update the `categories` dictionary in `app.py` to modify criteria or add new ones.

## Dependencies

- streamlit
- pandas
- matplotlib

## License

This project is for educational and demonstration purposes.

## Contributing

Feel free to submit issues or pull requests for improvements.