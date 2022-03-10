Multiclass
=============

OVA - one versus all 
----------------------
If have k classes, train k classifiers, each of which predicts yes/no is the data 
point this class 

AVA - all versus all 
----------------------
If have k classes, train k choose 2 classifiers, each of which says is it more one class or
the other. Select class with most votes. Could also do binary tree.

Excercises
------------
* Derive OVA, AVA error bounds