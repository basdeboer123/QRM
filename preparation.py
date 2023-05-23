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
participants_df = pd.read_csv('Data/metadata.tsv', sep='\t')
participants_df = participants_df.set_index('uid')
participants_df['screen_size'] = participants_df['screen_width'] * participants_df['screen_height']
participants_df = participants_df[['swipe_finger', 'screen_size']]

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

# Get simplified df of error data
error_df = error_data(participants[0])
del participants[0]
for participant in participants:
    error_df = error_df._append(error_data(participant))

# Get duration df
def duration_data(participant):
    # Get participant df
    df = participant_data(participant)

    # Calculate duration
    df = df.apply(lambda row: row[df['errors'].isin(['0\n'])])
    df['duration'] = df['duration'].astype('int64')
    df = df.groupby(['sentence', 'word']).agg({ 'duration': lambda x: x.max() - x.min()})
    df = df.reset_index()

    # Add participant uid
    df['uid'] = participant

    return df

# Get simplified df of duration data
duration_df = duration_data(participants[0])
del participants[0]
for participant in participants:
    duration_df = duration_df._append(duration_data(participant))

print(duration_df)
