import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

Trends = TrendReq()


Trends.build_payload(kw_search=["Devops Engineering"])
data = Trends.interest_by_region()
print(data.)
