# Burkholderia pseudomallei Exposure Awareness & Reporting Simulator

Educational simulation tool to help healthcare teams recognize potential
B. pseudomallei laboratory exposure scenarios and understand institutional
reporting and follow-up workflows using ynthetic data and publicly
available guidance.

> ⚠️ Educational use only. 
> This tool is not clinical guidance, not laboratory guidance, and
> must notbe used for real-world medical or laboratory decision-making.

---

## Why this project exists

Rare pathogens such as Burkholderia pseudomallei can pose high-consequence
occupational risks when exposures are not promptly recognized or communicated.
My background in epidemiology and public health highlighted how delays in
recognition and fragmented reporting can lead to preventable harm.

This project explores how systems-level awareness, documentation, and
communication pathways support safer healthcare environments.

---

## What this tool does

- Simulates synthetic exposure scenarios (no real cases)
- Categorizes exposure events into educational risk levels
- Displays who to notify using a clear reporting workflow
- Provides a conceptual follow-up timeline for monitoring
- Emphasizes coordination between:
  - laboratory staff
  - clinicians
  - infection prevention
  - occupational health
  - public health authorities

---

## What this tool explicitly does NOT do

- ❌ Diagnose disease
- ❌ Identify organisms
- ❌ Provide laboratory handling instructions
- ❌ Recommend or prescribe treatment
- ❌ Replace institutional protocols
- ❌ Use real patient or laboratory data

---

## Data & ethics

All scenarios are fully synthetic and created for educational purposes.
No patient data, laboratory data, or protected health information (PHI) is used.

---

## Employment Disclaimer

This project was developed in a personal capacity. It does not represent the
views, policies, or positions of the Centers for Disease Control and Prevention
(CDC) or the U.S. Government. No CDC data, systems, or resources were used in the
development of this project. The author of this repository is a co-author on cited literature. This project
does not reproduce, reinterpret, or extend published guidance and was developed
independently for educational purposes.

---

## Sources (public guidance)

This simulator is informed by publicly available guidance including:

- CDC Emerging Infectious Diseases:  
  Management of Accidental Laboratory Exposure to Burkholderia pseudomallei*
  and B. mallei
- CDC Melioidosis Laboratory Guidance

Links are provided for reference only.

---

## Evidence Base

This simulator is informed by peer-reviewed literature describing occupational
laboratory exposures to *Burkholderia pseudomallei* in non-endemic settings.

In particular, exposure patterns, risk categorization concepts, and serological
monitoring timelines are based on:

Richardson BT Jr. et al. *Occupational Laboratory Exposures to Burkholderia
pseudomallei in the United States: A Review of Exposures and Serological Monitoring
Data, 2008–2024.* Pathogens (2025).

This tool does not reproduce laboratory methods, clinical management, or
post-exposure prophylaxis recommendations described in the literature.

---

## How to run locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
