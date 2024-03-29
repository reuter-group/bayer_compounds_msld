#! /usr/bin/env python

import sys, os
import numpy as np
from subprocess import call

if len(sys.argv)==2:
  production=False
  istep=int(sys.argv[1])
  ndupl=1
elif len(sys.argv)==5:
  production=True
  istep=int(sys.argv[1])
  ndupl=int(sys.argv[2])
  begres=int(sys.argv[3])
  endres=int(sys.argv[4])
else:
  print("Error: Need 1 argument for flattening or 4 arguments for production")
  quit()

nblocks=np.loadtxt('../nblocks',dtype='int')
nsubs=np.loadtxt('../nsubs',dtype='int',ndmin=1)
nreps=np.loadtxt('../nreps',dtype='int')

fp=open('../name','r')
name=fp.readline().strip()
fp.close()

if not os.path.isdir('data'):
  os.mkdir('data')
DIR="data"

# ------------------------------------------------------------------------------

alphabet='abcdefghijklmnopqrstuvwxyz'

for idupl in range(0,ndupl):

  DDIR='../run'+str(istep)
  if production:
    DDIR=DDIR+alphabet[idupl]

  datasplit=[]

  for i in range(0,nreps):
    fnmsin=[]
    if production:
      for j in range(begres,endres):
        fnmsin.append(DDIR+'/res/'+name+'_prod'+str(j+1)+'.lmd_'+str(i))
    else:
      fnmsin.append(DDIR+'/res/'+name+'_flat.lmd_'+str(i))
    fnmout=DIR+("/Lambda.%d.node%d.dat" % (idupl,i))
    call(['../ALF/GetLambda.py',fnmout]+fnmsin)
    datasplit.append(np.loadtxt(fnmout))

  nsteps=len(datasplit[-1])

# ------------------------------------------------------------------------------
  if nreps==1:
    fnmin=DIR+("/Lambda.%d.node%d.dat" % (idupl,0))
    fnmout=DIR+("/Lambda.%d.%d.dat" % (idupl,0))
    call(['mv',fnmin,fnmout])
  else:
# ------------------------------------------------------------------------------

    fpex=open(DIR+'/rex.'+str(idupl)+'.exch',"w")
    if production:
      startline=0
      for j in range(begres,endres):
        fp=open(DDIR+'/'+name+'_prod'+str(j+1)+'.rex_0','r')
        for line in fp.readlines()[startline:]:
          fpex.write(line)
        fp.close()
        startline=1
    else:
      fp=open(DDIR+'/'+name+'_heat.rex_0','r')
      fpex.write(fp.readline())
      fp.close()
      fp=open(DDIR+'/'+name+'_flat.rex_0','r')
      for line in fp.readlines():
        fpex.write(line)
      fp.close()
    fpex.close()

# ------------------------------------------------------------------------------

    fpex=open(DIR+'/rex.'+str(idupl)+'.exch',"r")
    fpex.readline()

    bpstate=[]

    line=fpex.readline()
    while line[0]=="#":
      bpstate.append([])
      for i in range(0,nreps):
        line=fpex.readline()
        bpstate[-1].append(int(line.split()[0])-1)
      line=fpex.readline()
      if len(line)==0:
        break
    fpex.close()

    fpex=open(DIR+'/ex.'+str(idupl)+'.dat',"w")
    for s in bpstate:
      line=""
      for d in s:
        line+=(" %d" % (d,))
      line+="\n"
      fpex.write(line)
    fpex.close()

    NEXCH=len(bpstate)

# ------------------------------------------------------------------------------

    fp=[]
    for rep in range(0,nreps):
      fnm=DIR+("/Lambda.%d.%d.dat" % (idupl,rep))
      fp.append(open(fnm,"w"))

    for i in range(0,nsteps):
      for rep in range(0,nreps):
        node=bpstate[i*NEXCH/nsteps][rep]
        row=datasplit[node][i,:]
        line=""
        for entry in row:
          line+=(" %f" % entry)
        line+="\n"
        fp[rep].write(line)
        # fp[bpstate[0][rep]].write(line)

    for f in fp:
      f.close()
