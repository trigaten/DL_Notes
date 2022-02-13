* TD-error
    * error_t = R_{t+1} + y*V(s_{t+1}) - V(s_t)
    * biased towards Value estimator

* n-step TD-error
    * error_t = r_t + y*r_{t+1} + y^2*r_{t+2} + ... + y^{n-1}*r_{n-1} + ? - V(s_t)

* GAE
    * Geometric average over all n, n-1, n-2...TD-errors

excercises

* derive 
* apply to example