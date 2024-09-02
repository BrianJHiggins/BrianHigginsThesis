Instructions to run the pipeline:


This process is currently configured to run a demonstration that will scrape one live page from the website and 
produce a sentiment analysis output. If it is required to run all the research data then it will be necessary 
to change the page selection in the module 1.1 code to: 1 - 1000. 
However, this may not be practical in one run due to the large dataset resulting.

Modules 1.1 to 2.1
(1) First download file ‘S&P 500 Index Stocks List.csv' to the working directory. This file is required by module 1.1

(2) Run modules 1.1 – 1.4 in order

      The output will be file ‘ECC_FinBERT_Input.csv’
      
(3) Run module 2.1 this takes as its input ‘ECC_FinBERT_Input.csv’

       The output file is ‘ECC_FinBERT_sentiment_output.csv’

       
       
Modules 3.1 – 4.1 (these modules will run the processed research data, producing the research oiutput )
What is required:
(1) Download and unzip Folders ‘FinBERT output files combined Part1.zip’ and ’FinBERT output files combined Part2.zip’.

(2)  Download and unzip folder ‘Stock_Data_Files.zip’.

(3)  Download file ‘transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv’ Required for module 3.2

(4) Run modules 3.1, 3.2 and 4.1 in order.

The output is the results file 'updated_combined_file_with_compatible_date.csv' (module 3.2)
and the Pearson correlation files, scatter plots and heatmaps.(module 4.1)
    _____________________________________________________________________
