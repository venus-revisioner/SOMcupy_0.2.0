# coding=utf-8
import random
import numpy as np

from overhead.aioh.SomCudaDriver import SomWorker, SomCupy
from overhead.toolboxoh import import_file
from overhead.cryptooh import volatility, candle_normalize, coin_change
from som_param_data import *



som_worker = SomWorker(dim=(512, 512), max_iter=8, internal_iters=2, map_radius_scale=0.5,
                       neighb_pow=3., neighb_diminish_rate=1.,
                       init_learn_rate=0.4, learn_rate_mode="const",
                       mex_hat_w=12., mex_hat_d=2., use_ricker=False, use_mex_hat=False, use_gauss=True,
                       gauss_mean=0., gauss_std=2.)

# todo: map btc data (maybe in 1 weeks at a time) and see what kinda slope its making or heading

som_worker.save_path = "D:/PycharmProjects/SOMcupy"
som_worker.save_name = "btc_som_rand"
som_worker.save_weigths, som_worker.save_image, som_worker.save_BMU_dict = True, True, True
som_worker.start_training(btc_training_pool)


