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

Closed vs Open vocab 
-----------------------

* Vocab called closed if entire vocab known

Perplexity 
-----------------------

Intrinsic Performance measure used for language models 

"inverse probability of test set normalized by # of words"

"kind of like weighted branch factor of language"

Should only be used to compare models which use the same vocab 

Low Perplexity is good

Is 2 to the cross entropy

For a bigram model, can define as:

.. math::

    \text{PP(w)} = \sqrt[N]{\prod_{i=1}^{N}\frac{1}{p(w_i | w_{i-1})}}

Meta 
-------

* Distributional semantics 
    define word meanings by context in which they occur

* first order occurrences
    words similar to words that occur near by them 

* second order occurrence 
    similar words have similar neighbors


Excercises 
-------------
* derive perplexity cross entropy relationship