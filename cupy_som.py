import time
import numpy as np
from toolbox import PermuteBruteForce, print_headline
from toolbox.SomClassCupy import SomCupy
from toolbox.visualization import Canvas

s = 9
color_amt = 8
som = SomCupy(dim=(2 ** s, 2 ** s), max_iter=32 * 8,
              map_radius=1. * color_amt, neighb_pow=2.,
              init_learn_rate=2., learn_rate_mode='const')

canvas = Canvas(tex_size=som.dim, canvas_sca=0.75)
canvas.texture.interpolation = "nearest"

array_pool = [np.linspace(0., 1., color_amt).tolist()] * 3
permute = PermuteBruteForce(array_pool)

som.train(permute.permuted)
som.get_info()

prediction = None
iter_counter = 0
iter_permute = 0
while True:
	if canvas._closed:
		som.stop()
		break
	if som.iter_complete:

		if iter_permute < len(permute.permuted) and (iter_counter % 10 * 1 == 0):
			p = permute.permuted[iter_permute % len(permute.permuted)]
			prediction = som.predict(p)
			print(f'PREDICTING {iter_permute}: {p} -- LOCATION: {prediction[::-1]}')
			prediction = None
			iter_permute += 1

		if iter_permute == len(permute.permuted):
			print_headline("PREDICTION COMPLETED")
			iter_permute += 1
	# break
	else:
		time.sleep(1 / 60.)
	canvas.injection(som.get_weights)
	iter_counter += 1
# time.sleep(1/60.)
