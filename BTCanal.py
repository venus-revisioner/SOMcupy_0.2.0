# coding=utf-8
from dataclasses import dataclass
from random import random, shuffle
import numpy as np

from overhead.toolboxoh import import_file
from overhead.cryptooh import volatility, candle_normalize, coin_change
from som_param_data import *


@dataclass
class BTCanal:
	"""
	Use:
		btc = BTCanal()
		le = btc.lenght
		key = btc.keys
		ca_n = btc.candles_norm
		vola = btc.volat_norm
		volu = btc.vol_norm
	"""
	csv_path: str = "Binance_BTCUSDT_d.csv"
	bitcoin_data = import_file(csv_path).split("\n")
	keys = bitcoin_data[1].split(",")
	lenght = len(bitcoin_data[3:])
	bitcoin_dict = {}

	def __post_init__(self):
		self.bitcoin_dict = self.btc_dict

	@property
	def btc_dict(self):
		self.bitcoin_dict = {i: dict(zip(self.keys, self.bitcoin_data[i + 2].split(","))) for i in range(len(self.bitcoin_data) - 3)}
		return self.bitcoin_dict

	@property
	def candles_norm(self):
		return {i: candle_normalize(self.bitcoin_dict[i]['low'], self.bitcoin_dict[i]['high'], self.bitcoin_dict[i]['close']) for i in self.bitcoin_dict}

	@property
	def volat_norm(self):
		v = [volatility(self.bitcoin_dict[i]['high'], self.bitcoin_dict[i]['low']) / 100. for i in self.bitcoin_dict]
		return dict(zip(*(range(len(v)), v)))

	@property
	def vol_norm(self):
		max_vol = np.array([float(self.bitcoin_dict[i]["Volume BTC"]) for i in self.bitcoin_dict])
		max_vol /= np.max(max_vol)
		return dict(zip(*(range(len(max_vol)), max_vol)))
	
	@property
	def btc_training_pool(self):
		btc_data_list = [(self.candles_norm[i], self.volat_norm[i], self.vol_norm[i]) for i in range(self.lenght)]
		return tuple(btc_data_list)
	
	@property
	def btc_training_pool_suffle(self):
		btc_data_list = [(self.candles_norm[i], self.volat_norm[i], self.vol_norm[i]) for i in range(self.lenght)]
		shuffle(btc_data_list)
		return tuple(btc_data_list)
	
	def __repr__(self):
		return f"BTCanal(csv_path={self.csv_path})"
	
	def __str__(self):
		return f"BTCanal(csv_path={self.csv_path})"
	
	def __len__(self):
		return self.lenght
	
	def __getitem__(self, key):
		return self.bitcoin_dict[key]

	def __iter__(self):
		return iter(self.bitcoin_dict)
	
	def __contains__(self, item):
		return item in self.bitcoin_dict
	
	def __call__(self, *args, **kwargs):
		return self.bitcoin_dict

