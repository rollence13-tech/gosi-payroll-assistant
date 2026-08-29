import streamlit as st

st.set_page_config(
    page_title="GOSI Payroll Assistant",
    page_icon="🤖"
)

st.title("🤖 GOSI Payroll Assistant")
st.write("V1 — Payroll calculation prototype")

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

if st.button("Calculate GOSI"):

    contributory_wage = basic_salary + housing_allowance

    if nationality == "Saudi":
        employee_contribution = contributory_wage * 0.0975
        employer_contribution = contributory_wage * 0.1175
    else:
        employee_contribution = 0
        employer_contribution = contributory_wage * 0.02

    st.subheader("Calculation Result")

    st.write(f"**Employee:** {employee_name}")
    st.write(f"**Contributory wage:** SAR {contributory_wage:,.2f}")
    st.write(
        f"**Employee contribution:** "
        f"SAR {employee_contribution:,.2f}"
    )
    st.write(
        f"**Employer contribution:** "
        f"SAR {employer_contribution:,.2f}"
    )

    st.info(
        "Prototype only. Verify the applicable GOSI rules "
        "before using this for actual payroll."
    )
