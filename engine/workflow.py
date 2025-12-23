def get_notification_steps(event: dict, risk_level):
    steps = [
        "Notify laboratory supervisor or safety officer",
        "Document exposure details (what, when, role, route)",
        "Report to occupational health or designated clinic",
        "Notify infection prevention per institutional policy",
        "Contact state or local public health department"
    ]

    if risk_level.value.startswith("High"):
        steps.insert(0, "Urgent medical evaluation recommended")

    if event.get("agent_type") == "mallei":
        steps.append(
            "Note: Validated human serology is not available for B. mallei; symptom monitoring emphasized"
        )

    return steps

