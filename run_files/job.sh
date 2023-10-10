#!/bin/bash

./runset2.sh &>> 2phase.log

./runset3.sh  &>> 3phase.log

./subset4.sh
