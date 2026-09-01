# Probability and micromort model v3.5

- Cumulative hazard H may exceed 1.
- Death probability is P = 1 - exp(-H), always between 0 and 1.
- Micromorts are M = 1,000,000 × P, always between 0 and 1,000,000.
- 2,000 µMort = 0.2%, approximately 1:500.
- 1,000,000 µMort = 100%.
- The scale spans 0.01 to 1,000,000 µMort over eight logarithmic decades.
- Daily distance above 2,000 km triggers an extrapolation warning but remains calculable for model testing.
