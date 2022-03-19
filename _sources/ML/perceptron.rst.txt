Perceptron
==================

Gradient-free linear model training

Each example is feature weights, label -1 or +1 

Model contains linear weights, bias 

If the model predicts correctly, nothing happens 

Else, add/sub feature vector from weights and add/sub 1 from bias depending on label

* The margin is the distance between the hyperplane and the closest point to it


Voted perceptron 
-----------------
Keep all weights over time, at prediction step, make all predict then take average vote

Problems
**************

Computationally intensive

Average weighted perceptron 
-----------------

Keep all weights over time, then average them, then do single prediction

Perceptron proof
------------------

Inspiration
**************
Every time we update the perceptron weights from :math:`w_k` to :math:`w_{k+1}`, 
we want make sure that :math:`w_{k+1}` and :math:`w_*` become more similar. We 
measure this in 2 ways:

1. Ensure :math:`w_{k+1} * w_*` grows at each iteration

2. Ensure that :math:`w_{k+1} * w_*` grows faster than :math:`||w_k||^2`

Demonstrating that :math:`w_{k+1} * w_*` grows at each iteration
************************************************************************

.. math:: 

    w_{k+1} = w_k + y*x

    \text{multiply both sides by } w_*

    w_* * w_{k+1} = w_* * (w_k + yx)

    w_* * w_{k+1} = w_* w_k + w_* * yx

    \text{Recall the definition of the margin: }

    \gamma = \sup_{(x, y)}()



Practice
-----------
* Derive convergence proof
* Derive voted, average weighted formula