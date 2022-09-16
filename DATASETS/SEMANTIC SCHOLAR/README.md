# OFFLINE DATASET
```
    Open source Datadump prepared by 3rd party tutors. Added indirectly to the system though prepared scripts since these datasets  have to be downloaded first as compressed files.
    #DATADUMPS
        #REQUIREMENTS
            pip3 install pv [or]
            sudo apt install pv
            pip3 install spyql
            sudo apt  install jq
            python3.7 [INSTALED EALIER]
            AWS CLI [https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html]
        #SEMANTIC SHOLAR DATASET
            #DOWNLOAD DATA [LATEST]
                aws s3 cp --no-sign-request --recursive s3://ai2-s2-research-public/open-corpus/2022-02-01/ destinationPath
            #SAMPLED DATA
                cp s2-corpus-{100-2789}.gz
                pv *gz > final
                mv final s2-corpus.gz
                gzip -d s2-corpus.gz
            #BIG DATA
                pv *gz > final
                mv final s2-corpus.gz
                gzip -d s2-corpus.gz
            #JSON CONTAINER GENERATION
                mv s2-corpus s2-corpus.json
```
