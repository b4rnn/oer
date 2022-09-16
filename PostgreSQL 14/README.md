# DATABASE

*Storage , Read , Write and Index.*

* PostgreSQL 14 CONTAINER CONSISTS OF*

   *`POSTGRESQL DATABASE`

# SETUP
```
Install postgre >= 9.4 as elastic search  is mandatory.
Older postgre versions wont work well with syncqing data to elasticsearch >=7.1.
```
# Dependencies
```
sudo apt-cache search postgresql | grep postgresql
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt -y update
```
# INSTALL
```
sudo apt -y install postgresql-14
```
# CONDITIONS 
```
#[ENABLE] redis-server service
   sudo systemctl enable postgresql
#[RESTART] redis-server service
   sudo systemctl restart postgresql
#[STOP] redis-server service
   sudo systemctl stop postgresql
#[STATUS] redis-server service
   sudo systemctl status postgresql
```
# VERSION
```
redis-server --version
```
# CONFIG 
```
sudo nano /etc/postgresql/14/main/postgresql.conf
#WRITE ACCESS LOGS LEVEL
   [BEFORE] wal_level = ??
   [AFTER]  wal_level = logical
#REPLICATION SLOTS
   [BEFORE] # max_replication_slots = ??
   [AFTER]  max_replication_slots = 1
#WRITE ACCESS LOGS SIZE
   [BEFORE] max_slot_wal_keep_size = ??
   [AFTER]  max_slot_wal_keep_size = 100GB
#RESTART
   sudo systemctl restart postgresql 
#STATUS
   sudo systemctl status postgresql 
```
# PORTS 
```
postgre --5432
sudo ufw allow 5432/tcp
sudo ufw allow 5432/udp
```
# TEACHERS FUTURES
```
   CREATE TABLE TEACHERS_FUTURES_DB(
         id SERIAL PRIMARY KEY,
         Course VARCHAR  NULL,
         Author VARCHAR  NULL,
         Activity VARCHAR NULL,
         Week VARCHAR  NULL,
         Title VARCHAR  NULL,
         Description VARCHAR  NULL,
         Keywords VARCHAR  NULL,
         Document VARCHAR  NULL,
         Date_Created date NOT NULL default CURRENT_DATE
      );
         
   #alter table teachers_futures_db add column Date_Created date not null default CURRENT_DATE;

   postgres=# copy teachers_futures_db (Course,Author,Activity,Week,Title,Description,Keywords,Document) from '/home/dia/tf/ACTT Breakdown - Week 1.csv' DELIMITER ',' CSV HEADER;
   COPY 63
   postgres=# copy teachers_futures_db (Course,Author,Activity,Week,Title,Description,Keywords,Document) from '/home/dia/tf/ACTT Breakdown - Week 2.csv' DELIMITER ',' CSV HEADER;
   COPY 22
   postgres=# copy teachers_futures_db (Course,Author,Activity,Week,Title,Description,Keywords,Document) from '/home/dia/tf/ACTT Breakdown - Week 3.csv' DELIMITER ',' CSV HEADER;
   COPY 22
   postgres=# copy teachers_futures_db (Course,Author,Activity,Week,Title,Description,Keywords,Document) from '/home/dia/tf/ACTT Breakdown - Week 4.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE TEACHERS_FUTURES_VIDEO_DB(                                                                                                                                    
   id SERIAL PRIMARY KEY,
   Course VARCHAR  NULL,
   Author VARCHAR  NULL,
   Activity VARCHAR NULL,
   Week VARCHAR  NULL,
   Title VARCHAR  NULL,
   Description VARCHAR  NULL,
   Keywords VARCHAR  NULL,
   Document VARCHAR  NULL,
   Date_Created date NULL default CURRENT_DATE
);
copy teachers_futures_video_db (Course,Author,Activity,Week,Title,Description,Keywords,Document,Date_Created) from '/home/dia/tf/ACTT Text Breakdown - ACTT Video.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE TEACHERS_FUTURES_AUDIO_DB  (                                                                                                                                    
   id SERIAL PRIMARY KEY,
   Course VARCHAR  NULL,
   Author VARCHAR  NULL,
   Activity VARCHAR NULL,
   Week VARCHAR  NULL,
   Title VARCHAR  NULL,
   Description VARCHAR  NULL,
   Keywords VARCHAR  NULL,
   Document VARCHAR  NULL,
   Date_Created date NULL default CURRENT_DATE
);
copy teachers_futures_audio_db (Course,Author,Activity,Week,Title,Description,Keywords,Document,Date_Created) from '/home/dia/tf/ACTT Text Breakdown - ACTT Audio-2.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE TEACHERS_FUTURES_DB(                                                                                                                                    
   id SERIAL PRIMARY KEY,
   Course VARCHAR  NULL,
   Author VARCHAR  NULL,
   Activity VARCHAR NULL,
   Week VARCHAR  NULL,
   Title VARCHAR  NULL,
   Description VARCHAR  NULL,
   Keywords VARCHAR  NULL,
   Document VARCHAR  NULL,
   Date_Created date NULL default CURRENT_DATE
   );
copy teachers_futures_db (Course,Author,Activity,Week,Title,Description,Keywords,Document,Date_Created) from '/home/dia/tf/ACTT Text Breakdown - ACTT.csv' DELIMITER ',' CSV HEADER;
```
# OPENLIBRARY
```
   psql u -postgres

   psql postgres < /PATH_TO/openlibrary-db.sql
   ALTER TABLE editions DROP COLUMN work_key;

   COPY works FROM '/PATH_TO/[works_or_authors_editions_dataset].csv' DELIMITER E'\t' QUOTE '|' CSV;
   COPY authors FROM '/PATH_TO/[works_or_authors_editions_dataset].csv' DELIMITER E'\t' QUOTE '|' CSV;
   COPY editions FROM '/PATH_TO/[works_or_authors_editions_dataset].csv' DELIMITER E'\t' QUOTE '|' CSV;

   ALTER TABLE editions ADD COLUMN work_key;

   insert into editionisbn13s select distinct key,  jsonb_array_elements(data->'isbn_13')->>0  from editions where  key is not null and data->'isbn_13'->0 is not null;

   select e.data->>'title' "EditionTitle", e.data->'languages'->0->>'key' "Language",e.data->>'publish_date' "DateUpdated", e.data->>'subtitle' "EditionSubtitle" , e.data->>'subjects' "Subjects",a.data->'name' "author" from editions e join editionisbn13s ei on ei.edition_key = e.key join works w on w.key = e.work_key join authors a on a.key = w.data->'authors'->0->'author'->>'key'  where e.data->'languages'->0->>'key'='/languages/eng' OR e.data->'languages'->0->>'key' = '/l/eng' limit 3;

   copy (select e.data->>'title' "EditionTitle", e.data->'languages'->0->>'key' "Language",e.data->>'publish_date' "DateUpdated", e.data->>'subtitle' "EditionSubtitle" , e.data->>'subjects' "Subjects",a.data->'name' "author" from editions e join editionisbn13s ei on ei.edition_key = e.key join works w on w.key = e.work_key join authors a on a.key = w.data->'authors'->0->'author'->>'key'  where e.data->'languages'->0->>'key'='/languages/eng' OR e.data->'languages'->0->>'key' = '/l/eng' limit 3) to '/PATH_TO/open_library_export.csv' With CSV DELIMITER E'\t';

   CREATE TABLE BOOKS_ENG_DB(
         id SERIAL PRIMARY KEY,
         title VARCHAR  NULL,
         language VARCHAR  NULL,
         date_updated VARCHAR NULL,
         abstract VARCHAR  NULL,
         subject VARCHAR  NULL,
         authors VARCHAR  NULL
   );

INSERT INTO BOOKS_ENG_DB(title, language, date_updated, abstract, subject, authors, notes, description, book_key,covers)select e.data->>'title' , e.data->'languages'->0->>'key' ,e.data->>'publish_date', e.data->>'subtitle', e.data->>'subjects',a.data->'name',e.data->'notes'->>'value',e.data->'description'->>'value',w.key,w.data->'covers'->>0 from editions e join editionisbn10s ei on ei.edition_key = e.key join works w on w.key = e.work_key join authors a on a.key
= w.data->'authors'->0->'author'->>'key'  where e.data->'languages'->0->>'key'='/languages/eng' OR e.data->'languages'->0->>'key' = '/l/eng';
```
# X5GON
```
 [LOGIN TO MONGO VALIDATA IF DATA EXISTS FROM DB TEST AND COLLECTIONS X5GON]
mongo 192.168.8.212:27017 -u "AlbusDumbledore5" -p "SherbetPops22" --authenticationDatabase 'admin'
    show databases
    test.x5gon.count()
[LOGIN TO MONGO VALIDATA IF DATA EXISTS]
mongoexport --host 192.168.8.212:27017 -u "AlbusDumbledore5" -d test -c x5gon --forceTableScan  -p "SherbetPops22"  --authenticationDatabase 'admin' --type=csv --out x5gon.csv --fields 'record_data.title,record_data.description,record_data.type,record_data.url,record_data.website,record_data.language,record_data.creation_date,record_data.retrieved_date,record_data.provider.name,record_data.provider.id,record_data.provider.domain,record_data.content_ids.0,record_data.license.short_name ,record_data.license.disclaimer ,record_data.license.url'

[LOGIN TO POSTGRE DB]
psql u -postgres

CREATE TABLE X5GON(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    description VARCHAR  NULL,
    data_type VARCHAR NULL,
    url VARCHAR  NULL,
    website VARCHAR  NULL,
    language VARCHAR  NULL,
    creation_date VARCHAR  NULL,
    retrieved_date VARCHAR  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL
);
COPY x5gon(title,description,data_type,url,website,language,creation_date,retrieved_date,provider_name,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url)FROM '/home/dia/x5gon.csv' (FORMAT csv, HEADER, DELIMITER ',');

CREATE TABLE X5GON_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date DATE  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  X5GON_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url, data_type)select DISTINCT  title,language,description,url,website,provider_name,creation_date::timestamp::date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url, data_type from x5gon where language='en';

CREATE TABLE AUDIO_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date DATE  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  AUDIO_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name,creation_date::timestamp::date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='audio';

CREATE TABLE VIDEOS_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date DATE  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  VIDEOS_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name,creation_date::timestamp::date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='video';

CREATE TABLE TEXT_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date DATE  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  TEXT_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name,creation_date::timestamp::date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='text';

DATE FILTERS(2012)
CREATE TABLE VIDEOS_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date INTEGER  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  VIDEOS_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name, extract(year from creation_date),provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='video' AND  extract(year from creation_date) >=2012;

CREATE TABLE AUDIO_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date INTEGER  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  AUDIO_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name, extract(year from creation_date),provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='audio' AND  extract(year from creation_date) >=2012;

CREATE TABLE TEXT_EN_DB(
    id SERIAL PRIMARY KEY,
    title VARCHAR  NULL,
    language VARCHAR  NULL,
    description VARCHAR NULL,
    item VARCHAR  NULL,
    website VARCHAR  NULL,
    authors VARCHAR  NULL,
    creation_date INTEGER  NULL,
    retrieved_date DATE  NULL,
    provider_name VARCHAR  NULL,
    provider_id VARCHAR  NULL,
    provider_domain VARCHAR  NULL,
    content_ids VARCHAR  NULL,
    license_name VARCHAR  NULL,
    license_disclaimer VARCHAR  NULL,
    license_url VARCHAR  NULL,
    data_type VARCHAR  NULL
);
INSERT INTO  TEXT_EN_DB(title, language,description,item , website,authors,creation_date,provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type)select  title,language,description,item,website,provider_name, extract(year from creation_date),provider_id,provider_domain,content_ids,license_name,license_disclaimer,license_url,data_type from x5gon_en_db where data_type='text' AND  extract(year from creation_date) >=2012;
```
# SEMANTIC SCHOLAR
```
psql  -U postgres -h 127.0.0.1 --password scholar;
CREATE TABLE PAPERS_EN_DB(
   id SERIAL PRIMARY KEY,
   title VARCHAR  NULL,
   paperAbstract VARCHAR  NULL,
   authors VARCHAR NULL,
   year INTEGER  NULL,
   s2Url VARCHAR  NULL,
   pdfUrls VARCHAR  NULL,
   journalName VARCHAR  NULL,
   doiUrl VARCHAR  NULL,
   fieldsOfStudy VARCHAR  NULL
);
jq -c . *.json | spyql -Otable=papers_en_db "SELECT json->title, json->paperAbstract AS paperabstract, json->authors, json->year, json->s2Url AS s2url,json->pdfUrls AS pdfurls, json->journalName AS journalname, json->doiUrl AS doiurl,json->fieldsOfStudy AS fieldsofstudy FROM json TO sql" | psql  -U postgres -h 127.0.0.1 --password scholar

#[if you want to filter by year >=2012]
jq -c . *.json | spyql -Otable=papers_en_db "SELECT json->title, json->paperAbstract AS paperabstract, json->authors, json->year, json->s2Url AS s2url,json->pdfUrls AS pdfurls, json->journalName AS journalname, json->doiUrl AS doiurl,json->fieldsOfStudy AS fieldsofstudy FROM json  where json->year >=2012 TO sql " | psql  -U postgres -h 127.0.0.1 --password scholar

CREATE TABLE ADVANCED_PAPERS_EN_DB(
   id SERIAL PRIMARY KEY,
   title VARCHAR  NULL,
   paperAbstract VARCHAR  NULL,
   authors VARCHAR NULL,
   year INTEGER NULL,
   s2Url VARCHAR  NULL,
   pdfUrls VARCHAR  NULL,
   journalName VARCHAR  NULL,
   doiUrl VARCHAR  NULL,
   fieldsOfStudy VARCHAR  NULL
);
INSERT INTO ADVANCED_PAPERS_EN_DB (title, paperAbstract ,authors, year , s2Url ,pdfUrls,journalName,doiUrl ,fieldsOfStudy )select  title, paperAbstract ,authors, year , s2Url ,pdfUrls,journalName,doiUrl ,fieldsOfStudy  from PAPERS_EN_DB
where length(pdfUrls) >2;
```
# STATS
```
X5GON
   postgres=# SELECT  provider_domain , count(*) FROM X5GON_EN_DB WHERE  provider_domain is not null GROUP BY  provider_domain;
               provider_domain              | count 
   -------------------------------------------+-------
   http://campus.unibo.it                    |  3589
   http://madoc.univ-nantes.fr/              |    29
   https://av.tib.eu/                        |    33
   https://cnx.org                           |  7546
   https://media.upv.es                      |   164
   https://medienportal.siemens-stiftung.org |   652
   https://ocw.mit.edu/                      | 44963
   https://openlibrary.ecampusontario.ca/    |   197
   https://www.canal-u.tv                    |     5
   https://www.engageny.org/                 |  4595
   https://www.oerafrica.org/                |   317
   https://www.openlearnware.de/             |   135
   http://videolectures.net/                 | 23840
   (13 rows)

#[filter by year >=2012]
postgres=# SELECT  provider_domain , count(*) FROM X5GON_EN_DB WHERE  provider_domain is not null and extract(year from creation_date)>= 2012 GROUP BY  provider_domain;
              provider_domain              | count
-------------------------------------------+-------
 https://www.oerafrica.org/                |    47
 https://av.tib.eu/                        |    26
 http://videolectures.net/                 |  8610
 https://www.canal-u.tv                    |     5
 https://www.engageny.org/                 |  4595
 https://openlibrary.ecampusontario.ca/    |   197
 https://medienportal.siemens-stiftung.org |   652
 http://campus.unibo.it                    |  2342
 https://cnx.org                           |  6930
 https://www.openlearnware.de/             |   113
(10 rows)

[DB] 0:psql*                                                                                                             "smoke_dia_recorder" 12:06 15-Mar-22
   \COPY (SELECT  provider_domain , count(*) FROM X5GON_EN_DB WHERE  provider_domain is not null GROUP BY  provider_domain) TO '/home/dia/X5GON_EN_DB.csv' With CSV DELIMITER ',' HEADER;
#SEMANTIC SCHOLAR
   \COPY (SELECT   journalname , count(*) FROM advanced_papers_en_db WHERE  journalname is not null GROUP BY  journalname) TO '/home/dia/ADVANCED_PAPERS_EN_DB.csv' With CSV DELIMITER ',' HEADER;

```
