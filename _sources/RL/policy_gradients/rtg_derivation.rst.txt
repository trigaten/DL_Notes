Reward to Go Derivation
============================

We want to show that 

.. math::

    \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            \sum_{t=0}^{T}
                \Delta_{\theta} log \pi (a_t | s_t) * R(\tau)
        \right]
    = 
    \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            \sum_{t=0}^{T}
                \Delta_{\theta} log \pi (a_t | s_t) * R(\tau[t:])
        \right]


Lets expand the left side

.. math::

     \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            \sum_{t=0}^{T}
                \Delta_{\theta} log \pi (a_t | s_t) * \left(
                    \sum_{t'=0}^{T}R(s_{t'}, a_{t'}, s_{t'+1})
                \right)
        \right]

Lets put the sums together

.. math::

     \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            \sum_{t=0}^{T}\sum_{t'=0}^{T}
                \Delta_{\theta} log \pi (a_t | s_t) * \left(
                    R(s_{t'}, a_{t'}, s_{t'+1})
                \right)
        \right]

Now take the summations outside of the expectation. This doesnt make sense at first since 
T is the length of the episode sampled in the expectation. However, we can set T to be the 
longest episode possible or even an infinitely long episode and we can consider all episodes which
end before length T to actually stay in an absorbing state for the rest of the steps until T.

.. math::

     \sum_{t=0}^{T}\sum_{t'=0}^{T} \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
                \Delta_{\theta} log \pi (a_t | s_t)
                    R(s_{t'}, a_{t'}, s_{t'+1})
        \right]

We want to show that rewards which occur before actions have no effect on the probabilities
of those actions. So, we want to show that when t' < t, the value inside of the expectation is 0.
Lets separate the summation into cases where t' < t and t' >= t.

.. math::

    \mathbb{E}_{\tau \sim \pi_{\theta}} 
     \left[ 
         t, t'
    \right]
    = \Delta_{\theta} log \pi (a_t | s_t)
                    R(s_{t'}, a_{t'}, s_{t'+1})



    \textcolor{red}{
    \sum_{t=0}^{T} 
        \sum_{t'=0}^{t-1} \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            t, t'
        \right]}
    +
    \sum_{t=0}^{T} 
        \sum_{t'=t-1}^{T} \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
                t, t'
        \right]

Lets expand the left double sum.



.. math::
    \sum_{t=0}^{T} 
        \sum_{t'=0}^{t-1} \mathbb{E}_{\tau \sim \pi_{\theta}} 
        \left[ 
            \Delta_{\theta} log \pi (a_t | s_t)
                    R(s_{t'}, a_{t'}, s_{t'+1})
        \right]

Since the rewards occur before the actions, the two functions inside the expectation 
represent independent events. Thus, we can separate them.

.. math::
    \sum_{t=0}^{T} 
        \sum_{t'=0}^{t-1} 
        \textcolor{red}{\mathbb{E}_{\tau \sim \pi_{\theta}} \left[ 
            \Delta_{\theta} log \pi (a_t | s_t)
        \right]}
        *
        \mathbb{E}_{\tau \sim \pi_{\theta}} \left[ 
            R(s_{t'}, a_{t'}, s_{t'+1})
        \right]

Now, we attempt to prove that the left term equals zero via the expected gradient log theorum.

.. math::

    \int_{a_t} \pi_{\theta}(s_t|a_t) = 1

    \text{Differentiate according to } \theta

    \Delta_{\theta} \int_{a_t} \pi_{\theta}(s_t|a_t) = 0

    \text{Swap order of } \theta \text{ and } \int 

    \int_{a_t} \Delta_{\theta} \pi_{\theta}(s_t|a_t) = 0

    \text{Apply log derivitive trick}

    \int_{a_t} P(a_t | s_t) * \Delta_{\theta} log\pi_{\theta}(s_t|a_t) = 0

    \text{Convert to expectation}

    \mathbb{E} \left[
        \Delta_{\theta} log\pi_{\theta}(s_t|a_t)
    \right] 
     = 0

Thus, the previous formula ...

doesnt quite work

Sources
----------------
https://ai.stackexchange.com/questions/9614/why-does-the-reward-to-go-trick-in-policy-gradient-methods-work
https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html#expected-grad-log-prob-lemma








