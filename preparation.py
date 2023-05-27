import json
from pathlib import Path
import numpy as np
import pandas as pd

# Get list of all participants
directory = 'Data/swipelogs'
logfiles = Path(directory).glob('*.log')
participants = []
for file in logfiles:
    participants.append(Path(file).stem)

# Get simplified df of participants
def participant_basics(participant):
    # Read json data
    with open(f'Data/swipelogs/{participant}.json') as user_file:
        file_contents = user_file.read()
    data = json.loads(file_contents)

    # Calculate screen size
    size = data['screenWidth'] * data['screenHeight']

    return pd.DataFrame({'screen_size': size, 'swipe_finger': data['swipeFinger']}, index=[participant])    

# Get participant df
def participant_data(participant):
    # Read participant log file
    list = []
    file = open(f'Data/swipelogs/{participant}.log')
    line = file.readline()
    while line:
        try:
            list.append(line)
        except ValueError:
            print('Error in line :' + line )
        line = file.readline()
    df = pd.DataFrame([sub.split(" ") for sub in list])

    # Set new header
    df = df.rename(columns=df.iloc[0])
    df = df.drop(df.index[0])
    df = df.rename(columns={'is_err\n': 'errors', 'timestamp': 'duration'})

    # Select usable columns
    df = df[['sentence', 'event', 'duration', 'word', 'errors']]

    # Add participant uid
    df['uid'] = participant

    return df

# Get error df
def error_data(participant):
    # Get participant df
    df = participant_data(participant)

    # Calculate the amount of errors
    df['errors'] = np.where((df['event'] == 'touchend') & (df['errors'] == '1\n'), 1, 0)
    df['errors'] = df['errors'].astype('int32')

    # Calculate errors
    df = df.groupby(['sentence', 'word']).agg({ 'errors': np.sum })
    df = df.reset_index()

    # Calculate error percentage
    words_amount = len(df)
    total_errors = df['errors'].sum()
  
    return pd.DataFrame({'error_rate': [total_errors / words_amount]}, index=[participant])

# Get duration df
def duration_data(participant):
    # Get participant df
    df = participant_data(participant)

    # Calculate duration
    df = df.apply(lambda row: row[df['errors'].isin(['0\n'])])
    df['duration'] = df['duration'].astype('int64')
    df = df.groupby(['sentence', 'word']).agg({ 'duration': lambda x: x.max() - x.min()})
    df = df.reset_index()
    df['time_per_char'] = df['duration'] / df['word'].str.len()

    return pd.DataFrame({'avg_char_duration': df['time_per_char'].mean()}, index=[participant])

# Get simplified df of dataframes
participants_df = participant_basics(participants[0])
error_df = error_data(participants[0])
duration_df = duration_data(participants[0])
del participants[0]
for participant in participants:
    participants_df = participants_df._append(participant_basics(participant))
    error_df = error_df._append(error_data(participant))
    duration_df = duration_df._append(duration_data(participant))

# Combine data
data = error_df.join(duration_df).join(participants_df)
data.index.name = "uid"

# Remove missing values (missing swipe finger, multiple users that never typed a word right)
data = data.dropna(how='any')

# Export data
data.to_csv('prepared_data.csv', sep='\t', encoding='utf-8')
