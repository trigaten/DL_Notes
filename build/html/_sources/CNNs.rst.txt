
=============================================================
CNNs
=============================================================
------
Vocab
------

* spatial invariance - kernel applied at all locations
* translation invariance - kernel responds the same to the same patch regardless of location
* locality principle - early kernels only pay attention to very local areas
* cross correlation - operation of applying the kernel multiplication to each part of image
* convolution - cross correlation + added bias
* feature map - convolutional layer output
* receptive field - for some output element, its receptive field is all previous elements 
  which have had an effect on its calculation. This is of interest since if an element's receptive field 
  is too small, it may not be able to say much about the image.

----------
Questions
----------

* What happens to the kernel when there are multiple input channels?

  * The kernel becomes 3d and works the same!

* What information is lost with convolutional layers?

  * perimeter information!

* Whats a solution for this?

  * padding!

* Why pool?

  * mitigate convolution sensitivity? and spatially downsample 

* How does pooling work with multiple input channels?

  * pools them each separately without adding across channels