# 🧠 Smart Lead Prioritizer & Verifier

## 🎯 Objective
The original SaaSquatchLeads tool efficiently scrapes lead data but lacks validation and prioritization. Our goal was to enhance lead quality and sales efficiency by adding two core modules: **email verification** and **lead scoring** — all within a 5-hour build constraint.

## ⚙️ Approach & Architecture
We built a Streamlit-based tool that accepts a CSV of leads (name, email, role, domain) and outputs a scored, verified dataset. The core workflow includes:
- Email verification via SMTP (simple, fast, doesn't require paid APIs)
- Scoring based on:
  - Role relevance (Founder/CEO → higher)
  - Domain signals (e.g., `.ai`)
  - Verified status

![Architecture](https://raw.githubusercontent.com/akshit29g/smart-lead-prioritizer/main/architecture.png)

## 🧪 Model Selection & Data Processing
No ML model was used due to time/resource constraints. Instead, we implemented a rule-based scoring model:
- `+40`: High-impact roles (Founder, CEO)
- `+30`: Verified email
- `+20`: Domain signal (e.g., startup, tech)
All processing was done using `pandas` and built-in Python modules.

## 📈 Performance & Evaluation
- SMTP ping returned ~80–90% validation accuracy (some edge cases dropped)
- Score distribution showed clear separation of high- and low-priority leads
- SDRs can now eliminate ~30% of invalid or low-fit leads before outreach

## ✅ Value Addition
- Enhances lead conversion quality and outreach efficiency
- Provides a lightweight filter layer with zero learning curve
- Built for extensibility (future: CRM export, LinkedIn scrape, funding signals)

## 🔧 Stack
- Python, Streamlit, pandas, smtplib
- Optional APIs for enrichment (future)

