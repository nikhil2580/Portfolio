import numpy as np 
import pandas as pd 
from Quandl import Quandl

token = "sszA6k-rKBjSaaov7kHe"

dataset = Quandl.get("EOD / AAPL",authtoken=token)

print(dataset)