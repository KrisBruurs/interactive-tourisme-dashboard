# Global Tourism Dashboard 🌍

A portfolio project showcasing interactive data visualization and dashboard development skills using Streamlit and Plotly. This project demonstrates the ability to create dynamic, user-friendly dashboards with features like interactive world maps, dual-axis charts, and real-time filtering.

## Project Overview

This interactive dashboard explores the relationship between global tourism revenue and GDP growth across different countries and years. While the focus is on demonstrating dashboard development capabilities rather than data perfection, the project showcases key skills in:

- **Interactive Visualizations**: Choropleth maps with custom color scales and hover tooltips
- **User Interface Design**: Multi-tab layouts, dropdowns, sliders, and responsive controls
- **Data Processing**: ETL pipeline from raw data to dashboard-ready datasets
- **Multi-Chart Comparisons**: Dual-axis line charts for country-specific trend analysis

## Features

### 🗺️ World Map Tab
- Interactive choropleth map visualizing tourism revenue or GDP growth by country
- Year slider to explore temporal changes
- Metric selector to toggle between GDP growth and tourism revenue
- Custom color scales and hover information

### 📊 Country Comparison Tab
- Dual-axis line chart comparing GDP growth and tourism revenue over time
- Country selector to analyze specific nations
- Clear trend visualization across multiple years

## Technologies Used

- **Streamlit**: Dashboard framework
- **Plotly**: Interactive visualizations (choropleth maps, line charts)
- **Pandas**: Data manipulation and processing
- **KaggleHub**: Dataset download and management

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Bash shell (Git Bash, WSL, or native Linux/Mac terminal)
- Make utility

### Installation & Running

**Note**: This project uses a Makefile and should be run in a Bash environment.

1. **Clone the repository** (or download the project files)

2. **Install dependencies**:
   ```bash
   make requirements
   ```

3. **Download the dataset**:
   ```bash
   make download_data
   ```

4. **Transform the data**:
   ```bash
   make transform_data
   ```

5. **Run the dashboard**:
   ```bash
   make dashboard
   ```

6. **Open your browser** and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

### Optional: Remove Data Files

To clean up downloaded data files:
```bash
make remove_data
```

## Project Structure

```
interactive-tourisme-dashboard/
├── app.py                          # Main Streamlit dashboard application
├── download_data.py                # Script to download dataset from Kaggle
├── transform_data.py               # Data transformation pipeline
├── eda.ipynb                       # Exploratory data analysis notebook
├── requirements.txt                # Python dependencies
├── Makefile                        # Build automation
├── README.md                       # Project documentation
└── data/                           # Data directory (created on first run)
    ├── tourism_data.csv            # Raw downloaded data
    └── transformed_tourism_data.csv # Processed data
```

## Data Source

The dataset is sourced from Kaggle: [Global Tourism Revenue and GDP Growth Dataset](https://www.kaggle.com/datasets/abidhussai512/global-tourism-revenue-and-gdp-growth-dataset)

**Note**: This project prioritizes showcasing dashboard development skills. While the data provides meaningful insights, there may be minor inconsistencies or gaps in the dataset.

## Development Notes

This project was developed as a portfolio piece to demonstrate:
- Building interactive dashboards with Streamlit
- Creating complex visualizations with Plotly
- Data pipeline development (download → transform → visualize)
- UI/UX design for data exploration tools
- Automation with Makefiles

## Future Enhancements

Potential improvements for future iterations:
- Add more statistical analysis and correlations
- Include additional metrics (e.g., visitor numbers, average spend)
- Implement data caching for improved performance
- Add export functionality for charts and filtered data
- Expand comparison capabilities (multi-country comparisons)

## License

This project is available for educational and portfolio purposes.

## Contact

Feel free to reach out with questions or feedback about this portfolio project!
