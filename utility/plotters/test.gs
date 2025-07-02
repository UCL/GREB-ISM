START_TIME = 1
END_TIME = 730
"open ../../input/erainterim.atmospheric_humidity.clim.ctl";

time = START_TIME

while (time <= END_TIME)
"c";
"set t "time;
"d q";
"printim ../../plots/test_"time".png";
time = time + 1
endwhile

"quit";
