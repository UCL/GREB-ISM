# GREB-ISM
Code for Globally Resolved Energy Balance - Ice Sheet Model (GREB-ISM)


## Original Code

This is a 'fork' of [a previous work](https://github.com/YMI33/GREB-ISM).

## Prerequirment
* Fortran (gfortran)

## File systems
* input: binary files for model input
* job-script: csh script for running model
* src: source code for model
* experiment: directory for storing experiment results

## Job script 
* greb-ice-sheet.exp-scenario.newstart.com     coupled experiment (dynamic equalibrium and shortwave oscilation experiment) 
* run.greb.imodel.verify.csh                   EISMINT I/II experiments
* run.greb.icealone.(restart.)csh              new start (restart) standalone experiment           

## Model running instruction
1. edit job script in *GREB-ISM/job-script/*
2. change environment variable **WDIR** to the absolute path of your GREB-ISM 
3. change experiment setting (EXP:experiment number, KYRSTART:start date of experiment, etc.)
4. run job script
5. you can access the experiment output in *GREB-ISM/experiment*, which are binary files in [GrADS format](http://cola.gmu.edu/grads/gadoc/aboutgriddeddata.html#structure). You can easily read the data by CTL files in the same directory through GrADS. 


