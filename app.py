import streamlit as st
import pandas as pd
from lead_scoring import score_leads
from email_verifier import verify_email

st.title("🧠 Smart Lead Prioritizer & Verifier")

uploaded_file = st.file_uploader("Upload CSV with columns: name, email, role, domain", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("✅ Original Data", df.head())

    st.write("🔍 Verifying Emails & Scoring Leads...")

    df['verified'] = df['email'].apply(verify_email)
    df['score'] = df.apply(score_leads, axis=1)

    st.success("🎯 Done! Download your leads below.")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode()
    st.download_button("⬇ Download Scored Leads", csv, "scored_leads.csv", "text/csv")
