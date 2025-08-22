import streamlit as st

def run_dashboard(score, explanations, events):
    st.title("Explainable Credit Scorecard")

    st.write("### Model Accuracy")
    st.write(score)

    st.write("### Explanations")
    for exp in explanations:
        st.write(f"Instance {exp['instance']} → Prediction: {exp['prediction']}")
        st.write("Feature contributions:", exp["contributions"])

    st.write("### Event Based Signals")
    for e in events:
        if "debt restructuring" in e.lower():
            st.error(f"Event detected: {e} → Risk increases")
        elif "strong" in e.lower():
            st.success(f"Event detected: {e} → Risk improves")
        elif "declining demand" in e.lower():
            st.warning(f"Event detected: {e} → Risk increases")
