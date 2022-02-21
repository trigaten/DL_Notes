Basic Terms
==============

* normalization 
    * scale values into [0,1] 
* standardization 
    * mean 0 std 1
* inductive bias 
    * certain assumptions the model makes like "the decision boundary is linear"
* Entropy 
    measures expected amount of information (in bits) needed to represent an event. 
    For example, the result of flipping a fair coin can be encoded with a single bit (i.e. -log_2 (0.50)).
    We only expect to do this 50% of the time, so the entropy of this event would be -log_2 (0.50) * 0.50
    AKA the average amount of bits needed to encode the info.
* Information gain 
    Expected reduction in entropy caused by partitioning on an attribute, a, which could be "weather"

    High gain means high reduction in entropy 
    
    .. math::

        Gain (data, a) = \text{Entropy(data}) - \sum_{\text{v = for each value of a}}^{} \frac{\text{size of v}}{\text{size of data}} * \text{Entropy(v)}

* representation learning
    Learning allgos that automatically learn useful feature representations

* Accuracy 
    (tp + tn) / (tp + tn + fp + fn)

* precision 
    % of predicted positives that are actually positive 

* recall 
    % of actual positives predicted to be positive

* F-score 
    weighted harmonic mean of precision, recall 

    .. math::

        \frac{1}
        {(a)*\frac{1}{P} + (1-a)*\frac{1}{R}}

* F1-score 
    a = 0.5

* bias 
    Set of possible models with your configuration

Excercises
-------------
* Derive entropy, information gain, compute on sample data
* Derive F1 