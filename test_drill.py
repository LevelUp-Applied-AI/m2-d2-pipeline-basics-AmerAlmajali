"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():

    # TODO: Create a pd.Series with at least one NaN value
    # TODO: Call clean_column() on it
    # TODO: Assert no NaN values remain in the result
    # TODO: Assert the NaN was filled with the correct median value
    series = pd.Series([1, 3, 4, 5, None, None])
    cleaned = clean_column(series)
    assert cleaned.isna().sum() == 0
    assert cleaned.iloc[-1] == series.median()
    pass


def test_compute_revenue():
    # TODO: Create two small pd.Series (quantity and price)
    # TODO: Call compute_revenue() on them
    # TODO: Assert the result matches the expected element-wise product
    quantity = [1, 3, 5, 5, 6, 1]
    price = [10, 20, 30, 10, 30, 50]
    revenue = compute_revenue(quantity, price)
    expected = pd.Series([10, 60, 150, 50, 180, 50])
    assert revenue.equals(expected)
    pass
