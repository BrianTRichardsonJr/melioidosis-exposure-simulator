import json
import streamlit as st
from engine.risk_rules import classify_exposure, explain_risk
from engine.workflow import get_notification_steps
from engine.followup import get_followup_schedule

st.title("Melioidosis Exposure Awareness Simulator")
st.warning("Educational simulation only. Not for clinical or laboratory use.")

with open("data/scenarios.json") as f:
    scenarios = json.load(f)

scenario = st.selectbox(
    "Select a synthetic scenario",
    scenarios,
    format_func=lambda x: x["scenario_id"]
)

risk = classify_exposure(scenario)
reasons = explain_risk(scenario)

st.subheader("Risk Category")
st.write(risk.value)
for r in reasons:
    st.write("- ", r)

st.subheader("Who to Notify")
for step in get_notification_steps(scenario, risk):
    st.write("• ", step)

st.subheader("Follow-up Considerations")
for item in get_followup_schedule(scenario, risk):
    st.write("• ", item)

st.caption("Developed in a personal capacity. Does not represent CDC or U.S. Government positions.")
