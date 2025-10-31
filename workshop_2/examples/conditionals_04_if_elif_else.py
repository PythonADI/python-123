credit_score = 760
annual_income = 100_000
has_outstanding_debt = True

if credit_score >= 760 and annual_income >= 85000 and not has_outstanding_debt:
    print("Loan status: Preferred customer offer unlocked.")
elif credit_score >= 700 and annual_income >= 50000 and not has_outstanding_debt:
    print("Loan status: Approved with standard rates.")
elif credit_score >= 650 and annual_income >= 40000:
    print("Loan status: Conditional approval pending review.")
else:
    print("Loan status: Not approved at this time.")
