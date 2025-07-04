def score_leads(row):
    score = 0
    if row['role']:
        role = row['role'].lower()
        if any(x in role for x in ['founder', 'ceo', 'growth']):
            score += 40
        elif any(x in role for x in ['marketing', 'sales']):
            score += 20

    if row['verified']:
        score += 30

    if row['domain'] and "ai" in row['domain'].lower():
        score += 20

    return score
