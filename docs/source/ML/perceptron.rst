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


Practice
-----------
* Derive convergence proof
* Derive voted, average weighted formula