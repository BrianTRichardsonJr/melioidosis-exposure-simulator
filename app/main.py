import json
from datetime import datetime, timezone

import streamlit as st

from engine.risk_rules import classify_exposure, explain_risk
from engine.workflow import get_notification_steps
from engine.followup import get_followup_schedule


def build_incident_summary(event: dict, risk_value: str, reasons: list[str], notify_steps: list[str], followup: list[str]) -> str:
    """Build a plain-text incident summary for educational/documentation purposes."""
    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = []
    lines.append("Melioidosis Exposure Awareness Simulator — Incident Summary")
    lines.append("=" * 62)
    lines.append(f"Generated: {ts}")
    lines.append("")
    lines.append("DISCLAIMER")
    lines.append("- Educational simulation only. Not clinical or laboratory guidance.")
    lines.append("- Do not use for real-world decision-making.")
    lines.append("- Follow institutional policy and contact occupational health / public health authorities.")
    lines.append("")
    lines.append("SCENARIO")
    lines.append(f"- Scenario ID: {event.get('scenario_id')}")
    lines.append(f"- Agent type: {event.get('agent_type')}")
    lines.append(f"- Context: {event.get('organism_context')}")
    lines.append(f"- Setting: {event.get('event_setting')}")
    lines.append(f"- Exposure route category: {event.get('exposure_route')}")
    lines.append(f"- PPE used: {event.get('ppe_used')}")
    lines.append(f"- Time since event (hours): {event.get('time_since_event_hours')}")
    lines.append(f"- Symptoms present: {event.get('symptoms_present')}")
    lines.append(f"- Notes: {event.get('notes')}")
    lines.append("")
    lines.append("RISK CATEGORY (EDUCATIONAL)")
    lines.append(f"- {risk_value}")
    lines.append("")
    lines.append("WHY THIS CATEGORY WAS ASSIGNED")
    for r in reasons:
        lines.append(f"- {r}")
    lines.append("")
    lines.append("WHO TO NOTIFY (SYSTEMS WORKFLOW)")
    for s in notify_steps:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("FOLLOW-UP CONSIDERATIONS (CONCEPTUAL)")
    for f in followup:
        lines.append(f"- {f}")
    lines.append("")
    lines.append("EMPLOYMENT DISCLAIMER")
    lines.append("This project was developed in a personal capacity and does not represent CDC or U.S. Government positions.")
    return "\n".join(lines)


st.set_page_config(page_title="Melioidosis Exposure Awareness Simulator", layout="centered")
st.title("Melioidosis Exposure Awareness Simulator")
st.warning("Educational simulation only. Not for clinical or laboratory use.")

# Load synthetic scenarios
with open("data/scenarios.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)

scenario = st.selectbox(
    "Select a synthetic scenario",
    scenarios,
    format_func=lambda x: f"{x['scenario_id']} — {x.get('event_setting', '')}"
)

risk = classify_exposure(scenario)
reasons = explain_risk(scenario)

st.subheader("Risk Category (Educational)")
st.write(risk.value)
for r in reasons:
    st.write("- ", r)

st.subheader("Who to Notify (Workflow)")
notify_steps = get_notification_steps(scenario, risk)
for step in notify_steps:
    st.write("• ", step)

st.subheader("Follow-up Considerations (Conceptual)")
followup = get_followup_schedule(scenario, risk)
for item in followup:
    st.write("• ", item)

st.divider()

# Export block
st.subheader("Export Incident Summary")
st.caption("Exports a plain-text summary for educational documentation (no patient data).")

summary_text = build_incident_summary(
    event=scenario,
    risk_value=risk.value,
    reasons=reasons,
    notify_steps=notify_steps,
    followup=followup
)

st.download_button(
    label="Download incident summary (.txt)",
    data=summary_text,
    file_name=f"{scenario.get('scenario_id','scenario')}_incident_summary.txt",
    mime="text/plain"
)

st.caption("Developed in a personal capacity. Does not represent CDC or U.S. Government positions.")
