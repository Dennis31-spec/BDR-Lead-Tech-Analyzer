# 🛠️ BDR-Lead-Tech-Analyzer: Automating Technical Qualification

This repository contains a simple Python script designed to simulate a modern Business Development Representative's (BDR) initial technical discovery process. 

The goal is to automatically prioritize leads by assessing how well their current technology stack aligns with a developer-first platform, such as **Supabase**. This demonstrates both technical curiosity and a problem-solving approach to driving top-of-funnel activity.

---

## 🎯 Connecting Code to the BDR Role

The core of this project is the `calculate_supabase_fit_score` function in `analyzer.py`. The scoring criteria directly reflect the product knowledge required for effective technical qualification at Supabase:

| Criteria | Points | BDR Rationale | Supabase Service Alignment |
| :--- | :--- | :--- | :--- |
| **Current DB: PostgreSQL** | +3 | **Highest Priority:** Immediate architectural alignment, as Supabase is a Postgres development platform. Low friction for adoption. | **Database** |
| **Auth Method: Auth0/Custom** | +2 | Leads already using a separate auth service (Auth0, custom solution) have a clear pain point that Supabase's integrated Auth can solve, simplifying their stack. | **Auth** |
| **Scale Indicator: High** | +2 | High-growth companies require a robust, enterprise-grade solution. Postgres is trusted for scale. | **Commercial & Enterprise** |
| **Data Preference: Relational** | +1 | Easier transition to PostgreSQL (relational) than from a non-relational database like MongoDB. | **Database** |

---

## 💻 How to Run the Analysis

This project requires Python 3.x.

1. **Clone the repository:**
   ```bash
   git clone [YOUR_REPOSITORY_LINK]
   cd BDR-Lead-Tech-Analyzer
