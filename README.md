# QRM
Project Quantitative Research Methods - On finding an interaction effect between hand postures and screen size for time and error rate (for swipe typing)

An overview of the files in this github repository:
- Data:
    - Data: How We Swipe dataset from Leiva et al.(2021).
    - prepared_data.csv: data frame for two-way MANOVA with means for time and error and independent variables swipe_finger and screen_size with one participant per row
    - normalized_data.csv: test for normailizing data, after tip from Egon (However, this computation did not work out because it was not suitable for the Two way MANOVA)
    - test_for_removingoutliers_seperately: test for removing outleirs seperately per mixed independent variable combination (tip from Egon)
  
    - repeated_measures_including_outliers.csv: data frame for repeated measures of time and error of the first 20 words for every participant, all data (no outliers excluded yet)
    - repeated_measures_outliers_rm.csv: data frame for repeated measures of time and error for the first 20 words for every participant, with outliers removed.

- Code:
    - preparation.py: file for creating the intitial dataframe from the participants swipe log files (in DATA). This is the dataframa we initially wanted to use for our research (including  IVs:screen_size & swipe_finger, DVs: error & time)
    - exploration_of_data.ipynb: first exploration of the data (showing means, plots and possible significance test suitable for this data), this file is not used and just here to show you our process of exploring the data.
    - Outliers_normality_MANOVA.ipynb: Visualisations of outliers and removing outliers, and Shapiro Wilk test for normality. (also two-factor MANOVA and post hoc tests are included, however, these can not be used to to violation of the normality assumtion)
    - removing outliers per category.ipynb: file for removing the outliers for time and error rate based on all combinations of the independent variables (after tip from Egon)
    - dataframe_for_repeated_measures.ipynb: creating a dataframe ready for the two-way repeated measures MANOVA. including removing outliers (and a start on including Covariable age, but due to the limited time this is not further explored)
    - The two-factor repeated measures MANOVA is executed in SPPS since this was to complex to do in Python. 
      
