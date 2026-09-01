# Target model v3.8

lambda_ind,day(t) = R(t)*a*exp(b*t)/365 + sum_i e_i(t)*r_i*product_{j in B_i}(1-w_ij(t)).
P_day(t)=1-exp(-lambda_ind,day(t)).
Micromort=1,000,000*P_day(t).

The current car component is one implemented block within this intended long-term individualised model.
