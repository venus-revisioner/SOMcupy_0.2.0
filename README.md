# SOMcupy

CUDA implementation of SOM algorithm using cupy library.
- unsupervised learning


Create historical data from BTC daily prices, and calculate three components:
1. normalized daily candle
2. normalized volatility
3. normalized trading volume

And feed the values as rgb-matrix into the cuda-accelerated SOM, self-organizing map.

This associative unsupervised learning model is self-made from the scratch, from the
abstraction I found in the net. (It was 2013 I did my first one, and then proceeded using gpu
through a OpenGL-shader version of the code. It was a bit tricky! But fast. I mostly analyzed
Bach's Goldberg Variations, but also Ligeti, Scriabin and other modernist composers. MIDI data
is perfect for RGB-visualisation. But there's more to it. I also used it for mapping 18 parameter
granular synthesizer to 2D map. It enabled a smooth transition from the preset to the other without
it being just a plain old linear interpolation.)
