# Last Mile Logistics Auditor
### Veridi Logistics Delivery Performance & Customer Satisfaction Audit

> **"Are we failing specific regions, or is this a nationwide problem?"**  Veridi CEO

---

## Project Links

| Deliverable | Link |
|---|---|
| **Dashboard** | [Veridi Logistics Audit — Streamlit](https://last-mile-logistics-audit-ehhuvcwrvw6zxot5wvtqgz.streamlit.app/) |
| **Notebook** | [Google Colab](#) *(https://colab.research.google.com/drive/1AwUnp679FxzrCE2CGWaaKeyxAYWZfE2c?usp=sharing)* |
| **HTML** | https://htmlpreview.github.io/?https://github.com/badaouihakimou/Last-mile-logistics-audit/blob/main/Amalitech_Test.html |
| **Presentation** | https://docs.google.com/presentation/d/1wHkfYZKUvrhDMYI5lkwo79ZERZEHP9_Y/edit?usp=sharing&ouid=116024441528839692021&rtpof=true&sd=true |

---

## Executive Summary

This project audits last-mile delivery performance for **Veridi Logistics** using the real-world **Olist Brazilian E-Commerce Dataset** (96,478 delivered orders across 27 states, Oct 2016 – Aug 2018).

The analysis proves that **delivery delays are not a nationwide problem** they are concentrated in 5 Northeast states and predictable seasonal windows. Super Late deliveries cause review scores to collapse from **4.29 to 1.79 / 5**, confirming logistics is the primary driver of customer dissatisfaction.

| Finding | Detail |
|---|---|
| On Time Rate | **91.9%** : 88,644 orders |
| Late Rate | **3.7%** : 3,615 orders (1–5 days delay) |
| Super Late Rate | **4.4%** : 4,219 orders (>5 days delay) |
| Worst State | **AL (Alagoas) : 23.9% late** |
| Best State | **RO (Rondônia) : 2.9% late** |
| Peak Month | **March 2018 : 21.4% late** |

---

## Key Insights

### 1. Geographic Disparity : Not a Nationwide Problem
Northeast states are **systematically underserved**, with late rates up to 4× higher than São Paulo:

| State | Late Rate | Status |
|---|---|---|
| AL : Alagoas | 23.9% | Critical |
| MA : Maranhão | 19.7% | Critical |
| PI : Piauí | 16.0% | Critical |
| CE : Ceará | 15.3% | Critical |
| SE : Sergipe | 15.2% | Critical |
| SP : São Paulo | 5.9% | OK |
| RO : Rondônia | 2.9% | Best |

### 2. Delay Destroys Customer Satisfaction
A direct and measurable correlation between delays and negative reviews:

| Delivery Status | Avg Review Score | vs On Time |
|---|---|---|
| On Time | **4.29 / 5** | baseline |
| Late | **3.46 / 5** | −19% |
| Super Late | **1.79 / 5** | −58% |

> Over **60% of Super Late customers give a 1-star review** the distribution completely inverts compared to On Time orders.

### 3. Predictable Seasonal Spikes
Recurring high-risk windows that can be anticipated and prevented:

| Event | Month | Late Rate |
|---|---|---|
| Black Friday | Nov 2017 | 14.3% |
| Carnival | Feb 2018 | 16.0% |
| Post-Carnival Peak | Mar 2018 | **21.4% ** |

---

## Technical Approach

### Data Pipeline

```
5 CSV files (Olist)
    │
    ├── Reviews deduped by order_id (keep most recent)
    ├── Orders ← Reviews (left merge on order_id)
    ├── Orders ← Customers (left merge on customer_id)
    ├── Parse 5 datetime columns
    ├── Filter: order_status = 'delivered' only
    ├── Classify: On Time / Late / Super Late
    └── Translate: PT → EN product categories
    
Result: 96,478 clean rows, 27 states
```

### Story 1 : Schema Builder
Joined Orders + Reviews + Customers into a single master dataset.
- Reviews deduplicated by `order_id` before merging to prevent row duplication
- Verified: `len(master) == len(orders)` no duplicates introduced

### Story 2 : Delay Calculator
```python
days_difference = order_estimated_delivery_date - order_delivered_customer_date

On Time   : days_difference >= 0
Late      : -5 <= days_difference < 0
Super Late: days_difference < -5
```
- Excluded non-delivered orders (`order_status ≠ 'delivered'`)
- Handled missing values in delivery timestamps

### Story 3 : Geographic Heatmap
- Computed late delivery % per Brazilian state
- Visualized with 3 chart types: bar chart, bubble chart, and choropleth map (GeoPandas)
- Insight: Remote Northeast states disproportionately affected — geographic distance from São Paulo distribution hub is a key factor

### Story 4 : Sentiment Correlation
- Computed average review score by delivery status
- Visualized with bar chart, boxplot, and scatter plot (delay days vs review score)
- Confirmed: strong negative correlation between delay and satisfaction

### Bonus : PT → EN Translation
- Merged `product_category_name_translation.csv` to translate all Portuguese category names to English

---

## Candidate's Choice Additions

### Choice 1 : Seasonality Analysis
**Why it matters:** Knowing *when* delays spike allows Veridi to pre-position stock and increase carrier capacity **2–3 weeks before** Black Friday and Carnival preventing spikes instead of reacting after the damage is done.

The March 2018 peak (21.4%) likely reflects a compounded post-Carnival backlog. Staffing recovery plans should extend 4–6 weeks after the holiday period.

### Choice 2 : Review Score Distribution Deep Dive
**Why it matters:** Averages can hide severity. This analysis reveals that Super Late orders don't just lower the average — they generate a **1-star majority** (>60% of customers). This is a concrete severity metric that justifies infrastructure investment in the Northeast region to Veridi's CEO.

---

## Project Structure

```
Last-mile-logistics-audit/
├── app.py                         # Streamlit dashboard (6 pages)
├── requirements.txt               # Python dependencies
├── Amalitech_Test.ipynb           # Full analysis notebook
├── Amalitech_Test.html            # HTML export with all charts
├── Amalitech.pptx                 # Presentation slides
├── assets/                        # Chart images for dashboard
│   ├── choropleth_map.png
│   ├── delivery_status_overview.png
│   ├── geographic_bubble.png
│   ├── late_delivery_by_state.png
│   ├── review_distribution.png
│   ├── seasonality_analysis.png
│   └── sentiment_analysis.png
└── README.md
```

---

## Submission Checklist

- [x] GitHub Repo is Public
- [x] `.ipynb` notebook uploaded
- [x] HTML export uploaded
- [x] Raw dataset NOT uploaded
- [x] Code uses relative paths
- [x] Dashboard publicly accessible (no login required)
- [x] Presentation link publicly accessible
- [x] README updated with Executive Summary
- [x] User Stories 1–4 completed
- [x] Candidate's Choice completed and justified

---

**Dataset:** [Kaggle — Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  
**Tools:** Python · Pandas · Matplotlib · Seaborn · GeoPandas · Streamlit · Google Colab
