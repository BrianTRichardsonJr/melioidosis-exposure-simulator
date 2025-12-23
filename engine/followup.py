"""
Follow-up checkpoints reflect common monitoring intervals described in the
literature. This module does not specify diagnostic tests, laboratory assays,
thresholds, or medical interventions.
"""

def get_followup_schedule(event: dict, risk_level):
    schedule = [
        "Baseline documentation and clinical evaluation",
        "Education on symptom monitoring",
        "Scheduled follow-up assessments per occupational health protocol"
    ]

    if risk_level.value.startswith("High"):
        schedule.append("Consider serial monitoring over subsequent weeks")

    schedule.append(
        "Immediate evaluation if febrile or compatible symptoms develop"
    )

    return schedule

