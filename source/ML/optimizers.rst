Optimizers
==================

Good old SGD
------------------
Just have single step size for all weights 

LR scheduling
******************
Simple schedule is 

.. math:: 

    LR = \frac{1}{c+t}

Where c is a hyperparam

Momentum
------------------

Adjust weight by part of previous step's gradient plus this step's gradient

.. math::

    m_t = \alpha*m_{t-1} + \Delta w_t

    w_t = w_{t-1} - \mu * m_t


    \alpha \text{ is a momentum-weighting hyperparam, usually 0.9}

    \mu \text{ is the learning rate}

Adagrad 
------------------

* Shrinks learning rate over time to fine tune 
* Has a different learning rate for each param; in theory, different parameters are different distances away from their optimums
* A big change in gradient leads to smallers steps over time

.. math:: 

    \Delta w_t = \frac{\mu}{\sqrt{\sum_{\text{over all steps t}}{} g_t^2}} * g_t

    \mu \text{ is the learning rate}

Adam 
-----------
* Combine momentum with individual param updates 



Momentum:

.. math:: 

    m_t = B_1 * m_{t-1} + (1-B_1) * g_t

Exponentially weighted squares of grads:

.. math:: 

    V_t = B_2*V_{t-1} + (1-B_2)*g^2_t

    B_1, B_2 \text{ set close to 1}

Since B_1 and B_2 start close to 1, m_t and v_t are very close to 0.
Correct by:

.. math:: 

    m_t = \frac{m_t}{1-B_1^t}

    v_t = \frac{v_t}{1-B_2^t}

Final Update:

.. math:: 

    \Delta w_t = \frac{\mu}{\sqrt{v_t} + \epsilon} * m_t

Common hyperparam values:

.. math:: 

    B_1 = 0.9

    B_2 = 0.999

    \epsilon = 10^{-8}





Excercises
----------------------

* Derive all optimizers
* Why weight squares of grads exponentially in adam? - Sum could grow too large, permanently suppress LR
