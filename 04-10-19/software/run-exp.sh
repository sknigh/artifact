#!/bin/bash

# spack code originally sourced from here
# git clone -b 'feature/parallelbuild4' https://github.com/sknigh/spack.git

# configure python environment
virtualenv -p python36 venv
source venv/bin/activate
pip install numpy

# configure spack environment
source spack/share/spack/setup-env.sh

# change sequence max to number of cores on your machine
# can use stepping > 1 if shorter execution time is desired
j_lst=(`seq 1 28`)
stack_lst=('python' 'tk' 'rust@1.33.0' 'r' 'xsdk')

# xSDK is sensitive to compiler version
compiler='%gcc@6.4.0'


# create a timings database, skip this loop if you already have a timings.sqlite3
# this script here will clean everything (clean -a) then fetch, this time consuming is not usually necessary.
# It was done because the rust build system gets very finicky when it discovers a cache.
for j in "${j_lst[@]}"; do
    # clean up the environment
    spack uninstall --all -f -y
    spack clean -a
    spack -k fetch -D python tk rust r xsdk

    # collect timings for each dependency, will generate 'timings.sqlite3'
    for stack in "${stack_lst[@]}"; do
        spack -k install -j $j --time-phases "$stack $compiler"
    done
done


# run with schedulers and place logs in output directory
# these runs included CPA, although it wasn't used in the final paper
mkdir output
for stack in 'python' 'tk' 'rust@1.33.0' 'r' 'xsdk'; do
    # scheduler case
    for sched in 'cpr' 'filteredcpr' 'cpa' 'mcpa'; do
        spack uninstall --all -f -y
        spack clean -a
        spack -k fetch -D python tk r xsdk
        spack -k install --use-timings timings.sqlite3 --scheduler $sched "$stack $compiler" > output/$sched-$stack.txt
    done

    spack uninstall --all -f -y
    spack clean -a
    spack -k fetch -D python tk r xsdk

    # sequential case
    sched='serial'
    spack -k install "$stack $compiler" > output/$sched-$stack.txt
done


# collect parsable results from the output
grep -r finished output/
