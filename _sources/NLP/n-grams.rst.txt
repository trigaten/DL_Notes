N Grams 
=========

Corpus:

<s> I like peas </s>

<s> You like peas </s>


left: first word

top: second word 



.. list-table:: 
   :header-rows: 1
   :stub-columns: 1

   * - 
     - <s>
     - I 
     - like
     - peas
     - You
     - </s>
   * - <s>
     - 0
     - 1
     - 0
     - 0
     - 1
     - 0
   * - I
     - 0
     - 0
     - 1
     - 0
     - 0
     - 0
   * - like
     - 0
     - 0
     - 0
     - 2
     - 0
     - 0
   * - peas
     - 0
     - 0
     - 0
     - 0
     - 0
     - 2
   * - You
     - 0
     - 0
     - 1
     - 0
     - 0
     - 0

Probabilities (divide each element by sum of row)

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1

   * - 
     - <s>
     - I 
     - like
     - peas
     - You
     - </s>
   * - <s>
     - 0
     - 1/2
     - 0
     - 0
     - 1/2
     - 0
   * - I
     - 0
     - 0
     - 1
     - 0
     - 0
     - 0
   * - like
     - 0
     - 0
     - 0
     - 1
     - 0
     - 0
   * - peas
     - 0
     - 0
     - 0
     - 0
     - 0
     - 1
   * - You
     - 0
     - 0
     - 1
     - 0
     - 0
     - 0

Probability of I like peas = 

P(I | <s>) * P(like | I) * P(peas | like) * P(</s> | peas)

= 0.5 * 1 * 1 * 1 = 0.5

Generally express with logs, log(0.5)

Smoothing
------------
Having 0 probabilities for some n-grams is bad as they could make the test set occur with 0 probability

Lets smooth those probabilities!

Laplace Smoothing 
******************

Add 1 or k to every probability cell

Bigrams:

.. math::

    P_{add_k}(w_i | w_{i-1}) = \frac{Count(w_{n-1} w_n) + k}{Count(W_{n-1}) + V}

Recover adjusted counts
*********************************

We just modified the probability distribution. What does this say about the actual counts of each n gram?

Recover counts by multiplying by sum of row.

Backoff 
----------

If trigram doesn't exist, use bigrams, if they don't exist, unigrams, etc.

Stupid backoff 
****************

Just backs off and keeps multiplying by 0.4

