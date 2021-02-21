# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
recovered = dataiku.Dataset("3_time_series_covid19_recovered_global")
recovered_df = recovered.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

recovered_pivoted_df = recovered_df.melt(id_vars=["Country/Region", "Province/State", "Lat", "Long"], 
        var_name="Date", 
        value_name="Value")


# Write recipe outputs
recovered_pivoted = dataiku.Dataset("recovered_pivoted")
recovered_pivoted.write_with_schema(recovered_pivoted_df)
