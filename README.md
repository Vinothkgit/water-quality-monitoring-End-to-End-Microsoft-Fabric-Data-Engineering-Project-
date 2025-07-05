# water-quality-monitoring-End-to-End-Microsoft-Fabric-Data-Engineering-Project-
# 💧 Water Quality Monitoring and Lead Alert System (EPA-Inspired)

A full-stack Microsoft Fabric project for analyzing lead contamination in U.S. water bodies. This project leverages Medallion Architecture, Spark SQL notebooks, and Power BI for public health analytics — inspired by EPA compliance standards.
---
## 📊 Project Overview

This project simulates a real-world **environmental data engineering pipeline**, where lead concentration data is ingested, transformed, and visualized using modern data lakehouse practices.
--
## 🛠️ Tech Stack
- **Microsoft Fabric** (OneLake + Lakehouse)
- **Apache Spark (Spark SQL Notebooks)**
- **Power BI** (Direct Lake Semantic Model)
- **Delta Lake (Medallion Architecture)**
- **Python** (Data Ingestion via API)
- **GitHub** (Project Portfolio)
---
> **Note:** Data is fetched via Python and manually loaded to Bronze. All transformation logic is handled in Fabric notebooks using Spark SQL.
---
## 🧪 Medallion Architecture Workflow

### 🔹 Step 1: Data Ingestion (Bronze Layer)
- Python script fetches EPA-like batch data (CSV).
- File uploaded to Microsoft Fabric Lakehouse under `/Files/Bronze/Lead/`.

### 🔹 Step 2: Silver Layer – Data Cleaning
- Converted to Delta Table `Silver_Lead`.
- Null handling, type casting, new field generation (`lead_ppb`, `lead_risk_level`, `sample_date`).

### 🔹 Step 3: Gold Layer – Business Logic & Aggregations

Created the following Gold Delta Tables:

1. **Yearly Lead Summary per Location**
2. **Monthly Average Lead Levels**
3. **Locations with Consistent Unsafe Lead Levels**
4. **Exceedance Events (Above 15 µg/L)**
5. **Completeness Report**
6. **Lead Risk Categorization**

---

## 📈 Power BI Dashboard

A rich visual analytics report built in Power BI with:
- **Unsafe lead locations map**
- **Trend lines per location**
- **Monthly averages**
- **Exceedance alerts**
> Report connects via **Direct Lake Mode** for real-time updates.
---
## 🌟 Key Highlights
- ✅ Realistic, end-to-end Fabric Data Engineering Pipeline
- ✅ Spark SQL transformations (no Dataflows or Pipelines used)
- ✅ Insightful gold tables optimized for decision-making
- ✅ Professional Power BI dashboards
- ✅ GitHub-ready with visual storytelling

## 📚 Learning Outcomes
- Building scalable data pipelines using Medallion Architecture
- Spark SQL for real-time data modeling
- Microsoft Fabric integration with Power BI
- Effective data storytelling for public health

## 🤝 Let’s Connect

**Have feedback or want to collaborate? Feel free to connect or fork this project!**
---
> 🚨 **Disclaimer:** This project uses publicly available EPA-style data for learning and demo purposes only.

💡 Future Scope
Automate pipeline using Fabric Data Factory
Integrate alerting via Power BI + Data Activator
Connect live API feed for real-time streaming

🙋‍♂️ Author
Vinoth
LinkedIn: https://www.linkedin.com/in/vino-r-mt/
Email: rvkmt15@gmail.com
