import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Veridi Logistics — Delivery Audit",
    page_icon="📦",
    layout="wide",
)

RAW = "https://raw.githubusercontent.com/badaouihakimou/Last-mile-logistics-audit/main/assets"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #0d1117; color: #e6edf3; }
section[data-testid="stSidebar"] { background: #161b22; border-right: 1px solid #30363d; }
.block-container { padding-top: 1.5rem; }
.hero { background: #161b22; border: 1px solid #30363d; border-radius: 16px; padding: 2.5rem; margin-bottom: 1.5rem; }
.hero-label { font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; color: #58a6ff; margin-bottom: 0.5rem; }
.hero-title { font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800; color: #f0f6fc; line-height: 1.1; margin-bottom: 0.75rem; }
.hero-title span { color: #58a6ff; }
.hero-sub { font-size: 1rem; color: #8b949e; line-height: 1.6; }
.kpi { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 1.25rem 1.5rem; text-align: center; }
.kpi-label { font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: #8b949e; margin-bottom: 0.4rem; }
.kpi-value { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 700; color: #f0f6fc; }
.kpi-sub { font-size: 0.78rem; color: #8b949e; margin-top: 0.2rem; }
.insight { border-left: 3px solid #58a6ff; background: #1c2128; border-radius: 0 8px 8px 0; padding: 0.9rem 1.2rem; margin: 0.75rem 0; font-size: 0.88rem; color: #c9d1d9; line-height: 1.6; }
.insight.warn { border-left-color: #d29922; }
.insight.danger { border-left-color: #f85149; }
.insight strong { color: #f0f6fc; }
.section-title { font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 700; color: #f0f6fc; margin-bottom: 0.2rem; }
.section-sub { font-size: 0.85rem; color: #8b949e; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📦 Veridi Logistics")
    st.markdown("<div style='font-size:0.75rem;color:#8b949e;margin-bottom:1.5rem'>Delivery Performance Audit</div>", unsafe_allow_html=True)
    page = st.radio("Go to", [
        "🏠 Overview",
        "📊 Delivery Status",
        "🗺️ Geographic Analysis",
        "💬 Sentiment Analysis",
        "📅 Seasonality",
        "🔍 Deep Dive",
    ])
    st.markdown("<hr style='border-color:#30363d;margin:1.5rem 0'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.75rem;color:#8b949e;line-height:1.8'><b style='color:#c9d1d9'>Dataset</b><br>Olist Brazilian E-Commerce<br>96,478 delivered orders<br>27 Brazilian states<br><br><b style='color:#c9d1d9'>Period</b><br>Oct 2016 – Aug 2018</div>", unsafe_allow_html=True)

if "Overview" in page:
    st.markdown("<div class='hero'><div class='hero-label'>Veridi Logistics · Delivery Audit · 2016–2018</div><div class='hero-title'>Last Mile<br><span>Performance</span> Audit</div><div class='hero-sub'>An end-to-end analysis of 96,478 delivered orders across 27 Brazilian states — connecting logistics data to customer sentiment to find the root cause of negative reviews.</div></div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='kpi'><div class='kpi-label'>On Time Rate</div><div class='kpi-value' style='color:#3fb950'>91.9%</div><div class='kpi-sub'>88,644 orders</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='kpi'><div class='kpi-label'>Late Rate</div><div class='kpi-value' style='color:#d29922'>3.7%</div><div class='kpi-sub'>3,615 orders · 1–5 days</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='kpi'><div class='kpi-label'>Super Late Rate</div><div class='kpi-value' style='color:#f85149'>4.4%</div><div class='kpi-sub'>4,219 orders · >5 days</div></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='kpi'><div class='kpi-label'>Worst State</div><div class='kpi-value' style='color:#58a6ff'>AL</div><div class='kpi-sub'>Alagoas · 23.9% late</div></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Executive Summary</div>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("<div class='insight danger'><strong>🔴 Geographic Disparity — Not a Nationwide Problem</strong><br>5 Northeast states (AL, MA, PI, CE, SE) show a critical late rate ≥15%, while São Paulo stands at just 5.9%.</div><div class='insight warn'><strong>🟡 Delay Destroys Customer Satisfaction</strong><br>On-Time orders average <strong>4.29/5</strong> stars. Super Late orders collapse to <strong>1.79/5</strong> — a 58% drop.</div><div class='insight'><strong>🔵 Predictable Seasonal Spikes</strong><br>Black Friday (14.3%), Carnival (16.0%), and March 2018 (21.4% peak) are recurring high-risk windows.</div>", unsafe_allow_html=True)
    with col2:
        st.dataframe(pd.DataFrame({
            "Metric": ["Total Orders", "On Time Score", "Late Score", "Super Late Score", "Peak Month", "Critical States", "Best State", "National Avg"],
            "Value": ["96,478", "4.29 / 5", "3.46 / 5", "1.79 / 5", "Mar 2018 · 21.4%", "AL, MA, PI, CE, SE", "RO · 2.9%", "8.1%"]
        }), hide_index=True, use_container_width=True)

elif "Delivery Status" in page:
    st.markdown("<div class='section-title'>📊 Delivery Status Distribution</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 2 — On Time / Late / Super Late breakdown</div>", unsafe_allow_html=True)
    st.markdown("<div class='insight'><strong>Formula:</strong> Days_Difference = Estimated Date − Actual Date &nbsp;|&nbsp; On Time ≥0 · Late −5 to 0 · Super Late &lt;−5</div>", unsafe_allow_html=True)
    st.image(f"{RAW}/delivery_status_overview.png", use_column_width=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='kpi'><div class='kpi-label'>On Time</div><div class='kpi-value' style='color:#3fb950'>88,644</div><div class='kpi-sub'>91.9%</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='kpi'><div class='kpi-label'>Late</div><div class='kpi-value' style='color:#d29922'>3,615</div><div class='kpi-sub'>3.7%</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='kpi'><div class='kpi-label'>Super Late</div><div class='kpi-value' style='color:#f85149'>4,219</div><div class='kpi-sub'>4.4%</div></div>", unsafe_allow_html=True)

elif "Geographic" in page:
    st.markdown("<div class='section-title'>🗺️ Geographic Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 3 — Which states are failing customers?</div>", unsafe_allow_html=True)
    st.markdown("<div class='insight danger'><strong>The Northeast Crisis:</strong> AL (23.9%), MA (19.7%), PI (16.0%), CE (15.3%), SE (15.2%) — all exceed 15%, more than 2.5× the national average.</div>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["🗺️ Choropleth Maps", "📊 Bar Chart", "🫧 Bubble Chart"])
    with tab1:
        st.image(f"{RAW}/choropleth_map.png", use_column_width=True)
    with tab2:
        st.image(f"{RAW}/late_delivery_by_state.png", use_column_width=True)
    with tab3:
        st.image(f"{RAW}/geographic_bubble.png", use_column_width=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔴 Critical States**")
        st.dataframe(pd.DataFrame({"State": ["AL — Alagoas", "MA — Maranhão", "PI — Piauí", "CE — Ceará", "SE — Sergipe"], "Late Rate": ["23.9%", "19.7%", "16.0%", "15.3%", "15.2%"]}), hide_index=True, use_container_width=True)
    with c2:
        st.markdown("**🟢 Best States**")
        st.dataframe(pd.DataFrame({"State": ["RO — Rondônia", "AC — Acre", "AM — Amazonas", "AP — Amapá", "SP — São Paulo"], "Late Rate": ["2.9%", "3.8%", "4.1%", "4.5%", "5.9%"]}), hide_index=True, use_container_width=True)

elif "Sentiment" in page:
    st.markdown("<div class='section-title'>💬 Sentiment Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 4 — Do late deliveries cause bad reviews?</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='kpi'><div class='kpi-label'>On Time Score</div><div class='kpi-value' style='color:#3fb950'>4.29</div><div class='kpi-sub'>out of 5.0</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='kpi'><div class='kpi-label'>Late Score</div><div class='kpi-value' style='color:#d29922'>3.46</div><div class='kpi-sub'>−19% vs On Time</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='kpi'><div class='kpi-label'>Super Late Score</div><div class='kpi-value' style='color:#f85149'>1.79</div><div class='kpi-sub'>−58% vs On Time</div></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(f"{RAW}/sentiment_analysis.png", use_column_width=True)
    st.image(f"{RAW}/review_distribution.png", use_column_width=True)
    st.markdown("<div class='insight danger'><strong>Super Late Collapse:</strong> Over 60% of Super Late customers give a 1-star review — confirming delays are the primary driver of negative reviews.</div>", unsafe_allow_html=True)

elif "Seasonality" in page:
    st.markdown("<div class='section-title'>📅 Seasonality Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Candidate's Choice 1 — When do delay spikes happen?</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='kpi'><div class='kpi-label'>Black Friday 2017</div><div class='kpi-value' style='color:#d29922'>14.3%</div><div class='kpi-sub'>Nov 2017</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='kpi'><div class='kpi-label'>Carnival 2018</div><div class='kpi-value' style='color:#f85149'>16.0%</div><div class='kpi-sub'>Feb 2018</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='kpi'><div class='kpi-label'>Peak Month</div><div class='kpi-value' style='color:#f85149'>21.4%</div><div class='kpi-sub'>Mar 2018</div></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(f"{RAW}/seasonality_analysis.png", use_column_width=True)
    st.markdown("<div class='insight warn'><strong>Recommendation:</strong> Pre-position stock 2–3 weeks before Black Friday and Carnival to prevent delay spikes.</div>", unsafe_allow_html=True)

elif "Deep Dive" in page:
    st.markdown("<div class='section-title'>🔍 Deep Dive — Methodology</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**📐 Data Pipeline**")
        st.dataframe(pd.DataFrame({"Step": ["1. Load", "2. Deduplicate", "3. Join", "4. Clean", "5. Filter", "6. Classify", "7. Translate"], "Action": ["5 CSV files from Olist", "Reviews deduped by order_id", "Orders ← Reviews ← Customers", "Parse 5 datetime columns", "Keep status = 'delivered'", "On Time / Late / Super Late", "PT → EN category names"]}), hide_index=True, use_container_width=True)
        st.markdown("<br>**✅ Stories Completed**", unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({"Story": ["Story 1 · Schema Builder", "Story 2 · Delay Calculator", "Story 3 · Geographic Heatmap", "Story 4 · Sentiment", "Bonus · PT→EN", "Choice 1 · Seasonality", "Choice 2 · Score Distribution"], "Status": ["✅", "✅", "✅", "✅", "✅", "✅", "✅"]}), hide_index=True, use_container_width=True)
    with c2:
        st.markdown("**📊 Dataset**")
        st.dataframe(pd.DataFrame({"Table": ["olist_orders", "olist_reviews", "olist_customers", "olist_products", "After cleaning"], "Rows": ["99,441", "100,000", "99,441", "32,951", "96,478"]}), hide_index=True, use_container_width=True)
        st.markdown("<div class='insight'><strong>Candidate's Choice:</strong><br><strong>1. Seasonality</strong> — Enables proactive capacity planning.<br><strong>2. Score Distribution</strong> — Shows 1-star majority for Super Late orders, justifying Northeast investment.</div>", unsafe_allow_html=True)
