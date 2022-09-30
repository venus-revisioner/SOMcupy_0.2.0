

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

		"""
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
		"""

@dataclass
def BTCdeploy
	self.csv_path = self:
	le = self.length
	key = self.keys
	ca_n = self.candles_norm
	vola = self.volat_norm
	volu = self.vol_norm
	
	@property
	def btc_training_pool(self):
	btc_data_list = [(ca_n[i], vola[i], volu[i]) for i in range(le)]
	btc_training_pool = tuple(btc_data_list)
	return btc_training_pool

	csv_path = "Binance_BTCUSDT_d.csv"
