# coding=utf-8

from ylitools.SomClassCupy import SomWorker
from som_param_data import *

som_worker = SomWorker()
som_worker.__dict__.update(SOMSet_1.__dict__)
som_worker.demo_rgb(color_amt=4)
