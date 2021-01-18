## Software
I use linux system. so i will use libreoffice calc software which is free in cost.

## Dataset
For Analysis, i use the hospital charges data set.
The Hospital Charges dataset has more than 150,000 records of treatment of various ailments in several US hospitals.

Some stats about the dataset:
- The dataset has a record of 100 ailments
- It has a list of 3000+ healthcare providers (hospitals, medical centres, etc.)
- It has data from 50 states of the USA and approximately 2000 cities across the USA
- It describes the cost of treatment for approximately 7 million patients

### Features of hospital charges data set are:
1. Each record (or row) is a unique combination of state, city, ailment & provider. 
    1. DRG Definition : kind of treatment that they taken
    2. Provider Id,	Provider Name	, Provider Street, Address,	Provider City,	Provider State,	Provider Zip Code : info about services provider
    3. Hospital Referral Region Description: way of group hospital in certain region
    4. Total Discharges : total number of people treated in it
2. It also lists the average cost of treatment for a particular ailment.
    1. Average Covered Charges : averages charges
    2. Average Total Payments: paid by governments
    3. Average Medicare Payments: paid by privates insurances agencies.
    
# Phase 1: Searching for Useful Data  
##      a. slicing and dicing data
The sort and filter operations are meant to do these type of analyses. Sorting means to arrange the data (typically a column) in increasing, decreasing or alphabetical order. Filters, as the name suggests, enable you to filter out certain data, like all the hospitals in Alabama or all the hospitals treating chest pain. 
   
## Analyze
We are going to analyse this "raw" dataset and prepare a "report" having the list of providers treating a specific ailment in a particular state of USA. Subsequently, we will rank providers by the cost of treatment.

Such a "report" will be extremely useful to government agencies and patients across the state. Instead of analysing the entire dataset, they will now use this report to find the cheapest healthcare provider in their city. Think of this report like a sorted "Yellow Pages" or "Dictionary".
