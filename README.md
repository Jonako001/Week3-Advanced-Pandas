## Day 13 Exercise: Mombasa Microfinance - Loan Repayment Analysis

**Dataset:** 150 fictional loan records (loan_id, amount_kes, days_to_first_repayment, county) - Mombasa region.

**Tasks Completed:**
1. **Typical loan amount** - Full statistical summary
   - Mean: 39,785 KES
   - Median: 33,921 KES (better typical value - less affected by large loans)
   - Std Dev: 26,664 KES
   - Q1: 25,326 KES, Q3: 45,764 KES

2. **Unusually large or small loans** - IQR Method
   - IQR = 20,438 KES
   - Normal range: 76,422 KES upper limit
   - **9 outliers found:** LN1005 (185,000), LN1017 (92,113), LN1023 (210,000), LN1031 (82,029), LN1044 (80,453), LN1055 (86,677), LN1069 (88,191), LN1077 (165,000), LN1092 (76,900)
   - These are unusually large loans requiring board review.

3. **Link between loan size and repayment time**
   - Correlation: **0.68** (moderate positive)

### For Board Members (Non-Technical):
> **"Larger loans tend to take slightly longer before the first repayment — customers who borrow more need a few extra days to start paying back. In our 150 loans, for every increase in loan size, we see borrowers taking a few more days to make their first payment."**

**Visual:** `loan_amounts_histogram.png` shows most loans cluster between 20k-50k KES, with a few very large loans above 150k KES.

**Files:**
- `day13_microfinance_mombasa.py` - Full analysis code
- `mombasa_microfinance_loans.csv` - Dataset
- `loan_amounts_histogram.png` - Distribution chart