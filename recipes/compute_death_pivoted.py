# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
time_series_covid19_deaths_global = dataiku.Dataset("time_series_covid19_deaths_global")
deaths_global_df = time_series_covid19_deaths_global.get_dataframe()


death_pivoted_df = deaths_global_df.melt(id_vars=["Country/Region", "Province/State", "Lat", "Lon"], 
        var_name="Date", 
        value_name="Value")


# Write recipe outputs
death_pivoted = dataiku.Dataset("death_pivoted")
death_pivoted.write_with_schema(death_pivoted_df)
