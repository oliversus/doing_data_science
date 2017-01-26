from __future__ import division
import pandas as pd
import numpy as np

# get data for one day
data1 = pd.read_csv("dds_datasets/nyt1.csv")

# first look at data
data1.describe()
# minimum age is 0: babys are not using the internet, so this could be a missing value
data1[data1.Age==0].head(10)
# gender = 0 and Signed_In = 0 for all (?) of them
data1[data1.Age==0 and data1.Signed_In==1].head(10)
# no signed in user is 0 years old, so get rid of not signed in users
data1 = data1[data1.Signed_In!=0]

# create age_bins variable with categorized values
age_bins = [-float('inf'), 18, 24, 34, 44, 54, 64, float('inf')]
group_names = ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
data1['age_group'] = pd.cut(data1.Age, age_bins, labels=group_names)

# plot distributions of Impressions and Click-through-rate (clicks/impressions) for each age group
# impressions
data1.Impressions.hist(by=data1.age_group, bins=range(1,20), normed=True)
data1['click_rate'] = data1.Clicks / data1.Impressions
data1.click_rate.hist(by=data1.age_group, bins=np.linspace(0.01,1,20), range=[0.01, 1.])

# Define a new variable to segment or categorize users based on their click behavior
click_rate_bins = np.linspace(0, 1, 11)
group_names = ["<0.1", "0.1-0.2", "0.2-0.3", "0.3-0.4", "0.4-0.5", "0.5-0.6", "0.6-0.7", "0.7-0.8", "0.8-0.9", "0.9-1"]
data1['click_group'] = pd.cut(data1.click_rate, click_rate_bins, labels=group_names)
