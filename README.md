# Restaurant-Sales-Data-Restoration-Analysis
Turning dirty data into business intelligence. This project implements a Python cleaning workflow to handle severe data gaps, enabling accurate analysis of seasonal revenue trends and customer retention.

## 📌 Project Overview
This project is an end-to-end data analysis pipeline designed to extract actionable business intelligence from raw, real-world restaurant transaction logs. 

The primary goal was to bridge the gap between "messy" operational data and strategic decision-making. By building a robust preprocessing workflow to handle significant data gaps, this project uncovers key insights regarding **seasonal revenue trends, menu item performance, and customer loyalty dynamics.**

## 🎯 The Business Problem
The restaurant industry relies on thin margins and high volume. This analysis aimed to answer critical operational questions:
1.  **Seasonality:** When are the peak revenue periods?
2.  **Menu Engineering:** Which items and categories drive the most volume vs. revenue?
3.  **Customer Behavior:** Does loyalty status correlate with higher spend per ticket?
4.  **Infrastructure:** What are the dominant payment methods to inform future tech upgrades?

## 📊 Key Insights & Results
After processing the raw data, the analysis revealed:

* **📈 Seasonal Spikes:** A major revenue surge occurs in **March**, significantly outperforming Winter and Fall months. *Recommendation: Allocate marketing budget and inventory buffers specifically for Q1.*
* **🍔 Product Dominance:** "Beef Chili" is the highest-volume item, while Main Dishes drive the bulk of revenue.
* **👥 Customer Loyalty:** High retention rate (many recurring customers), but **Loyalty Status** showed no direct correlation with higher order totals. *Insight: The current loyalty program may need restructuring to incentivize higher spending.*
* **💳 Payment Trends:** Cash remains the dominant payment method, suggesting that digital transformation in this specific location may face friction.

## 🛠️ The Data Pipeline (Engineering Approach)
Real-world data is rarely analysis-ready. A significant portion of this project involved engineering a solution for a "dirty" dataset containing missing prices, items, and payment methods.

### 1. Ingestion & Audit
* Loaded raw CSV logs and performed an initial audit of null values and data types.
* Identified that ~30% of critical rows contained missing data that would skew financial results if simply dropped.

### 2. Intelligent Restoration (Preprocessing)
Instead of discarding incomplete records, I implemented a statistical imputation strategy:
* **Mathematical relationships:** Leveraged the correlation between `Price`, `Category`, and `Order Total`.
* **Algorithmic filling:** Utilized **K-Nearest Neighbors (KNN)** to mathematically infer missing menu items based on price clusters, preserving the dataset's volume and integrity.

### 3. Analysis & Visualization
* Aggregated time-series data to visualize monthly trends.
* Performed correlation analysis on customer segments vs. spending behavior.

## Dashboard Using Streamlit
 **Automated Dashboard:** Ported these static insights into a live Streamlit 


## How to Run
 ### 1. Clone the Repository
To get a local copy of the code, run the following command in your terminal:
```bash
git clone [https://github.com/bbb1/Restaurant-Sales-Data-Restoration-Analysis.git](https://github.com/bbb1/Restaurant-Sales-Data-Restoration-Analysis.git)
cd Restaurant-Sales-Data-Restoration-Analysis
### 2.Install Dependencies
pip install pandas numpy scikit-learn seaborn plotly jupyter streamlit
