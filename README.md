Results data in file 'updated_combined_file_with_compatible_date.csv'

Results correlation data: Q&A_tone_price_correlation.csv, Q&A_tone_price_correlation_by_GICS.csv 
and scatter plots,and correlation matrices in the 'plots' folder.


Instructions to run the pipeline:

Download the following modules: 1.1, 1.2, 1.3, 1.4, 2.1, 3.1, 3.2, 4.1 and GICS_corrleation  

Download and unzip the following folders: Stock_Data_Files, FinBERT output files Combined Part1 / and Part2

Download the following files: S&P 500 Index Stocks List.csv, transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv

modules 1.1 - 2.1 are currently configured to run a demonstration that will scrape two live pages from the website and 
produce a sentiment analysis output. 
If it is required to run all the research data then it will be necessary 
to change the page selection in module 1.1 code (line 33), from 'range(301, 303)' to 'range(1, 1000)' 
However, this may not be practical in one run due to the large dataset resulting.


Run:

modules 1.1 to 2.1

(1) First download file ‘S&P 500 Index Stocks List.csv' to the working directory. This file is required by module 1.1

(2) Run modules 1.1 – 1.4 in order

      The output will be file ‘ECC_FinBERT_Input.csv’
      
(3) Run module 2.1 this takes as its input ‘ECC_FinBERT_Input.csv’

       The output file is ‘ECC_FinBERT_sentiment_output.csv’
       

Run:       
modules 3.1 – 4.1 and GICS_correlation (these modules will run the sentiment processed research data, and will produce the research output )

(1) Download and unzip Folders ‘FinBERT output files combined Part1.zip’ and ’FinBERT output files combined Part2.zip’.

(2)  Download and unzip folder ‘Stock_Data_Files.zip’.

(3)  Download file ‘transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv’ Required for module 3.2

(4) Run modules 3.1, 3.2 , 4.1 and GICS_correlation in order. (ignore warnings in 3.2 and allow to complete ~ 2-3 minutes)


The output is the results file 'updated_combined_file_with_compatible_date.csv' (module 3.2)

and the Pearson correlation files, scatter plots and heatmaps.(module 4.1 and module GICS_correlation)

    _____________________________________________________________________
