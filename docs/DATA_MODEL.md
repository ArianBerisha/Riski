# RiskAI Data Registry v7.1

The SQLite database is the source of truth. CSV and JSON are exported snapshots.

## Evidence decisions
- validated/calibrated: eligible for production after regression tests
- research: visible only with explicit research status
- blocked: no numeric result

## Core rule
A numerator and denominator must refer to the same population, period, geography, role and endpoint definition. Counts are not rates. Cross-mode EU candidate rates are not Germany-specific production parameters.
