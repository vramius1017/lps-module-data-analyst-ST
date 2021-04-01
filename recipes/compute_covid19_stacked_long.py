# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
covid19_stacked = dataiku.Dataset("covid19_stacked")
covid19_stacked_df = covid19_stacked.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

covid19_stacked_long_df = covid19_stacked_df.melt(id_vars=["Country/Region", "Province/State", "Lat", "Long", "type"], 
        var_name="Date", 
        value_name="Value")


# Write recipe outputs
covid19_stacked_long = dataiku.Dataset("covid19_stacked_long")
covid19_stacked_long.write_with_schema(covid19_stacked_long_df)




