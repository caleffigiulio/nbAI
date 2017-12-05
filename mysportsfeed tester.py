from ohmysportsfeedspy import MySportsFeeds

import pandas as pd

msf = MySportsFeeds(version="1.0")

msf.authenticate("GiulioDC", "V7C6D6KyM85x")

output = msf.msf_get_data(league='nba', season='2016-2017-regular', feed='player_gamelogs', format='csv',
                          player='stephen-curry')
dataframe = pd.DataFrame(output, columns = ['Game'])

dataframe


