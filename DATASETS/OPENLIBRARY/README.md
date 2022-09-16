# OFFLINE DATASET
```
    Open source Datadump prepared by 3rd party tutors. Added indirectly to the system though prepared scripts since these datasets  have to be downloaded first as compressed files.
    #DATADUMPS
        #OPENLIBRARY DATASET
            #DOWNLOAD DATA [LATEST]
            wget https://openlibrary.org/data/ol_dump_works_latest.txt.gz
            wget https://openlibrary.org/data/ol_dump_authors_latest.txt.gz
            wget https://openlibrary.org/data/ol_dump_editions_latest.txt.gz

            #CLEAN DATA
                LC_ALL=C sed -i 's/[\d128-\d255]//g' /PATH_TO/[works_or_authors_editions_dataset].txt 
                iconv -f utf-8 -t utf-8 -c /PATH_TO/[works_or_authors_editions_dataset].txt
                sed 's/\\u0000//g' /PATH_TO/[works_or_authors_editions_dataset].txt > clean_    [works_or_authors_editions_dataset].txt
            #CSV FILE GENERATION

```
