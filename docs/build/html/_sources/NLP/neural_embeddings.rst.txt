Neural Embeddings
=====================

More efficient than neural LM since no big softmax

Skip gram with negative sampling 
------------------------------------------

self supervised method trains a binary classifier.

Uses target, context pairs as positive examples and target, random word pairs as negative examples 

Separate vectors are trained for context and target words.

Similarity is computed by multiplying c * w 

Weighted unigram sampling
****************************
Smooth probabilities when selecting random words using:

.. math::

    p_a(w) = \frac{count(w)^a}{\sum_{w'}count(w')^a}


Fasttext
----------
Different neural embedding method that represents words as theirselves + subwords (as n-grams)

e.g. where -> [<wh, whe, her, ere, re>]

Excercises
------------
* Derive skipgram loss


