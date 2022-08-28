# coding=utf-8

from dataclasses import dataclass


@dataclass
class SOMSet_1:
	dim = (64,64)
	max_iter: int = 129
	map_radius = 2.
	neigh_pow: float = 1.1
	neigh_diminish_pow: float = 0.2
	init_learn_rate: float = 0.7
	learn_rate_mode: str = "const"


@dataclass
class SOMSet_2:
	dim = (512, 512)
	max_iter: int = 64
	map_radius = 8.
	neigh_pow: float = 2.
	neigh_diminish_pow: float = 0.6
	init_learn_rate: float = 0.8
	learn_rate_mode: str = "variable"
