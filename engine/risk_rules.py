"""
Risk categories are conceptual and derived from published summaries of
laboratory exposure events. This module does not describe laboratory
procedures or biosafety practices.
"""


from enum import Enum

class RiskLevel(Enum):
    LOW = "Low Concern"
    ELEVATED = "Potential Exposure – Review Needed"
    HIGH = "High Concern – Escalation Required"


def classify_exposure(event: dict) -> RiskLevel:
    if event.get("symptoms_present"):
        return RiskLevel.HIGH

    route = event.get("exposure_route")
    ppe = event.get("ppe_used")

    if route in ["percutaneous", "aerosol_concern"]:
        return RiskLevel.HIGH

    if ppe in ["no", "unknown"]:
        return RiskLevel.ELEVATED

    return RiskLevel.LOW


def explain_risk(event: dict):
    reasons = []
    if event.get("symptoms_present"):
        reasons.append("Symptoms reported following potential exposure.")
    if event.get("exposure_route") in ["percutaneous", "aerosol_concern"]:
        reasons.append("Exposure route associated with higher concern.")
    if event.get("ppe_used") in ["no", "unknown"]:
        reasons.append("PPE use was absent or unknown.")
    if not reasons:
        reasons.append("No high-risk features identified in this scenario.")
    return reasons

