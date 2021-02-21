# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
2_time_series_covid19_confirmed_global = dataiku.Dataset("2_time_series_covid19_confirmed_global")
2_time_series_covid19_confirmed_global_df = 2_time_series_covid19_confirmed_global.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

confirmed_pivoted_df = 2_time_series_covid19_confirmed_global_df # For this sample code, simply copy input to output


# Write recipe outputs
confirmed_pivoted = dataiku.Dataset("confirmed_pivoted")
confirmed_pivoted.write_with_schema(confirmed_pivoted_df)
