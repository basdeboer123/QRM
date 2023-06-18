# QRM
Project Quantitative Research Methods

See here an overview of the files in this github repository:
- data:
    - prepared_data.csv: data frame for two-way MANOVA with means for time and error
    - normalized_data.csv: test for normailizing data (after tip from Egon, this intervention did not work out)
    - repeated_measures_including_outliers.csv: data frame for repeated measures of first 20 word, all data (no ouliers excluded yet)
    - repeated_measures_outliers_rm.csv: data frame for repeated measures of first 20 word, with outliers removed.

- Code:
    - preparation.py: file for creating the intitial datframe what we wanted to use for our research (including screen_size, swipe_finger, error and time)
    - exploration_of_data.ipynb: first exploration of the data (showing means, plots and possible significance test suitable for this data), this file is not used and just here to show you our process of exploring the data.
    - Outliers_normality_MANOVA.ipynb: Visualisations of outliers and removing outliers, and Shapiro Wilk test for normality. (also two-factor MANOVA and post hoc tests are included, however, these can not be used to to violation of the normality assumtion)
    - dataframe_for_repeated_measures.ipynb: creating a dataframe ready for the two-way repeated measures MANOVA. including removing outliers (and a start on including Covariable age, but due to the limited time this is not further explored)
    - The two factor repeated measures MANOVA is executed in SPPS since this was to complex to do in Python.
    
