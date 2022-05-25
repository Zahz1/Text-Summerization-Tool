# Text-Summerization-Tool
## Description: A tool to summerize text with multible different summerization tools

## Input for single file runs
The input text can be entered in the \TextSummarization_LinuxVersion\data.txt file. All the text summerization scripts get data from this text file
## Input for multible file runs
The input text can be entered in the ArticleTexts file in the following format
-> Create text file named the name of what text you are saveing is, ex "articalName.txt"

## Output
The output will always be stored in the \TextSummarization_LinuxVersion\Results folder 
### Output for single file runs
In the folder the results for each text summerization tool will be named as so, "textSummerizationToolName.txt". These results will be from what ever data was stored in the \TextSummarization_LinuxVersion\data.txt file.

### Output for multible file runs
In the folder the results for each text will be saved in a file with that text file's name. In this file each text summerization tool will be named as so, "textSummerizationToolName.txt". 

## How to Run
First install the requiremented libs with: "pip3 install -r requirements.txt" in the main Dir

### How to run single file
Execute the \TextSummarization_LinuxVersion\forOnlyDataALL.py

Note: It might be needed to execute the \TextSummarization_LinuxVersion\preProssessing.py file because ome charactors can mess up some text Summerization tools

### How to run multible files
Execute the \TextSummarization_LinuxVersion\RunALL.py

Note: This file also automatically execute the \TextSummarization_LinuxVersion\preProssessing.py file before it attemts to run any text summerization tools

# Rouge Testing
## Description: A tool to compare the results from the text summerization tools with the user generated ones

##Input
Results will be stored as so in the file RougeAndTrackRating\Articles
-> create file with name of areticle, ex "articalName"
-> create two files in the file named system_sum and reference_sum, ex "articalName"\system_sum and "articalName"\reference_sum
-> put all results from the text summerization tools in the system_sum as their txt files
-> then put 4 txt files in the reference_sum whith what ever summaries you would like to compare 

##Output
Results will be stored as so in the file RougeAndTrackRating\Results
Note: if it is needed to combine these results execute RougeAndTrackRating\combineResults.py and the results will be stored in MasterDataFile.csv
