Embeddings
==============

What
------

Embeddings are ways of representing words or documents of words as numbers (technically vectors of numbers).

Why
------

Basically, computers work with numbers, but not words 

How 
------

There are a bunch of ways 

Term Document Matrix
---------------------

We can use a term document matrix to create embeddings for documents OR words as follows:

Given a list of documents (Tweets) and counted occurences of words in them, 
we can simply represent each document by its corresponding column of words.

.. list-table:: Data
   :header-rows: 1
   :stub-columns: 1

   * - 
     - Tweet 1
     - Tweet 2
     - Tweet 3
     - Tweet 4
     - More Tweets...
   * - the
     - 2
     - 3
     - 7
     - 4
     - ...
   * - car
     - 0
     - 0
     - 2
     - 3
     - ...
   * - walk
     - 3
     - 1
     - 4
     - 5
     - ...
   * - More words...
     - ...
     - ...
     - ...
     - ...
     - ...

Thus, Tweet 1 would be represented as the vector [2, 0, 3, ...]
We could also represent a word by its corresponding row of documents, so
"the" could be represented as [2, 3, 7, 4, ...]

Problems:

* Common words like "the" will have very large counts and depending on the distance metrics,
  this could make ALL document embeddings look the same since "the" will contribute much more to 
  the metric than other words.

Word-Word Matrix
---------------------

Comment 1: "I love sweaters"

Comment 2: "I like sweaters"

Comment 3: "I like frogs"

.. list-table:: Data
   :header-rows: 1
   :stub-columns: 1

   * - 
     - I
     - love
     - sweaters
     - like
     - frogs
   * - I
     - 0
     - 1
     - 0
     - 2
     - 0
   * - love
     - 1
     - 0
     - 1
     - 0
     - 0
   * - sweaters
     - 0
     - 1
     - 0
     - 1
     - 0
   * - like
     - 2
     - 0
     - 1
     - 0
     - 1
   * - frogs
     - 0
     - 0
     - 0
     - 1
     - 0

Now, we can represent the word "love" as the vector [0, 1, 0, 2, 0]

Problems:

* Common words like "the" will have very large counts and depending on the distance metrics,
  this could make ALL document embeddings look the same since "the" will contribute much more to 
  the metric than other words.

TF-IDF
---------

TF-IDF works towards reducing how much very common words like "the" contribute to word embeddings. 
TD-IDF has two parts,

1. TF   

TF is the same as the vector we made with the term document matrix. 
It is just a count of the words occurences across documents.

2. IDF 

IDF is a scalar computed per word as 

.. math::

   log (\frac{ \text{# documents} }{\text{# documents in which word appears}})

It scores words which occur in few documents higher than words which occur in many documents.
This makes very common words less important.

TF-IDF then is just TF * IDF


Pointwise Mutual Information 
------------------------------

PMI is computed on word-word matrices and asks whether words are more or less likely 
to co-occur within a context window.

Its formula is:

.. math::

    PMI(X, Y) = log_2 (\frac{P(X, Y)}{P(X) * P(Y)})

Where X and Y are two words.

P(X, Y) is estimated as the number of times X and Y occur in the same context window 
divided by the sum of all counts in the table.

P(X) and P(Y) are each estimated as the number of times the word occurs 
divided by the table sum.

If PMI > 0, this indicates that if we have X or Y, the other word will be more 
likely to occur in the context window.

If PMI < 0, this theoretically indicates that if we know one word occurs, 
the other will be less likely to occur.

However:

Problems:

*

PPMI
---------

Just set < 0 values to 0


Excercises
-------------

* Derive TF-IDF from scratch.
* Compute the TF-IDF of a word in the first grid
* Derive PPMI from scratch 
* Compute the PPMI of a word in the second grid