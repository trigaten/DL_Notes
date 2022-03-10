Neural Nets
==================

Weight initialization 
----------------------------

Layer norm
---------------

Layerwise normalization...

After computing the layer output, W_t * h_t, get vector x_t

Compute the mean and variance of it then 

.. math::

    x_t = \frac{g}{\sigma} * (x_t - \mu) + b

Where g and b are 2 trainable vectors