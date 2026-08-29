import streamlit as st

# ============================================================
# GOSI RULES — V1
# Keep rules separate from calculation logic.
# Verify official GOSI rules before production use.
# ============================================================

GOSI_RULES = {
    "existing_system": {
        "saudi": {
            "pension_employee": 0.09,
            "pension_employer": 0.09,
            "saned_employee": 0.01,
            "saned_employer": 0.01,
            "occupational_hazards_employer": 0.02,
        },
        "non_saudi": {
            "occupational_hazards_employer": 0.02,
        },
    }
}


# ============================================================
# CALCULATION ENGINE
# ============================================================

def calculate_gosi(nationality, basic_salary, housing_allowance):

    contributory_wage = basic_salary + housing_allowance

    if nationality == "Saudi":

        rules = GOSI_RULES["existing_system"]["saudi"]

        employee_contribution = contributory_wage * (
            rules["pension_employee"]
            + rules["saned_employee"]
        )

        employer_contribution = contributory_wage * (
            rules["pension_employer"]
            + rules["saned_employer"]
            + rules["occupational_hazards_employer"]
        )

    else:

        rules = GOSI_RULES["existing_system"]["non_saudi"]

        employee_contribution = 0

        employer_contribution = contributory_wage * (
            rules["occupational_hazards_employer"]
        )

    return {
        "contributory_wage": contributory_wage,
        "employee_contribution": employee_contribution,
        "employer_contribution": employer_contribution,
        "total_gosi": employee_contribution + employer_contribution,
    }


# ============================================================
# USER INTERFACE
# ============================================================

st.set_page_config(
    page_title="GOSI Payroll Assistant",
    page_icon="🤖"
)

st.title("🤖 GOSI Payroll Assistant")
st.write("V1 — Rules-based payroll calculation prototype")

st.divider()

employee_name = st.text_input("Employee name")

nationality = st.selectbox(
    "Nationality",
    ["Saudi", "Non-Saudi"]
)

basic_salary = st.number_input(
    "Basic salary (SAR)",
    min_value=0.0,
    value=0.0
)

housing_allowance = st.number_input(
    "Housing allowance (SAR)",
    min_value=0.0,
    value=0.0
)
employment_date = st.date_input(
    "Employment date"
)
if employment_date >= __import__("datetime").date(2024, 7, 3):
    regime = "New Social Insurance Law assessment"
else:
    regime = "Existing-system assessment"
if st.button("Calculate GOSI"):

    result = calculate_gosi(
        nationality,
        basic_salary,
        housing_allowance
    )

    st.subheader("Calculation Result")

    st.write(f"**Employee:** {employee_name}")
    st.write(
        f"**Contributory wage:** "
        f"SAR {result['contributory_wage']:,.2f}"
    )

    st.write(
        f"**Employee contribution:** "
        f"SAR {result['employee_contribution']:,.2f}"
    )

    st.write(
        f"**Employer contribution:** "
        f"SAR {result['employer_contribution']:,.2f}"
    )

    st.write(
        f"**Total GOSI:** "
        f"SAR {result['total_gosi']:,.2f}"
    )

    st.warning(
        "Prototype only. Verify the applicable GOSI rules "
        "before using this for actual payroll."
    )
