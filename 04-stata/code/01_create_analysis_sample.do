* relative path to data folder
use ../open-trade-data/CERDI/CERDI-seadistance.dta, clear
* as opposed to: /Users/koren/Documents/stata-batch/open-trade-data/CERDI/CERDI-seadistance.dta
* as opposed to: cd /Users/koren/Documents/stata-batch/open-trade-data/CERDI/
* as opposed to: global path = /Users/koren/Documents/stata-batch/open-trade-data/CERDI/ (this is second best)

keep if iso1=="HUN"

* all countries with missing values are coastal
mvencode capitalport*, mv(0) override

save ../analysis_sample/distance-to-hungary.dta, replace
* always add a new line at end
