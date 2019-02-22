~~~
$ pw
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ⇥pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ⇥⇥tree
~~~
{: .bash}

~~~

├── CERDI
│   └── CERDI-seadistance.dta
├── IMF
│   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
├── README.md
├── UN
│   └── country-codes.csv
├── download.sh
└── screenlog.0

3 directories, 7 files
~~~
{: .output}

~~~
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ mv ~/Documents/hundred_random_values.do .
$ ls
~~~
{: .bash}

~~~

IMF				download.sh
README.md			hundred_random_values.do
~~~
{: .output}

~~~
$ which stata
$ which stata-mp
$ stata
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ locate stata
~~~
{: .bash}

~~~

/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/lexers/__pycache__/_stata_builtins.cpython-37.pyc
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/lexers/__pycache__/stata.cpython-37.pyc
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/lexers/_stata_builtins.py
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/lexers/stata.py
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/styles/__pycache__/stata.cpython-37.pyc
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/styles/stata.py
/usr/share/vim/vim80/syntax/stata.vim
~~~
{: .output}

~~~
$ /Applications/Stata/StataMP.app/Contents/MacOS/stata-mp
~~~
{: .bash}

~~~

  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Unicode is supported; see help unicode_advice.
      2.  More than 2 billion observations are allowed; see help obs_advice.
      3.  Maximum number of variables is set to 5000; see help set_maxvar.

. exit
~~~
{: .output}

~~~
$ PATH = /Applications/Stata/StataMP.app/Contents/MacOS/:$PATH
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ export 
~~~
{: .bash}

~~~

bash: export: `/Applications/Stata/StataMP.app/Contents/MacOS/:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin': not a valid identifier
bas/Applications/Stata/StataMP.app/Contents/MacOS/:$PATH
/Applications/Stata/StataMP.app/Contents/MacOS/:$PATH

bash: export: `/Applications/Stata/StataMP.app/Contents/MacOS/:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin': not a valid identifier
~~~
{: .output}

~~~
$ export PATH /Applications/Stata/StataMP.app/Contents/MacOS/:$PATH
~~~
{: .bash}

~~~
$PATH
/Applications/Stata/StataMP.app/Contents/MacOS/:$PATH
=/Applications/Stata/StataMP.app/Contents/MacOS/:$PATH

~~~
{: .output}

~~~
$ echo $PATH
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ stata-mp
~~~
{: .bash}

~~~

  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Unicode is supported; see help unicode_advice.
      2.  More than 2 billion observations are allowed; see help obs_advice.
      3.  Maximum number of variables is set to 5000; see help set_maxvar.

. exit
~~~
{: .output}

~~~
$ StataMP
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ls *.do
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ stata-mp -b do hundred_random_values.do 
$ # for windows
$ StataMP-64 /b do hun⇥dred_random_values.do
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ls
~~~
{: .bash}

~~~

IMF				download.sh			screenlog.0
README.md			hundred_random_values.do
~~~
{: .output}

~~~
$ ls -al
~~~
{: .bash}

~~~

drwxr-xr-x@ 11 koren  staff   352 Feb 22 13:05 .
drwxr-xr-x@ 10 koren  staff   320 Feb 22 12:19 ..
drwxr-xr-x@ 12 koren  staff   384 Feb 22 12:19 .git
drwxr-xr-x@  3 koren  staff    96 Feb 22 12:19 CERDI
drwxr-xr-x@  4 koren  staff   128 Feb 22 12:19 IMF
-rw-r--r--@  1 koren  staff   522 Feb 22 12:19 README.md
drwxr-xr-x@  3 koren  staff    96 Feb 22 12:19 UN
-rw-r--r--@  1 koren  staff   208 Feb 22 12:19 download.sh
-rw-r--r--@  1 koren  staff    81 Feb 22 12:33 hundred_random_values.do
-rw-r--r--@  1 koren  staff  1145 Feb 22 13:05 hundred_random_values.log
-rw-r--r--@  1 koren  staff  6302 Feb 22 13:09 screenlog.0
~~~
{: .output}

~~~
$ stata-mp do hu⇥ndred_random_values.
~~~
{: .bash}

~~~

  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Unicode is supported; see help unicode_advice.
      2.  More than 2 billion observations are allowed; see help obs_advice.
      3.  Maximum number of variables is set to 5000; see help set_maxvar.

. do hundred_random_values. 
file hundred_random_values not found
r(601);


. exit
~~~
{: .output}

~~~
$ stata-mp do hundred_random_values.do
~~~
{: .bash}

~~~

  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Unicode is supported; see help unicode_advice.
      2.  More than 2 billion observations are allowed; see help obs_advice.
      3.  Maximum number of variables is set to 5000; see help set_maxvar.

. do hundred_random_values.do 

. set obs 100
number of observations (_N) was 0, now 100

. generate x = uniform()

. generate y = uniform()

. replace y = 0.99 in 10
(1 real change made)

. 
end of do-file


. exit
no; data in memory would be lost
r(4);

. exit, clear
~~~
{: .output}

~~~
$ stata-mp do hundred_random_values.
~~~
{: .bash}

~~~

# for windows
stata-mp -b do hundred_random_values.do 
# for windows
StataMP-64 /b do hundred_random_values.do
⇥⇥⇥⇥⇥⇥⇥⇥⇥⇥⇥cat hun⇥dred_random_values.log 

  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Stata is running in batch mode.
      2.  Unicode is supported; see help unicode_advice.
      3.  More than 2 billion observations are allowed; see help obs_advice.
      4.  Maximum number of variables is set to 5000; see help set_maxvar.

. do hundred_random_values.do 

. set obs 100
number of observations (_N) was 0, now 100

. generate x = uniform()

. generate y = uniform()

. replace y = 0.99 in 10
(1 real change made)

. 
end of do-file
~~~
{: .output}

~~~
$ ls h-al 
~~~
{: .bash}

~~~

-rw-r--r--@ 1 koren  staff  1145 Feb 22 13:05 hundred_random_values.log
~~~
{: .output}

~~~
$ ⇥⇥less hun⇥dred_random_values.log 
~~~
{: .bash}

~~~


  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Stata is running in batch mode.
      2.  Unicode is supported; see help unicode_advice.
      3.  More than 2 billion observations are allowed; see help obs_advice.
      4.  Maximum number of variables is set to 5000; see help set_maxvar.

. do hundred_random_values.do 

. set obs 100
number of observations (_N) was 0, now 100

. generate x = uniform()

. generate y = uniform()

. replace y = 0.99 in 10
(1 real change made)

. 
end of do-file
hundred_random_values.log (END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOB
⇥
(END)
 ESCOA
⇥
(END)
 ESCOA
⇥
(END)
 ESCOA
⇥
(END)
 ESCOA
⇥
(END)
 ESCOA
⇥
(END)
 ESCOA
⇥
(END)
49lbash-3.2$ less hundred_random_values.log cat⇥⇥ ⇥
.git/                      README.md                  hundred_random_values.do
CERDI/                     UN/                        hundred_random_values.log
IMF/                       download.sh                screenlog.0
~~~
{: .output}

~~~
$ less hundred_random_values.log cat h⇥undred_random_values.log 
~~~
{: .bash}

~~~


  ___  ____  ____  ____  ____ (R)
 /__    /   ____/   /   ____/
___/   /   /___/   /   /___/   15.1   Copyright 1985-2017 StataCorp LLC
  Statistics/Data Analysis            StataCorp
                                      4905 Lakeway Drive
     MP - Parallel Edition            College Station, Texas 77845 USA
                                      800-STATA-PC        http://www.stata.com
                                      979-696-4600        stata@stata.com
                                      979-696-4601 (fax)

Single-user 2-core Stata perpetual license:
       Serial number:  501506203290
         Licensed to:  Miklos Koren
                       CEU MicroData


Notes:
      1.  Stata is running in batch mode.
      2.  Unicode is supported; see help unicode_advice.
      3.  More than 2 billion observations are allowed; see help obs_advice.
      4.  Maximum number of variables is set to 5000; see help set_maxvar.

. do hundred_random_values.do 

. set obs 100
number of observations (_N) was 0, now 100

. generate x = uniform()

. generate y = uniform()

. replace y = 0.99 in 10
(1 real change made)

. 
end of do-file
hundred_random_values.log (file 1 of 2) (END) - Next: cat
49lbash-3.2$ pwd
/Users/koren/Dropbox/teaching/courses/2019/research-seminar/scientific-computing-bootcamp/open-trade-data
~~~
{: .output}

~~~
$ cd 
$ cd Documents/
$ mkdir stata-batch
$ cd st⇥ata-batch/
$ clear
$ tree
~~~
{: .bash}

~~~


0 directories, 0 files
~~~
{: .output}

~~~
$ git clone git@github.com:korenmiklos/open-trade-data.git
~~~
{: .bash}

~~~

remote: Enumerating objects: 11, done.
remote: Counting objects:   9% (1/11)   
remote: Counting objects:  18% (2/11)   
remote: Counting objects:  27% (3/11)   
remote: Counting objects:  36% (4/11)   
remote: Counting objects:  45% (5/11)   
remote: Counting objects:  54% (6/11)   
remote: Counting objects:  63% (7/11)   
remote: Counting objects:  72% (8/11)   
remote: Counting objects:  81% (9/11)   
remote: Counting objects:  90% (10/11)   
remote: Counting objects: 100% (11/11)   
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects:  11% (1/9)   
remote: Compressing objects:  22% (2/9)   
remote: Compressing objects:  33% (3/9)   
remote: Compressing objects:  44% (4/9)   
remote: Compressing objects:  55% (5/9)   
remote: Compressing objects:  66% (6/9)   
remote: Compressing objects:  77% (7/9)   
remote: Compressing objects:  88% (8/9)   
remote: Compressing objects: 100% (9/9)   
remote: Compressing objects: 100% (9/9), done.
Receiving objects:   9% (1/11)   
Receiving objects:  18% (2/11)   
Receiving objects:  27% (3/11)   
Receiving objects:  36% (4/11)   
Receiving objects:  45% (5/11)   
Receiving objects:  54% (6/11), 204.00 KiB | 323.00 KiB/s   
Receiving objects:  54% (6/11), 1.23 MiB | 546.00 KiB/s   
Receiving objects:  63% (7/11), 1.23 MiB | 546.00 KiB/s   
Receiving objects:  72% (8/11), 1.23 MiB | 546.00 KiB/s   
Receiving objects:  81% (9/11), 1.23 MiB | 546.00 KiB/s   
remote: Total 11 (delta 0), reused 11 (delta 0), pack-reused 0
Receiving objects:  90% (10/11), 1.23 MiB | 546.00 KiB/s   
Receiving objects: 100% (11/11), 1.23 MiB | 546.00 KiB/s   
Receiving objects: 100% (11/11), 1.71 MiB | 627.00 KiB/s, done.
~~~
{: .output}

~~~
$ tree
~~~
{: .bash}

~~~

└── open-trade-data
    ├── CERDI
    │   └── CERDI-seadistance.dta
    ├── IMF
    │   ├── DOT_02-20-2019\ 15-34-49-99.csv
    │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
    ├── README.md
    ├── UN
    │   └── country-codes.csv
    └── download.sh

4 directories, 6 files
~~~
{: .output}

~~~
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ mkdir code/
$ mkdir analysis_sample/
$ mkdir output/
$ tree
~~~
{: .bash}

~~~

├── analysis_sample
├── code
├── open-trade-data
│   ├── CERDI
│   │   └── CERDI-seadistance.dta
│   ├── IMF
│   │   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
│   ├── README.md
│   ├── UN
│   │   └── country-codes.csv
│   └── download.sh
└── output

7 directories, 6 files
~~~
{: .output}

~~~
$ cd code/
$ ls
$ touch create_analysis_sample.do
$ ls -al
~~~
{: .bash}

~~~

drwxr-xr-x  3 koren  staff   96 Feb 22 13:35 .
drwxr-xr-x  6 koren  staff  192 Feb 22 13:32 ..
-rw-r--r--  1 koren  staff    0 Feb 22 13:35 create_analysis_sample.do
~~~
{: .output}

~~~
$ touch calculate_distances.do
$ touch write_countries_csv.do
$ ls -al
~~~
{: .bash}

~~~

drwxr-xr-x  5 koren  staff  160 Feb 22 13:38 .
drwxr-xr-x  6 koren  staff  192 Feb 22 13:32 ..
-rw-r--r--  1 koren  staff    0 Feb 22 13:37 calculate_distances.do
-rw-r--r--  1 koren  staff    0 Feb 22 13:35 create_analysis_sample.do
-rw-r--r--  1 koren  staff    0 Feb 22 13:38 write_countries_csv.do
~~~
{: .output}

~~~
$ touch read_analysis_sample.do
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ cd ..
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ tree
~~~
{: .bash}

~~~

├── analysis_sample
├── code
│   ├── calculate_distances.do
│   ├── create_analysis_sample.do
│   ├── read_analysis_sample.do
│   └── write_countries_csv.do
├── open-trade-data
│   ├── CERDI
│   │   └── CERDI-seadistance.dta
│   ├── IMF
│   │   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
│   ├── README.md
│   ├── UN
│   │   └── country-codes.csv
│   └── download.sh
└── output

7 directories, 10 files
~~~
{: .output}

~~~
$ mkdir analysis_sample/
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ tree
~~~
{: .bash}

~~~

├── analysis_sample
│   └── distance-to-hungary.dta
├── code
│   ├── calculate_distances.do
│   ├── create_analysis_sample.do
│   ├── read_analysis_sample.do
│   └── write_countries_csv.do
├── open-trade-data
│   ├── CERDI
│   │   └── CERDI-seadistance.dta
│   ├── IMF
│   │   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
│   ├── README.md
│   ├── UN
│   │   └── country-codes.csv
│   └── download.sh
└── output
    └── nearby-countries.csv

7 directories, 12 files
~~~
{: .output}

~~~
$ less output/nearby-countries.csv 
~~~
{: .bash}

~~~

iso_3166_country_code
ABW
AFG
AGO
AIA
ALB
AND
ANT
ARE
ARG
ARM
ASM
ATG
AUS
AUT
AZE
BDI
BEL
BEN
BFA
BGD
BGR
BHR
BHS
BIH
BLR
BLZ
BMU
BOL
BRA
BRB
BRN
BTN
BWA
CAF
CAN
CHE
output/nearby-countries.csv
 ESCOB
CHL
:
 ESCOB
CHN
:
 ESCOB
CIV
:
 ESCOB
CMR
:
 ESCOB
COD
:
 ESCOB
COG
:
 ESCOB
COK
:
 ESCOB
COL
:
 ESCOB
COM
:
 ESCOB
CPV
:
 ESCOB
CRI
:
 ESCOB
CUB
:
 ESCOB
CYM
:
 ESCOB
CYP
:
 ESCOB
CZE
:
 ESCOB
DEU
:
 ESCOB
DJI
:
 ESCOB
DMA
:
 ESCOB
DNK
:
 ESCOB
DOM
:
 ESCOB
DZA
:
 ESCOB
ECU
:
 ESCOB
EGY
:
 ESCOB
ERI
:
 ESCOB
ESP
:
 ESCOB
EST
:
 ESCOB
ETH
:
 ESCOB
FIN
:
 ESCOB
FJI
:
 ESCOB
FLK
:
 ESCOB
FRA
:
 ESCOB
FRO
:
 ESCOB
FSM
:
 ESCOB
GAB
:
 ESCOB
GBR
:
 ESCOB
GEO
:
 ESCOB
GHA
:
 ESCOB
GIB
:
 ESCOB
GIN
:
 ESCOB
GLP
:
 ESCOB
GMB
:
 ESCOB
GNB
:
 ESCOB
GNQ
:
 ESCOB
GRC
:
 ESCOB
GRD
:
 ESCOB
GRL
:
 ESCOB
GTM
:
 ESCOB
GUF
:
 ESCOB
GUM
:
 ESCOB
GUY
:
 ESCOB
HKG
:
 ESCOB
HND
:
 ESCOB
HRV
:
 ESCOB
HTI
:
 ESCOB
IDN
:
 ESCOB
IND
:
 ESCOB
IRL
:
 ESCOB
IRN
:
 ESCOB
IRQ
:
 ESCOB
ISL
:
 ESCOB
ISR
:
 ESCOB
ITA
:
 ESCOB
JAM
:
 ESCOB
JOR
:
 ESCOB
JPN
:
 ESCOB
KAZ
:
 ESCOB
KEN
:
 ESCOB
KGZ
:
 ESCOA
FRA

:
 ESCOB
KGZ
:
 ESCOB
KHM
:
 ESCOB
KIR
:
 ESCOB
KNA
:
 ESCOB
KOR
:
 ESCOB
KWT
:
 ESCOB
LAO
:
49lbash-3.2$ wc -l oooutput/nearby-countries.csv 
      12 output/nearby-countries.csv
~~~
{: .output}

~~~
$ cat output/nearby-countries.csv 
~~~
{: .bash}

~~~

ALB
AUT
BIH
HRV
LIE
MKD
MLT
MNE
SRB
SVK
SVN
~~~
{: .output}

~~~
$ mv code/c⇥reate_analysis_sample.do code/c01_
$ ⇥mv code/read_analysis_sample.do code/02_
$ mv code/calculate_distances.do code/03_
$ mv code/⇥write_countries_csv.do cod04_
$ tree
~~~
{: .bash}

~~~

├── analysis_sample
│   └── distance-to-hungary.dta
├── code
│   ├── 01_create_analysis_sample.do
│   ├── 02_read_analysis_sample.do
│   ├── 03_calculate_distances.do
│   └── 04_write_countries_csv.do
├── open-trade-data
│   ├── CERDI
│   │   └── CERDI-seadistance.dta
│   ├── IMF
│   │   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
│   ├── README.md
│   ├── UN
│   │   └── country-codes.csv
│   └── download.sh
└── output
    └── nearby-countries.csv

7 directories, 12 files
~~~
{: .output}

~~~
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ cd code/
$ pwd
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ls -al
~~~
{: .bash}

~~~

drwxr-xr-x  7 koren  staff  224 Feb 22 14:44 .
drwxr-xr-x  6 koren  staff  192 Feb 22 13:32 ..
-rw-r--r--@ 1 koren  staff  571 Feb 22 14:40 01_create_analysis_sample.do
-rw-r--r--@ 1 koren  staff   54 Feb 22 14:23 02_read_analysis_sample.do
-rw-r--r--@ 1 koren  staff  314 Feb 22 14:08 03_calculate_distances.do
-rw-r--r--@ 1 koren  staff  138 Feb 22 14:29 04_write_countries_csv.do
-rw-r--r--@ 1 koren  staff  108 Feb 22 14:44 master.do
~~~
{: .output}

~~~
$ stata-mp -b do master
$ ls -al
~~~
{: .bash}

~~~

drwxr-xr-x  8 koren  staff   256 Feb 22 14:48 .
drwxr-xr-x  6 koren  staff   192 Feb 22 13:32 ..
-rw-r--r--@ 1 koren  staff   571 Feb 22 14:40 01_create_analysis_sample.do
-rw-r--r--@ 1 koren  staff    54 Feb 22 14:23 02_read_analysis_sample.do
-rw-r--r--@ 1 koren  staff   314 Feb 22 14:08 03_calculate_distances.do
-rw-r--r--@ 1 koren  staff   138 Feb 22 14:29 04_write_countries_csv.do
-rw-r--r--@ 1 koren  staff   108 Feb 22 14:44 master.do
-rw-r--r--  1 koren  staff  2501 Feb 22 14:48 master.log
~~~
{: .output}

~~~
$ tail mas⇥ter.log 
~~~
{: .bash}

~~~


. export delimited using ../output/nearby-countries.csv, replace
file ../output/nearby-countries.csv saved

. 
end of do-file

. 
end of do-file
~~~
{: .output}

~~~
$ ls -al ../output/nearby-countries.csv 
~~~
{: .bash}

~~~

~~~
{: .output}

~~~
$ ⇥tree ..
~~~
{: .bash}

~~~

├── analysis_sample
│   └── distance-to-hungary.dta
├── code
│   ├── 01_create_analysis_sample.do
│   ├── 02_read_analysis_sample.do
│   ├── 03_calculate_distances.do
│   ├── 04_write_countries_csv.do
│   ├── master.do
│   └── master.log
├── open-trade-data
│   ├── CERDI
│   │   └── CERDI-seadistance.dta
│   ├── IMF
│   │   ├── DOT_02-20-2019\ 15-34-49-99.csv
│   │   └── Metadata_DOT_02-20-2019\ 15-34-49-99.csv
│   ├── README.md
│   ├── UN
│   │   └── country-codes.csv
│   └── download.sh
└── output
    └── nearby-countries.csv

7 directories, 14 files
~~~
{: .output}

~~~
$ # end of stata episode 1 1453
$ history 100 > history.txt
$ less history.txt 
~~~
{: .bash}

