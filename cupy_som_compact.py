# coding=utf-8

from overhead.aioh.SomCudaDriver import SomWorker
from BTCanal import BTCanal
btc_training_pool = BTCanal().btc_training_pool
print("btc_training_pool lenght: ", len(btc_training_pool))

som_worker = SomWorker(dim=(512, 512), max_iter=64, internal_iters=2, map_radius_scale=0.01,
                       neighb_pow=2., neighb_diminish_rate=1.,
                       init_learn_rate=0.12, learn_rate_mode="const",
                       mex_hat_w=4., mex_hat_d=8., use_ricker=True, use_mex_hat=False, use_gauss=False,
                       gauss_mean=0., gauss_std=4.)

# todo: map btc data (maybe in 1 weeks at a time) and see what kinda slope its making or heading

som_worker.save_name = "btc_som_rand"
som_worker.save_weigths, som_worker.save_image, som_worker.save_BMU_dict = True, True, True
som_worker.start_training(btc_training_pool)
