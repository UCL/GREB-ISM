"open ../../input/erainterim.atmospheric_humidity.clim.ctl";

time = 1

while (time <= 730)
"c";
"set t "time;
"d q";
"printim test_"time".png";
time = time + 1
endwhile

"quit";
