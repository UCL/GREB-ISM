#!/bin/csh

set scriptdir = $PWD

echo 'Script directory: ' $scriptdir

source $scriptdir/set_parameters.csh
source $scriptdir/make_output_directories.csh
source $scriptdir/compile.csh
source $scriptdir/run_model.csh
