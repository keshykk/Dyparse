drop table test1;
create table test1 (Nazwa varchar(35), Cena int(10));
LOAD DATA INFILE 'Glovo_kebab.csv' INTO TABLE test1 
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
Ignore 1 lines;