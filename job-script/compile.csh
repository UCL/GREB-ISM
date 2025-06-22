if ($COMPILE == 1) then
echo ''
echo 'compile GREB model'
cd $WDIR/experiments/$NAME/work/
set ICE   = $MDIR/ice-sheet.f90
set MAIN  = $MDIR/greb.main.f90
set OCEN  = $MDIR/greb.ocean.f90
set ATMO  = $MDIR/greb.atmosphere.f90
\rm -f greb.x *.mod

### gfortran compiler (Linux (e.g. Ubuntu), Unix or MacBook Air)
gfortran -fopenmp -march=native -O3 -ffast-math -funroll-loops $MAIN $ATMO $OCEN $ICE -o greb.x
### ifort compiler (Linux, Unix or MacBook Air), contributed by Dr. Wang Yue 
# ifort -qopenmp -qopenmp-link=static -O3 -fast -assume byterecl $MAIN $ATMO $OCEN $ICE -o greb.x

endif 
