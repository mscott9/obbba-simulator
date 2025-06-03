
import streamlit as st

st.set_page_config(page_title="OBBBA Budget Simulator", layout="centered")
st.title("🇺🇸 One Big Beautiful Bill – Budget Simulator")

st.markdown("Try to balance the bill by adjusting growth, tax capture, and spending items.")

# Presets
if st.sidebar.button("Use Trump Plan Preset"):
    gdp_growth = 3.0
    revenue_capture_rate = 18.0
    social_cuts = 0.4
    new_defense_spend = 0.22
    tax_credit_expansion = 0.4
elif st.sidebar.button("Use Balanced Budget Preset"):
    gdp_growth = 2.5
    revenue_capture_rate = 20.0
    social_cuts = 1.2
    new_defense_spend = 0.1
    tax_credit_expansion = 0.2
else:
    gdp_growth = st.slider("Annual GDP Growth Rate (%)", 0.0, 7.0, 2.0, step=0.1)
    revenue_capture_rate = st.slider("Tax Revenue Capture (% of new GDP)", 10.0, 25.0, 18.0, step=0.1)
    social_cuts = st.slider("Spending Cuts from Social Programs ($ Trillions)", 0.0, 2.0, 0.5, step=0.1)
    new_defense_spend = st.slider("Defense & Border Spending ($ Trillions)", 0.0, 0.5, 0.22, step=0.01)
    tax_credit_expansion = st.slider("Child Tax Credit & MAGA Savings Expansion ($ Trillions)", 0.0, 1.0, 0.4, step=0.05)

# Constants
TAX_CUT_COST = 2.7  # in trillions
GDP_BASE = 30.0     # in trillions

# Calculate revenue
gdp_multiplier = ((1 + gdp_growth / 100) ** 10) - 1
added_gdp = GDP_BASE * gdp_multiplier
revenue_from_growth = added_gdp * (revenue_capture_rate / 100)

# Final cost in trillions
total_cost = TAX_CUT_COST + new_defense_spend + tax_credit_expansion
total_savings = social_cuts + (revenue_from_growth / 1e12)
net_deficit = total_cost - total_savings

# Output
st.subheader("📊 10-Year Budget Result")
if net_deficit > 0:
    st.error(f"🚨 Estimated Deficit: ${net_deficit:.2f} Trillion")
elif net_deficit < 0:
    st.success(f"✅ Estimated Surplus: ${-net_deficit:.2f} Trillion")
else:
    st.success("🎯 Balanced Budget Achieved!")

# Breakdown
st.markdown("### 🧾 Breakdown")
st.markdown(f"- **Tax Cuts Extended**: ${TAX_CUT_COST:.2f}T")
st.markdown(f"- **Defense & Border**: ${new_defense_spend:.2f}T")
st.markdown(f"- **Tax Credit Expansion**: ${tax_credit_expansion:.2f}T")
st.markdown(f"- **Social Program Cuts**: ${social_cuts:.2f}T")
st.markdown(f"- **Revenue from Growth**: ${revenue_from_growth / 1e12:.2f}T")
