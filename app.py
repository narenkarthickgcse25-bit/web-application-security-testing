import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Web Security Testing",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Web Application Security Testing")
st.write("Python-based Security Assessment Dashboard")

st.info(
    "Educational project using controlled local Python simulations. "
    "These are not verified production vulnerabilities."
)

# Vulnerability findings
data = [
    {
        "ID": "VULN-001",
        "Vulnerability": "Insecure Password Storage",
        "Risk": "High",
        "Status": "Open"
    },
    {
        "ID": "VULN-002",
        "Vulnerability": "SQL Injection Simulation",
        "Risk": "High",
        "Status": "Fixed and Retested"
    },
    {
        "ID": "VULN-003",
        "Vulnerability": "XSS Simulation",
        "Risk": "High",
        "Status": "Fixed and Retested"
    },
    {
        "ID": "VULN-004",
        "Vulnerability": "Input Validation Observation",
        "Risk": "Medium",
        "Status": "Remediation Required"
    },
    {
        "ID": "VULN-005",
        "Vulnerability": "Security Headers Observation",
        "Risk": "Medium",
        "Status": "Remediation Required"
    },
    {
        "ID": "VULN-006",
        "Vulnerability": "Session Security Assessment",
        "Risk": "Informational",
        "Status": "Basic Checks Passed"
    }
]

df = pd.DataFrame(data)

# Summary
st.header("📊 Security Assessment Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Findings", len(df))
col2.metric("High Risk", len(df[df["Risk"] == "High"]))
col3.metric("Medium Risk", len(df[df["Risk"] == "Medium"]))
col4.metric(
    "Informational",
    len(df[df["Risk"] == "Informational"])
)

# Risk chart
st.header("Risk Level Analysis")

risk_counts = df["Risk"].value_counts()

st.bar_chart(risk_counts)

# Findings table
st.header("🔍 Vulnerability Findings")

st.dataframe(df, use_container_width=True)

# Recommendations
st.header("🛠️ Recommended Security Fixes")

recommendations = {
    "VULN-001": "Store passwords using Argon2id or bcrypt hashing.",
    "VULN-002": "Use parameterized SQL queries.",
    "VULN-003": "Use context-aware HTML output encoding.",
    "VULN-004": "Implement server-side validation and input limits.",
    "VULN-005": "Configure appropriate HTTP security headers.",
    "VULN-006": "Use secure cookies, session rotation and expiration."
}

for vuln_id, recommendation in recommendations.items():
    st.write(f"**{vuln_id}:** {recommendation}")

# Download report
st.header("📥 Download Vulnerability Report")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="security_vulnerability_report.csv",
    mime="text/csv"
)

st.success("Security Assessment Dashboard Loaded Successfully!")

st.caption("Educational Python Security Testing Project")
