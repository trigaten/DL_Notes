Policy Gradient Derivation
============================

.. math::

    U(\theta) = \sum_{\tau} P(\tau ; \theta) * R(\tau)

Take gradient 

.. math::

    \Delta_{\theta} U(\theta) = \Delta_{\theta} \sum_{\tau} P(\tau ; \theta) * R(\tau)

Since summation is a linear operation, we can move the gradient inside the sum.

.. math::

    \Delta_{\theta} U(\theta) = \sum_{\tau} \Delta_{\theta} P(\tau ; \theta) * R(\tau)

It is difficult to see what to do next. On one hand, we could immediatly expand 
:math:`P(\tau ; \theta)`. However, a bit down the road this would lead to problems.
Instead, we will employ the grad-log trick. Lets first add in 2 terms which multiply to 1.
Their utility will soon be apparent.

.. math::

    \Delta_{\theta} U(\theta) = \sum_{\tau} \frac{P(\tau ; \theta)}{1} * \frac{1}{P(\tau ; \theta)} *
     \Delta_{\theta} P(\tau ; \theta) * R(\tau)


Now we will employ the log-derivitive trick (:math:`\Delta log(x) = \frac{1}{x} * \Delta x`)

.. math::

    \Delta_{\theta} U(\theta) = 
    \sum_{\tau} 
        P(\tau ; \theta) * 
        \Delta_{\theta} log(P(\tau ; \theta)) * 
        R(\tau)

Lets quickly condense the formula via the expectation operator

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
        \Delta_{\theta} log(P(\tau ; \theta)) * 
        R(\tau)
    \right]

Now lets expand :math:`P(\tau ; \theta)`. The probability of a trajectory can be defined as 
the probability of the first state * the probability of transitioning into the next state given 
the current state and selected action * the probability of the selected action under the current 
policy. We repeatedly multiply the last 3 steps until the end of the trajectory.

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
        \Delta_{\theta} log \left(
            P(s_0) * 
            \prod_{t=0}^{\tau} P \left( s_{t+1} | s_t, a_t \right) * \pi (a_t | s_t)
        \right) * 
        R(\tau)
    \right]

Now we employ the log-sum trick (:math:`log(a*b) = log(a) + log(b)`)

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
        \Delta_{\theta} 
            \left(
                log (P(s_0)) + 
                \sum_{t=0}^{\tau}
                    log \left( P \left( s_{t+1} | s_t, a_t \right)\right) + 
                    log \left( \pi (a_t | s_t) \right) 
            \right) * 
        R(\tau)
    \right]

Lets move the gradient inside the parenthesis.

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
            \left(
                \Delta_{\theta} log (P(s_0)) + 
                \Delta_{\theta} \sum_{t=0}^{\tau}
                    log \left( P \left( s_{t+1} | s_t, a_t \right)\right) + 
                    log \left( \pi (a_t | s_t) \right) 
            \right) * 
        R(\tau)
    \right]

Recognize that the first term does not depend on :math:`\theta`. Thus, its gradient is 0.

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
            \left(
                \Delta_{\theta} \sum_{t=0}^{\tau}
                    log \left( P \left( s_{t+1} | s_t, a_t \right)\right) + 
                    log \left( \pi (a_t | s_t) \right) 
            \right) * 
        R(\tau)
    \right]

Lets move the gradient into the sum.

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
            \left(
                 \sum_{t=0}^{\tau}
                    \Delta_{\theta} log \left( P \left( s_{t+1} | s_t, a_t \right)\right) + 
                    \Delta_{\theta} log \left( \pi (a_t | s_t) \right) 
            \right) * 
        R(\tau)
    \right]

We can see that the transition probability does not depend on :math:`\theta`. Thus, its gradient is 0.

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
            \left(
                 \sum_{t=0}^{\tau}
                    \Delta_{\theta} log \left( \pi (a_t | s_t) \right) 
            \right) * 
        R(\tau)
    \right]