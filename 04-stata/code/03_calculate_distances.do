* first you go to port, then ship by sea, then go from port to capital
generate total_distance = capitalport1 + seadistance + capitalport2
label var total_distance "Total distance between capitals (by sea, km)"

* beware: missing is greater than any number
drop if total_distance > 2000 & !missing(total_distance)
