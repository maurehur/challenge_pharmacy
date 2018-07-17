# Insight Data Engineering - Coding Challenge
1. [Solution Description](README.md#solution-description)
2. [Requirements and Dependencies](README.md#requirements)
3. [General Comments](README.md#general-comments)

# Solution Description

In this challenge was analized a dataset (using only I/O libraries, no external library were used) with information on prescription drugs prescribed by individual physicians and other health care providers. This repo contain a script provide a list of all drugs,the total number of UNIQUE individuals who have been prescribed a medication, and the total drug cost and it is sorted in descending order based on the total drug cost. This project presents the following structure:

    |── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
                    |── top_cost_drug.txt
    
The input folder must contain the dataset (provided by insight), after to run the script a list will be saved in the output folder with all drugs sorted in descending order based on the total drug cost.

# Requirements

The dataset was analyzed in python3.

Required packages:
* os
* re
* sys

# General Comments

You can run the script with the following command from within the pharmacy_counting folder:

```
pharmacy_counting~$ ./run.sh
```
the output file ('top_cost_drug.txt') will look like this:

```
drug_name,num_prescriber,total_cost
HARVONI,5219,5992222543
CRESTOR,147113,2704097429
LANTUS SOLOSTAR,106352,2237688500
ADVAIR DISKUS,126943,2038325949
SPIRIVA,114190,1966117068
JANUVIA,98897,1910493980
REVLIMID,5487,1887150891
NEXIUM,114026,1761213922
LANTUS,91055,1623149913
LYRICA,108953,1526906113
```
