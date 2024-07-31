# SUMMARY
Open Education Resources Search Engine
# OER
```
 Improving Education Through Personalised Learning.
```
# DEVELOPMENT SETUP
*OER box consists of  containers*

   * `DATA STORAGE`
    `DATA  INDEXERS`
    `QUERY RESULT RANKER`
    
* See individual containers (optimised for cpu ) for a distributed system setup.
# GOAL
```
Give High quality Search Results thourgh Artifial Intelligence.
```

# OBJECTIVES
```
Acquire Data
Clean Data
Store Data
Data Syncing
Index Data
High quality search results based on user query
```
# PREREQUISITE

*  
    `Ubuntu 18.04 LTS`
    `PostgreSQL 14`
    `MongoDB >4.0`
    `Redis Server`
    `ElasticSearch =>7.0`
    `pgsync`
    `Storage => 500GB`
    `RAM => 32GB`
    `CORES => 16`


# APIS
```
 grep -Eo 'http://[^ >]+' ADVANCED_PAPERS_EN_DB.txt > ADVANCED_PAPERS_URL.txt    
 grep -Eo 'https://[^ >]+' ADVANCED_PAPERS_EN_DB.txt > ADVANCED_PAPERS_URL.tx
 cat ADVANCED_PAPERS_HTTPS.txt | awk -F/ '{print $3}' > DOMAIN_HTTPS.TXT
```
