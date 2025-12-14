import json

# --- 1. Define Qualification Criteria ---
# This function calculates a "fit score" based on how well the lead's current stack
# aligns with the Supabase platform (Postgres, integrated services, scalability).
def calculate_supabase_fit_score(lead):
    score = 0
    
    # 1. Supabase Core Alignment (Postgres)
    # The BDR knows a lead using Postgres is a high-value prospect.
    if lead.get('current_database') == 'PostgreSQL':
        score += 3
        
    # 2. Need for Integrated Services (Auth/Storage)
    # Supabase offers integrated Auth, making leads using a separate provider or custom solution a good fit.
    if lead.get('auth_method') in ['Auth0', 'Custom Node.js Auth']:
        score += 2

    # 3. Scalability Indicator (Supabase is built for growth)
    # Leads indicating higher scale need a robust, enterprise-grade solution.
    if lead.get('scale_indicator') == 'High':
        score += 2
    elif lead.get('scale_indicator') == 'Medium':
        score += 1
        
    # 4. Relational Preference
    # Supabase is relational (Postgres), making it an easier transition than document DBs.
    if lead.get('data_model_preference') == 'Relational':
        score += 1

    return score

# --- 2. Main Execution ---
def run_analysis():
    print("--- Supabase Lead Qualification Analyzer ---")
    
    try:
        # Load the simulated leads data
        with open('leads_data.json', 'r') as f:
            leads = json.load(f)
    except FileNotFoundError:
        print("Error: leads_data.json not found.")
        return

    scored_leads = []
    for lead in leads:
        lead['supabase_fit_score'] = calculate_supabase_fit_score(lead)
        scored_leads.append(lead)

    # Sort leads by score (highest fit first)
    scored_leads.sort(key=lambda x: x['supabase_fit_score'], reverse=True)

    print("\n✅ Analysis Complete. Sorted Leads (Highest Fit to Lowest):\n")
    
    # Print results in a readable format
    print(f"{'Company':<20} | {'Current DB':<12} | {'Auth Method':<22} | {'Fit Score':<10}")
    print("-" * 67)
    for lead in scored_leads:
        print(f"{lead['company_name']:<20} | {lead['current_database']:<12} | {lead['auth_method']:<22} | {lead['supabase_fit_score']:<10}")

    print("\n--- End of Report ---")
    print("Interpretation: Leads with the highest score should be prioritized for immediate technical discovery.")

if __name__ == '__main__':
    run_analysis()
