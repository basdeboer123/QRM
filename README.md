# QRM
Project Quantitative Research Methods

See here an overview of the files in this github repository:
- data:
    - prepared_data.csv: data frame for two-way MANOVA with means for time and error
    - normalized_data.csv: test for normailizing data, after tip from Egon (However, this computation did not work out because it was not suitable for the Two way MANOVA)
    - repeated_measures_including_outliers.csv: data frame for repeated measures of time and error of the first 20 words of participants, all data (no ouliers excluded yet)
    - repeated_measures_outliers_rm.csv: data frame for repeated measures of time and error for the first 20 word for every participants, with outliers removed.
    - test_for_removingoutliers_seperately: test fro removing outleirs seperately per mixed independent variable combination (tip from Egon)

- Code:
    - preparation.py: file for creating the intitial dataframe from the participants swipe log files (in DATA). This is the dataframa we initially wanted to use for our research (including  IVs:screen_size & swipe_finger, DVs: error & time)
    - exploration_of_data.ipynb: first exploration of the data (showing means, plots and possible significance test suitable for this data), this file is not used and just here to show you our process of exploring the data.
    - Outliers_normality_MANOVA.ipynb: Visualisations of outliers and removing outliers, and Shapiro Wilk test for normality. (also two-factor MANOVA and post hoc tests are included, however, these can not be used to to violation of the normality assumtion)
    - test_removingoutliers_seperately.ipynb: notbook for removing outliers seperatly for every independent variable combination -> this resulted in a bit higher normality, hoever, still very far of from a a normal distribution
    - dataframe_for_repeated_measures.ipynb: creating a dataframe ready for the two-way repeated measures MANOVA. including removing outliers (and a start on including Covariable age, but due to the limited time this is not further explored)
    - The two-factor repeated measures MANOVA is executed in SPPS since this was to complex to do in Python. 
    - 
