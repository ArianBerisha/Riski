# Pkw accumulation v3.6.1

The previous calculation became stuck at 5,000 µMort because it multiplied the probability of at least one injury crash by 5 deaths per 1,000 injury crashes. The corrected calculation accumulates fatal-event hazard directly and converts it by P = 1 - exp(-H). Consequently, the result can rise beyond 5,000 and approaches 1,000,000 µMort as exposure becomes extremely large.
