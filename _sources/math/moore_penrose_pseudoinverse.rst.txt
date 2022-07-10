Moore Penrose Pseudoinverse
====================================

A generalization of matrix inversion which creates :math:`A^+`

such that

.. math::

    A * A^+ * A = A

but not necessarily

.. math::

    A * A^+ = I_n 

It is calculated via SVD