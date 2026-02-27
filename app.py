import streamlit as st
import numpy as np
from scipy import stats

st.title("📊 One Sample T-Test Calculator")

st.write("Perform a one-sample t-test using SciPy")

# User input for sample data
data_input = st.text_area(
    "Enter sample data (comma separated)",
    "102, 98, 101, 105, 97, 99, 103"
)

# Population mean input
pop_mean = st.number_input("Enter Population Mean (H0)", value=108.0)

# Hypothesis selection
hypothesis = st.selectbox(
    "Select Alternative Hypothesis",
    ["two-sided", "less", "greater"]
)

if st.button("Run T-Test"):
    try:
        # Convert input string to list of floats
        data = [float(x.strip()) for x in data_input.split(",")]

        # Perform t-test
        t_stat, p_val = stats.ttest_1samp(
            data,
            pop_mean,
            alternative=hypothesis
        )

        st.subheader("Results")
        st.write(f"T-Statistic: {t_stat:.4f}")
        st.write(f"P-Value: {p_val:.4f}")

        if p_val < 0.05:
            st.success("Reject the Null Hypothesis (Significant)")
        else:
            st.warning("Fail to Reject the Null Hypothesis")

    except:
        st.error("Please enter valid numeric data.")