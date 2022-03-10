Decision Trees
==================

Decision Tree from known features 
-----------------------------------

The idea of the decision tree is that you select a feature, split your 
data according to their label on this feature then recursively do that.

Ways to split 
---------------
* Select feature based on its independent classification accuracy (at this point in 
the tree, so conditioned on the data it is given)

* Select feature based on lowest entropy

* How many possible trees are there with n features

Pruning 
----------
Remove leaves and assign label as majority of parent. 

Prepruning
***********
Stop growing at some point (more popular)

Postpruning
**********************
Prune after tree made