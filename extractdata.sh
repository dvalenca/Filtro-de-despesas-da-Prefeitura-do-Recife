#!/bin/bash

head -n 1 recife-dados-despesas-2013.csv >> all.out


allThreads=(";1012;" ";1563;" ";2023;" ";2143;" ";2510;" ";2541;")

for file in *.csv
 do
  grep ";2510;" $file >> all.csv
  grep ";2541;" $file >> all.csv
  grep ";1563;" $file >> all.csv
  grep ";1012;" $file >> all.csv
  grep ";;" $file >> all.csv
  grep ";2143;" $file >> all.csv
 done



#for file in *
#do
# cat $file | sed "1 d" | grep ";2510;" $file >> all.csv
# grep ";2541;" $file >> all.csv
# grep ";1563;" $file >> all.csv
# grep ";1012;" $file >> all.csv
# grep ";;" $file >> all.csv
# grep ";2143;" $file >> all.csv
#done

