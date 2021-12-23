# AC-FEUP
Machine Learning at FEUP - 1st year of M.EIC

### Usage 

All the available code can be accessed in the `src/jupyters´

Requirements:
    - Python
    - Jupyter Notebook

Given the runnable code is done through *jupyter notebooks*, there is no need to install further dependencies, as the notebooks have been executed and deliverd in a way that the desired output of each file can be seen.

The folders are distributed like this:
    - docs
        - Presentation_G75.pdf - Presentation displayed in class at 15/12/2021
        - report_G75.pdf - Final Report *PowerPoint* as a pdf file for the 23/12/2021 delivery
    - src
        - banking_data - Inicial Provided CSVs
        - csvs - CSV files created by our group
            - results - csvs with te last generated predictions
                - final.csv - *StratifiedKFold* algorithm generated prediction
                - testing_model.csv - *train_test_split* algorithm generated prediction
            - loan_united_test.csv - final csv after data cleaning and merging containg the *test* data
            - loan_united_train.csv - final csv after data cleaning and merging containg the *train* data
        - database - folder with the database related files (used to replace csv files)
        - jupyters - Code for the project
            - **algorithms.ipynb** - python notebook containg all the pipeline execution off all our clasification algorithms
            - **cleaning.py** - python code for the data cleaning process
            - **clustering.ipynb** - python notebook for data clustering generation
            - **graphs.ipynb** - python notebook for the graph generation and data analysis
            - **goals.md** - markdown file for the project goals
            - **merge.ipynb** - python notebook for data merging into a single sqlite3 final table, to which the algorithms can now be applied

### Final Submission

- Final report slides can be seen [here](https://github.com/EdgarACarneiro/feup-ecac/blob/master/docs/ECAC%20Presentation%20-%20T1%20G10.pdf)

