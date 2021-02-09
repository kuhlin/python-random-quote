# Import pandas
import pandas as pd

# Define file containing dataset
runkeeper_file = 'datasets/cardioActivities.csv'

# Create DataFrame with parse_dates and index_col parameters 
mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")
df_activities = pd.DataFrame(pd.pd.read_csv(runkeeper_file, parse_dates = ["Date"], index_col = mydateparser)

# First look at exported data: select sample of 3 random rows 
display(df_activities.sample(n = 3))

# Print DataFrame summary
print(df_activities.info())