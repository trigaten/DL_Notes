Reward to Go 
==================

We previously derived the following policy gradient:

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
        \sum_{t=0}^{\tau}
            \Delta_{\theta} log \left( \pi (a_t | s_t) \right) * 
            R(\tau)
    \right]

Inspecting it, we can see that the sum of rewards (:math:`R(\tau)`) is used to
scale all log probs. This doesnt really make sense to do since only rewards collected
after an action is executed should be used to scale it.

What we want is:

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
        \sum_{t=0}^{\tau}
            \Delta_{\theta} log \left( \pi (a_t | s_t) \right) * 
            R(\tau [t:])
    \right]

Can we justify this mathematically? Yes! It turns out that the previous two formulas are equivalent.