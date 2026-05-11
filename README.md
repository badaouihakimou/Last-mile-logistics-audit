# Last Mile Logistics Auditor  
## Veridi Logistics – Delivery Performance & Customer Satisfaction Analysis  

**Dataset:** Olist Brazilian E-Commerce Dataset  
**Tools:** Python · Pandas · Seaborn · Matplotlib · GeoPandas  

---

# Executive Summary

This project investigates last-mile delivery performance for Veridi Logistics using real e-commerce data from Brazil. The goal is to identify whether delivery delays are driven by regional inefficiencies, operational constraints, or seasonal demand spikes, and how these delays impact customer satisfaction.

The analysis reveals strong geographic disparities in logistics performance, with Northeast Brazilian states showing significantly higher late delivery rates compared to Southeastern regions. A clear and strong negative correlation is observed between delivery delays and customer review scores, confirming that late deliveries are a major driver of customer dissatisfaction. Additionally, recurring seasonal peaks during Black Friday, Carnival, and March 2018 indicate predictable operational stress periods that can be proactively managed.

Overall, the findings show that delivery performance is not a nationwide issue but rather concentrated in specific regions and time periods.

---

# Key Insights

- **Regional inequality:** Northeast states (AL, MA, PI, CE, SE) show late delivery rates ≥ 15%, compared to São Paulo at 5.9%
- **Customer impact:** Review score drops from **4.29 (On Time)** to **1.79 (Super Late)**
- **Operational risk:** 7,834 late deliveries (8.1% of total delivered orders)
- **Seasonality effect:** Major spikes observed during:
  - Black Friday (14.3%)
  - Carnival (16.0%)
  - March 2018 peak (21.4%)
- **Not a national issue:** Performance is highly uneven across regions

---

# Business Problem

Veridi Logistics suspected that customer dissatisfaction was linked to inaccurate delivery promises and inconsistent logistics performance.

This project answers three key business questions:
- Are delays caused by specific regions or system-wide failure?
- Do delays directly impact customer satisfaction?
- Can we predict or anticipate high-risk delivery periods?

---

# Technical Approach

## 1. Data Preparation
- Merged multiple relational datasets (orders, reviews, customers, products)
- Converted timestamp fields into proper datetime format
- Cleaned missing values and removed duplicate review entries
- Filtered dataset to include only delivered orders for analysis

## 2. Feature Engineering
- Created delivery delay metric:

  **Delay = Estimated Delivery Date − Actual Delivery Date**

- Classified delivery performance:
  - On Time
  - Late
  - Super Late (> 5 days delay)

## 3. Analytical Modules
- Geographic performance analysis (state-level heatmaps)
- Customer sentiment correlation analysis
- Seasonality and demand fluctuation analysis
- Distribution analysis of review scores
- Product category translation (Portuguese → English)

---

# Candidate’s Value-Added Analysis

To go beyond standard requirements, additional insights were developed:

### 1. Seasonality Risk Detection
Identified predictable demand spikes (Black Friday, Carnival) that significantly increase late delivery rates, enabling proactive logistics planning.

### 2. Review Score Distribution Deep Dive
Analyzed full distribution of customer ratings across delivery categories, confirming that delays disproportionately increase extreme negative reviews (1–2 stars).

---

# Key Business Conclusions

1. **Logistics inefficiency is geographically concentrated**, not systemic
2. **Delivery delays are a strong predictor of customer dissatisfaction**
3. **Operational planning should focus on seasonal peaks and high-risk regions**
4. **Improving delivery accuracy could significantly increase customer retention**

---

# Project Structure
