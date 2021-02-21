# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
2_time_series_covid19_confirmed_global = dataiku.Dataset("2_time_series_covid19_confirmed_global")
2_time_series_covid19_confirmed_global_df = 2_time_series_covid19_confirmed_global.get_dataframe()


confirmed_pivoted_df = 2_time_series_covid19_confirmed_global_df.melt(id_vars=["Country/Region", "Province/State", "Lat", "Long"], 
        var_name="Date", 
        value_name="Value")


# Write recipe outputs
confirmed_pivoted = dataiku.Dataset("confirmed_pivoted")
confirmed_pivoted.write_with_schema(confirmed_pivoted_df)
