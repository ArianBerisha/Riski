# Pkw model v3.4

## Numeric inputs
- Distance in km: exposure.
- Road type: injury-crash rate and fatality severity.
- Belt status: fatality-severity modifier for driver/front seat.
- Vehicle age: transferred fatality-severity association.
- ESC: crash and fatality-severity modifiers.

## Excluded from general calculation
Minutes, weather, time, AEB, lane assist, blind-spot systems and airbags are not used as universal multipliers because the available effects are not compatible all-crash, per-kilometre factors. This avoids false precision and double counting.

## Equations
P(injury crash)=1-exp(-km × road injury-crash rate × ESC crash factor).
P(death)=P(injury crash) × road fatality severity × belt factor × vehicle-age factor × ESC severity factor.
Micromorts=1,000,000 × P(death).
