"""
---------------------------------------------------
SPRINT 2: GRITTY GOALS BY HB (STUB)
---------------------------------------------------
[ ] Functions created for each major task
[ ] main() delegates tasks properly
[ ] Placeholder logic included (pass)
---------------------------------------------------
"""

# Humza Bangash Gritty Goals Sprint Project

# -----------------------------
# FUNCTION DEFINITIONS
# -----------------------------

def get_user_data():
    """Collect user financial information."""
    # TODO: Replace with real input later
    
    return {
        "name": "Humza",
        "income": 4500,
        "fixed": 2000,
        "variable": 1000,
        "reduction": 20
    }


def calculate_expenses(fixed, variable):
    """Calculate total expenses."""
    # TODO: Add fixed and variable expenses together
    return fixed + variable


def calculate_savings(income, expenses, reduction_percent):
    """Calculate current and projected savings."""
    # TODO: Compute savings and projected yearly savings
    
    current_savings = income - expenses
    reduced_expenses = expenses * (reduction_percent / 100)
    new_savings = current_savings + reduced_expenses
    yearly_projection = new_savings * 12
    
    return new_savings, yearly_projection


def generate_report(name, income, expenses, savings, projected):
    """Create formatted report."""
    # TODO: Format financial data into a readable report
    
    report = f"""
-------------------------------------
GRITTY GOALS SAVINGS REPORT
-------------------------------------
User: {name}

Monthly Income: ${income}
Total Expenses: ${expenses}

New Monthly Savings: ${savings}
Projected Yearly Savings: ${projected}

Stay disciplined and keep building wealth.
-------------------------------------
"""
    return report


def save_to_file(data):
    """Save data to log/report files."""
    # TODO: Write data to a file
    
    with open("budget_report.txt", "w") as file:
        file.write(data)


# -----------------------------
# MAIN CONTROLLER
# -----------------------------

def main():
    """Program controller that delegates tasks."""

    # Step 1: Get user data
    user_data = get_user_data()

    # Safety check
    if user_data is None:
        print("Error: User data could not be retrieved.")
        return

    # Step 2: Calculate expenses
    total_expenses = calculate_expenses(
        user_data["fixed"], user_data["variable"]
    )

    # Step 3: Calculate savings
    savings, projected = calculate_savings(
        user_data["income"],
        total_expenses,
        user_data["reduction"]
    )

    # Step 4: Generate report
    report = generate_report(
        user_data["name"],
        user_data["income"],
        total_expenses,
        savings,
        projected
    )

    # Step 5: Save report
    save_to_file(report)

    print(report)


# -----------------------------
# PROGRAM START
# -----------------------------

if __name__ == "__main__":
    main()