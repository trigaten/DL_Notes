Meta 
======

Evaluating similarity measures 
-----------------------------------

Extrinsic - plug into downstream system and see how well they perform 

Intrinsic - ask humans to evaluate

Inter annotator agreement
-----------------------------------

Basic probability
********************

.. math::

    \text{P(label)} = \frac{\text{agree}}{\text{agree + disagree}}

Cohen's Kappa 
********************

.. math::

    \frac{\text{P(a) - E[a]}}{1 - E[a]}

Where P(a) is according to the annotators and E[a] is the probability
of a having this label at random.

Baselines for word sense prediction
---------------------------------------------

* Just predict word as most frequent sense 
* Lesks Algorithm - check context and compare to different word sense definitions

