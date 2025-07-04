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

    st.success("🎯 Scoring complete! Use filters below.")

    # Add visual tag for verification
    df['verified_status'] = df['verified'].apply(lambda x: '✅ Verified' if x else '❌ Unverified')

    # Filters
    st.subheader("🔎 Filter Leads")
    min_score = st.slider("Minimum Score", 0, 100, 50)
    show_verified = st.checkbox("Only show verified leads", value=True)

    filtered_df = df[df['score'] >= min_score]
    if show_verified:
        filtered_df = filtered_df[filtered_df['verified'] == True]

    display_df = filtered_df[['name', 'email', 'role', 'domain', 'verified_status', 'score']]
    st.dataframe(display_df)

    # Download final output
    csv = filtered_df.to_csv(index=False).encode()
    st.download_button("⬇ Download Filtered Leads", csv, "scored_leads.csv", "text/csv")
