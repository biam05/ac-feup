# AC-FEUP-G75
Data Mining Project *To Loan or not to Loan* 

Project Group - G75

Project Members:
- Hugo Guimarães - up201806490
- Beatriz Mendes - up201806551
- Henrique Pereira - up201806538

### Usage 

All the available code can be accessed in the `src/jupyters´

Requirements:
    - Python
    - Jupyter Notebook

Given the runnable code is done through *jupyter notebooks*, there is no need to install further dependencies, as the notebooks have been executed and delivered in a way that the desired output of each file can be seen.

The project contents are distributed like this:
- [docs](https://github.com/biam05/ac-feup/tree/Delivery/docs)
    - **Presentation_G75.pdf** - Presentation displayed in class at 15/12/2021
    - **report_G75.pdf** - Final Report *PowerPoint* as a pdf file for the 23/12/2021 delivery
- [src](https://github.com/biam05/ac-feup/tree/Delivery/src)
    - [banking_data](https://github.com/biam05/ac-feup/tree/Delivery/src/banking_data) - Inicial Provided CSVs
    - [csvs](https://github.com/biam05/ac-feup/tree/Delivery/src/csvs) - CSV files created by our group
        - [results](https://github.com/biam05/ac-feup/tree/Delivery/src/csvs/results) - csvs with te last generated predictions
            - **final.csv** - *StratifiedKFold* algorithm generated prediction
            - **testing_model.csv** - *train_test_split* algorithm generated prediction
        - **loan_united_test.csv** - final csv after data cleaning and merging containg the *test* data
        - **loan_united_train.csv** - final csv after data cleaning and merging containg the *train* data
    - [database](https://github.com/biam05/ac-feup/tree/Delivery/src/database) - folder with the database related files (used to replace csv files)
    - [jupyters](https://github.com/biam05/ac-feup/tree/Delivery/src/jupyters) - Code for the project
        - **algorithms.ipynb** - python notebook containg all the pipeline execution off all our clasification algorithms
        - **cleaning<span>.py** - python code for the data cleaning process
        - **clustering.ipynb** - python notebook for data clustering generation
        - **graphs.ipynb** - python notebook for the graph generation and data analysis
        - **goals<span>.md** - markdown file for the project goals
        - **merge.ipynb** - python notebook for data merging into a single sqlite3 final table, to which the algorithms can now be applied

### Final Submission

- Final report slides can be seen [here](https://github.com/biam05/ac-feup/blob/Delivery/docs/report_G75.pdf)

