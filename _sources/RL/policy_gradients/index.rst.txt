Policy Gradients
==================

What
--------
Policy gradient algorithms are a class of deep reinforcement learning algorithms.

Why
--------
They are useful since they directly optimize the policy and can learn continuous actions.

Explanation
-------------

In RL we attempt to maximize discounted expected return. The utility of a policy 
(how well it performs) is defined by its expected discounted return.

.. math::
    
    U(\theta) =  \mathbb{E}_{\tau \sim \pi_{\theta}} \left[ 
        \sum_{t=0}^{\tau} \gamma^{t} * r_t
    \right]

It can also be written as:

.. math::
    U(\theta) = \sum_{\tau} P(\tau ; \theta) * R(\tau)


A common way of maximizing functions is by taking their gradient and stepping up the gradient. Since 
:math:`\theta` are the parameters that we are modifying, we take the gradient with respect to :math:`\theta`.

The gradient ends up being

.. math::

    \Delta_{\theta} U(\theta) = 
    \mathbb{E}_{\tau \sim \pi} \left[
            \sum_{t=0}^{\tau}
                \Delta_{\theta} log \left( \pi (a_t | s_t) \right) *
                R(\tau)
    \right]


.. toctree::
   
   pg_derivation
   reward_to_go
   rtg_derivation
   baselines/index