import streamlit as st
from PIL import Image
import os

# ── Asset path — works on Streamlit Cloud and locally ────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS   = os.path.join(BASE_DIR, "assets")

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Veridi Logistics — Delivery Audit",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* Background */
.stApp {
    background: #0d1117;
    color: #e6edf3;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #161b22;
    border-right: 1px solid #30363d;
}
section[data-testid="stSidebar"] * { color: #c9d1d9 !important; }
section[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    padding: 0.3rem 0;
}

/* Hero header */
.hero {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%);
    border: 1px solid #30363d;
    border-radius: 16px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(88,166,255,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.hero-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #58a6ff;
    margin-bottom: 0.5rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #f0f6fc;
    line-height: 1.1;
    margin-bottom: 0.75rem;
}
.hero-title span { color: #58a6ff; }
.hero-sub {
    font-size: 1rem;
    color: #8b949e;
    max-width: 600px;
    line-height: 1.6;
}

/* KPI Cards */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.kpi-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.kpi-card:hover { border-color: #58a6ff; }
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
}
.kpi-card.green::after  { background: #3fb950; }
.kpi-card.orange::after { background: #d29922; }
.kpi-card.red::after    { background: #f85149; }
.kpi-card.blue::after   { background: #58a6ff; }
.kpi-label {
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #8b949e;
    margin-bottom: 0.5rem;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #f0f6fc;
    line-height: 1;
}
.kpi-sub {
    font-size: 0.8rem;
    color: #8b949e;
    margin-top: 0.3rem;
}

/* Section headers */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #f0f6fc;
    margin-bottom: 0.25rem;
}
.section-sub {
    font-size: 0.85rem;
    color: #8b949e;
    margin-bottom: 1.25rem;
}

/* Chart containers */
.chart-box {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 1.25rem;
    margin-bottom: 1.25rem;
}
.chart-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #c9d1d9;
    margin-bottom: 1rem;
}

/* Insight callouts */
.insight {
    background: #1c2128;
    border-left: 3px solid #58a6ff;
    border-radius: 0 8px 8px 0;
    padding: 0.9rem 1.2rem;
    margin: 1rem 0;
    font-size: 0.88rem;
    color: #c9d1d9;
    line-height: 1.6;
}
.insight.warn  { border-left-color: #d29922; }
.insight.danger { border-left-color: #f85149; }
.insight strong { color: #f0f6fc; }

/* Finding badges */
.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin: 1rem 0;
}
.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
}
.badge.green  { background: rgba(63,185,80,0.15);  color: #3fb950; border: 1px solid rgba(63,185,80,0.3); }
.badge.orange { background: rgba(210,153,34,0.15); color: #d29922; border: 1px solid rgba(210,153,34,0.3); }
.badge.red    { background: rgba(248,81,73,0.15);  color: #f85149; border: 1px solid rgba(248,81,73,0.3); }
.badge.blue   { background: rgba(88,166,255,0.15); color: #58a6ff; border: 1px solid rgba(88,166,255,0.3); }

/* Divider */
.divider {
    border: none;
    border-top: 1px solid #30363d;
    margin: 1.5rem 0;
}

/* Findings table */
.findings-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}
.findings-table th {
    background: #1c2128;
    color: #8b949e;
    font-weight: 500;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.75rem 1rem;
    text-align: left;
    border-bottom: 1px solid #30363d;
}
.findings-table td {
    padding: 0.7rem 1rem;
    color: #c9d1d9;
    border-bottom: 1px solid #21262d;
}
.findings-table tr:last-child td { border-bottom: none; }
.findings-table tr:hover td { background: #1c2128; }
</style>
""", unsafe_allow_html=True)

# ── Asset loader ───────────────────────────────────────────────────────────────
def img(name):
    path = os.path.join(ASSETS, name)
    return Image.open(path) if os.path.exists(path) else None

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📦 Veridi Logistics")
    st.markdown("<div style='font-size:0.75rem;color:#8b949e;margin-bottom:1.5rem;'>Delivery Performance Audit</div>", unsafe_allow_html=True)

    page = st.radio("Navigation", [
        "🏠  Overview",
        "📊  Delivery Status",
        "🗺️  Geographic Analysis",
        "💬  Sentiment Analysis",
        "📅  Seasonality",
        "🔍  Deep Dive",
    ], label_visibility="collapsed")

    st.markdown("<hr style='border-color:#30363d;margin:1.5rem 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.75rem;color:#8b949e;line-height:1.8;'>
    <b style='color:#c9d1d9'>Dataset</b><br>
    Olist Brazilian E-Commerce<br>
    96,478 delivered orders<br>
    27 Brazilian states<br><br>
    <b style='color:#c9d1d9'>Period</b><br>
    Oct 2016 – Aug 2018
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if "Overview" in page:

    st.markdown("""
    <div class='hero'>
        <div class='hero-label'>Veridi Logistics · Delivery Audit · 2016–2018</div>
        <div class='hero-title'>Last Mile<br><span>Performance</span> Audit</div>
        <div class='hero-sub'>
            An end-to-end analysis of 96,478 delivered orders across 27 Brazilian states —
            connecting logistics data to customer sentiment to find the root cause of negative reviews.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI row
    st.markdown("""
    <div class='kpi-row'>
        <div class='kpi-card green'>
            <div class='kpi-label'>On Time Rate</div>
            <div class='kpi-value'>91.9%</div>
            <div class='kpi-sub'>88,644 orders</div>
        </div>
        <div class='kpi-card orange'>
            <div class='kpi-label'>Late Rate</div>
            <div class='kpi-value'>3.7%</div>
            <div class='kpi-sub'>3,615 orders · 1–5 days</div>
        </div>
        <div class='kpi-card red'>
            <div class='kpi-label'>Super Late Rate</div>
            <div class='kpi-value'>4.4%</div>
            <div class='kpi-sub'>4,219 orders · >5 days</div>
        </div>
        <div class='kpi-card blue'>
            <div class='kpi-label'>Worst State</div>
            <div class='kpi-value'>AL</div>
            <div class='kpi-sub'>Alagoas · 23.9% late</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Executive Summary
    st.markdown("<div class='section-header'>Executive Summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Key findings from the delivery performance audit</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class='insight danger'>
            <strong>🔴 Geographic Disparity — Not a Nationwide Problem</strong><br>
            5 Northeast states (AL, MA, PI, CE, SE) show a critical late rate ≥15%, while São Paulo stands at just 5.9%.
            This is a targeted regional failure, not a systemic collapse.
        </div>
        <div class='insight warn'>
            <strong>🟡 Delay Destroys Customer Satisfaction</strong><br>
            On-Time orders average <strong>4.29/5</strong> stars. Super Late orders collapse to <strong>1.79/5</strong> —
            a 58% drop in satisfaction. Late deliveries are the primary driver of negative reviews.
        </div>
        <div class='insight'>
            <strong>🔵 Predictable Seasonal Spikes</strong><br>
            Black Friday (14.3%), Carnival (16.0%), and March 2018 (21.4% peak) are recurring high-risk windows
            that can be anticipated and mitigated with proactive resource planning.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='chart-box'>
            <div class='chart-title'>Key Metrics at a Glance</div>
        """, unsafe_allow_html=True)

        findings = [
            ("Total Orders Audited", "96,478"),
            ("Avg Review (On Time)", "4.29 / 5"),
            ("Avg Review (Late)", "3.46 / 5"),
            ("Avg Review (Super Late)", "1.79 / 5"),
            ("Peak Late Month", "Mar 2018 · 21.4%"),
            ("Critical States (≥15%)", "AL, MA, PI, CE, SE"),
            ("Best Performing State", "RO · 2.9%"),
            ("National Late Avg", "8.1%"),
        ]
        rows = "".join(f"<tr><td>{k}</td><td style='text-align:right;color:#f0f6fc;font-weight:500'>{v}</td></tr>" for k, v in findings)
        st.markdown(f"<table class='findings-table'>{rows}</table>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Badge row
    st.markdown("""
    <div class='badge-row'>
        <span class='badge red'>AL · 23.9% late</span>
        <span class='badge red'>MA · 19.7% late</span>
        <span class='badge red'>PI · 16.0% late</span>
        <span class='badge red'>CE · 15.3% late</span>
        <span class='badge red'>SE · 15.2% late</span>
        <span class='badge green'>RO · 2.9% late</span>
        <span class='badge green'>SP · 5.9% late</span>
        <span class='badge blue'>National avg · 8.1%</span>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: DELIVERY STATUS
# ══════════════════════════════════════════════════════════════════════════════
elif "Delivery Status" in page:

    st.markdown("<div class='section-header'>📊 Delivery Status Distribution</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 2 — How often are we on time, late, or super late?</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='insight'>
        <strong>Formula:</strong> Days_Difference = Estimated Delivery Date − Actual Delivery Date<br>
        <strong>On Time</strong> ≥ 0 days &nbsp;|&nbsp; <strong>Late</strong> −5 to 0 days &nbsp;|&nbsp; <strong>Super Late</strong> &lt; −5 days
    </div>
    """, unsafe_allow_html=True)

    image = img("delivery_status_overview.png")
    if image:
        st.image(image, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='kpi-card green' style='text-align:center'>
            <div class='kpi-label'>On Time</div>
            <div class='kpi-value'>88,644</div>
            <div class='kpi-sub'>91.9% of orders</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='kpi-card orange' style='text-align:center'>
            <div class='kpi-label'>Late (1–5 days)</div>
            <div class='kpi-value'>3,615</div>
            <div class='kpi-sub'>3.7% of orders</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='kpi-card red' style='text-align:center'>
            <div class='kpi-label'>Super Late (>5 days)</div>
            <div class='kpi-value'>4,219</div>
            <div class='kpi-sub'>4.4% of orders</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class='insight warn' style='margin-top:1.25rem'>
        <strong>Key Takeaway:</strong> While 91.9% of orders are delivered on time, the <strong>8.1% late rate</strong>
        (7,834 orders) is highly concentrated in the Northeast region and specific seasonal windows —
        making this a solvable, targeted problem rather than a systemic failure.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GEOGRAPHIC ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif "Geographic" in page:

    st.markdown("<div class='section-header'>🗺️ Geographic Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 3 — Which states are failing customers?</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='insight danger'>
        <strong>The Northeast Crisis:</strong> AL (23.9%), MA (19.7%), PI (16.0%), CE (15.3%), SE (15.2%)
        all exceed the 15% critical threshold — more than 2.5× the national average of 8.1%.
        These states are geographically remote from the main distribution hub in São Paulo.
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🗺️ Choropleth Maps", "📊 Bar Chart by State", "🫧 Volume vs Late Rate"])

    with tab1:
        st.markdown("<div style='font-size:0.85rem;color:#8b949e;margin-bottom:0.75rem;'>On Time / Late / Super Late rates by state — the darker the red, the more critical the region.</div>", unsafe_allow_html=True)
        image = img("choropleth_map.png")
        if image:
            st.image(image, use_container_width=True)

    with tab2:
        st.markdown("<div style='font-size:0.85rem;color:#8b949e;margin-bottom:0.75rem;'>States ranked by late delivery rate. Red = Critical (≥15%), Orange = Warning (10–15%), Green = OK (&lt;10%).</div>", unsafe_allow_html=True)
        image = img("late_delivery_by_state.png")
        if image:
            st.image(image, use_container_width=True)

    with tab3:
        st.markdown("<div style='font-size:0.85rem;color:#8b949e;margin-bottom:0.75rem;'>States with high volume (SP) still perform well. High late rates are concentrated in low-volume remote states.</div>", unsafe_allow_html=True)
        image = img("geographic_bubble.png")
        if image:
            st.image(image, use_container_width=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='chart-box'>
            <div class='chart-title'>🔴 Critical States (≥15% late)</div>
            <table class='findings-table'>
                <tr><th>State</th><th>Late Rate</th><th>Status</th></tr>
                <tr><td>AL — Alagoas</td><td>23.9%</td><td><span class='badge red'>Critical</span></td></tr>
                <tr><td>MA — Maranhão</td><td>19.7%</td><td><span class='badge red'>Critical</span></td></tr>
                <tr><td>PI — Piauí</td><td>16.0%</td><td><span class='badge red'>Critical</span></td></tr>
                <tr><td>CE — Ceará</td><td>15.3%</td><td><span class='badge red'>Critical</span></td></tr>
                <tr><td>SE — Sergipe</td><td>15.2%</td><td><span class='badge red'>Critical</span></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='chart-box'>
            <div class='chart-title'>🟢 Best Performing States</div>
            <table class='findings-table'>
                <tr><th>State</th><th>Late Rate</th><th>Status</th></tr>
                <tr><td>RO — Rondônia</td><td>2.9%</td><td><span class='badge green'>OK</span></td></tr>
                <tr><td>AC — Acre</td><td>3.8%</td><td><span class='badge green'>OK</span></td></tr>
                <tr><td>AM — Amazonas</td><td>4.1%</td><td><span class='badge green'>OK</span></td></tr>
                <tr><td>AP — Amapá</td><td>4.5%</td><td><span class='badge green'>OK</span></td></tr>
                <tr><td>SP — São Paulo</td><td>5.9%</td><td><span class='badge green'>OK</span></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SENTIMENT ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif "Sentiment" in page:

    st.markdown("<div class='section-header'>💬 Sentiment Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Story 4 — Do late deliveries actually cause bad reviews?</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='kpi-card green' style='text-align:center'>
            <div class='kpi-label'>On Time · Avg Score</div>
            <div class='kpi-value'>4.29</div>
            <div class='kpi-sub'>out of 5.0</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='kpi-card orange' style='text-align:center'>
            <div class='kpi-label'>Late · Avg Score</div>
            <div class='kpi-value'>3.46</div>
            <div class='kpi-sub'>−19% vs On Time</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='kpi-card red' style='text-align:center'>
            <div class='kpi-label'>Super Late · Avg Score</div>
            <div class='kpi-value'>1.79</div>
            <div class='kpi-sub'>−58% vs On Time</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.25rem;'>", unsafe_allow_html=True)
    image = img("sentiment_analysis.png")
    if image:
        st.image(image, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header' style='font-size:1.1rem;'>Review Score Distribution by Status</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Candidate's Choice 2 — Understanding the full distribution of dissatisfaction</div>", unsafe_allow_html=True)

    image2 = img("review_distribution.png")
    if image2:
        st.image(image2, use_container_width=True)

    st.markdown("""
    <div class='insight danger'>
        <strong>The Super Late Collapse:</strong> For Super Late orders (n=4,219), over <strong>60% of customers give a 1-star review</strong>.
        The distribution is completely reversed compared to On Time orders where 5-stars dominate.
        This confirms that logistics delays are the primary driver of negative customer reviews.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SEASONALITY
# ══════════════════════════════════════════════════════════════════════════════
elif "Seasonality" in page:

    st.markdown("<div class='section-header'>📅 Seasonality Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Candidate's Choice 1 — When do delay spikes happen?</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='insight'>
        <strong>Business Value:</strong> Identifying seasonal patterns allows Veridi Logistics to proactively
        allocate resources during high-risk months — preventing delay spikes before they happen rather than
        reacting after customers are already frustrated.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='kpi-card orange' style='text-align:center'>
            <div class='kpi-label'>Black Friday 2017</div>
            <div class='kpi-value'>14.3%</div>
            <div class='kpi-sub'>Nov 2017</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='kpi-card red' style='text-align:center'>
            <div class='kpi-label'>Carnival 2018</div>
            <div class='kpi-value'>16.0%</div>
            <div class='kpi-sub'>Feb 2018</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='kpi-card red' style='text-align:center'>
            <div class='kpi-label'>Peak Month</div>
            <div class='kpi-value'>21.4%</div>
            <div class='kpi-sub'>Mar 2018 — all-time high</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.25rem;'>", unsafe_allow_html=True)
    image = img("seasonality_analysis.png")
    if image:
        st.image(image, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='insight warn'>
        <strong>Recommendation:</strong> Pre-position stock and increase carrier capacity <strong>2–3 weeks before</strong>
        Black Friday (November) and Carnival (February). The March 2018 peak (21.4%) likely reflects
        a compounded effect of post-Carnival backlog — staffing recovery plans should extend 4–6 weeks
        after the holiday period.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: DEEP DIVE
# ══════════════════════════════════════════════════════════════════════════════
elif "Deep Dive" in page:

    st.markdown("<div class='section-header'>🔍 Deep Dive — Methodology & Data</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Technical explanation of the audit approach</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='chart-box'>
            <div class='chart-title'>📐 Data Pipeline</div>
            <table class='findings-table'>
                <tr><th>Step</th><th>Action</th></tr>
                <tr><td>1. Load</td><td>5 CSV files from Olist dataset</td></tr>
                <tr><td>2. Deduplicate</td><td>Reviews deduped by order_id (keep latest)</td></tr>
                <tr><td>3. Join</td><td>Orders ← Reviews ← Customers (left merge)</td></tr>
                <tr><td>4. Clean</td><td>Parse 5 datetime columns, flag nulls</td></tr>
                <tr><td>5. Filter</td><td>Keep only order_status = 'delivered'</td></tr>
                <tr><td>6. Classify</td><td>On Time / Late / Super Late by days_difference</td></tr>
                <tr><td>7. Translate</td><td>PT → EN category names via lookup CSV</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='chart-box' style='margin-top:1rem;'>
            <div class='chart-title'>📊 Dataset Summary</div>
            <table class='findings-table'>
                <tr><th>Table</th><th>Rows</th></tr>
                <tr><td>olist_orders_dataset</td><td>99,441</td></tr>
                <tr><td>olist_order_reviews</td><td>100,000</td></tr>
                <tr><td>olist_customers</td><td>99,441</td></tr>
                <tr><td>olist_products</td><td>32,951</td></tr>
                <tr><td>After cleaning (delivered)</td><td><strong>96,478</strong></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='chart-box'>
            <div class='chart-title'>✅ User Stories Completed</div>
            <table class='findings-table'>
                <tr><th>Story</th><th>Status</th></tr>
                <tr><td>Story 1 · Schema Builder</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Story 2 · Delay Calculator</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Story 3 · Geographic Heatmap</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Story 4 · Sentiment Correlation</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Bonus · PT→EN Translation</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Candidate's Choice 1 · Seasonality</td><td><span class='badge green'>Done</span></td></tr>
                <tr><td>Candidate's Choice 2 · Score Distribution</td><td><span class='badge green'>Done</span></td></tr>
            </table>
        </div>

        <div class='chart-box' style='margin-top:1rem;'>
            <div class='chart-title'>🛠️ Tools Used</div>
            <div class='badge-row'>
                <span class='badge blue'>Python 3.10</span>
                <span class='badge blue'>Pandas</span>
                <span class='badge blue'>Matplotlib</span>
                <span class='badge blue'>Seaborn</span>
                <span class='badge blue'>GeoPandas</span>
                <span class='badge blue'>Streamlit</span>
                <span class='badge blue'>Google Colab</span>
            </div>
        </div>

        <div class='insight' style='margin-top:1rem;'>
            <strong>Candidate's Choice Justification:</strong><br>
            <strong>1. Seasonality</strong> — Enables proactive capacity planning before known high-risk periods
            (Black Friday, Carnival), directly reducing delay spikes and protecting revenue.<br><br>
            <strong>2. Review Distribution Deep Dive</strong> — Reveals that Super Late orders generate
            a 1-star majority (not just a lower average), giving the CEO a concrete severity metric
            to justify infrastructure investment in the Northeast.
        </div>
        """, unsafe_allow_html=True)
