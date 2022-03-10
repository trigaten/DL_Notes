Evaluating LMs
=================

BLEU 
-------
Compute precision of predicted sentence's 1-4grams compared to true translation(s)

.. math::

    BLEU = min(1, \frac{output length}{reference length})(\Pi_{i=1}^{4}precision_i)^{1/4}