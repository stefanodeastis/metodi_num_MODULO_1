#!/usr/bin/env python3
# Copyright (C) 2022 s.deastis@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#uniform=np.array([random.random() for i in range (LUNGH)])
import argparse
import time
import random
import numpy as np
import matplotlib.pyplot as plt
'''
LUNGH=int(1e06)
SIGMA=1
mean=10
'''
def version1 (start,delta):
    random.seed(1)
    gaussian=np.array([start])
    for i in range (LUNGH):

    #genero un numero nell'intervallo [x_k-delta,x_k+delta]
        x_p=random.random()*2*delta+gaussian[i]-delta
        prob=np.e**((-(x_p-mean)**2+(gaussian[i]-mean)**2)/(2*SIGMA**2))
        if random.random() <= prob:
            gaussian=np.append(gaussian,x_p)
        else:
            gaussian=np.append(gaussian,gaussian[i])
    return gaussian

def version2 (start,delta):
    random.seed(1)
    uniform=np.array([random.random() for i in range (LUNGH)])
    gaussian=np.array([start])
    random.seed(2)
    for i in range (LUNGH):

    #genero un numero nell'intervallo [x_k-delta,x_k+delta]
        x_p=random.random()*2*delta+gaussian[i]-delta
        prob=np.e**((-(x_p-mean)**2+(gaussian[i]-mean)**2)/(2*SIGMA**2))
        if uniform[i] <= prob:
            gaussian=np.append(gaussian,x_p)
        else:
            gaussian=np.append(gaussian,gaussian[i])
    return gaussian

def version3 (start,delta,n_generated, mean, dev_std):
    random.seed(time.time())
    uniform=np.array([random.random() for i in range (n_generated)])
    gaussian=np.zeros(n_generated)
    gaussian[0]=start
    random.seed(time.time())
    prove=np.array([random.random() for i in range (n_generated)])

    for i in range (n_generated-1):
        x_p=prove[i]*2*delta+gaussian[i]-delta
    #genero un numero nell'intervallo [x_k-delta,x_k+delta]
        prob=np.e**((-(x_p-mean)**2+(gaussian[i]-mean)**2)/(2*dev_std**2))
        if uniform[i] <= prob:
            gaussian[i+1]=x_p
        else:
            gaussian[i+1]=gaussian[i]
    return gaussian


def dati(array,n_generated):
    mean=np.mean(gauss)
    devstd= np.sqrt(((array-mean)**2).sum()/((n_generated-1)*n_generated))
    print(f'la media della gaussiana è: {mean}+- {devstd}')
    return
if __name__ == '__main__':
    '''da mettere gli argparse per seed, x0, media, sigma,delta
    '''
    start=time.time()
    parser = argparse.ArgumentParser(description='generatore di una gaussiana')
    parser.add_argument('-m','--mean', type=float, help='mean of the gaussian',default=0)
    parser.add_argument('-dev','--devstd', type=float, help='devstd of the gaussian',default=1)
    parser.add_argument('-s','--start', type=float, help='x_0 of the algorithm',default=0)
    parser.add_argument('-d','--delta', type=float, help='delta of the algorithm',default=1)
    parser.add_argument('-n','--n_tot', type=int, help='number of generated points',default=int(1e06))
    #parser.add_argument('devstd', type=float, help='devstd of the gaussian')
    args = parser.parse_args()
    #mean=args.mean
    #gauss=version1(x_0,1)
    #gauss=version2(x_0,1)

    gauss=version3(args.start,args.delta,args.n_tot,args.mean,args.devstd)
    #uniform=np.array([random.random() for i in range (LUNGH)])
    dati(gauss,args.n_tot)

    plt.hist(gauss,histtype='step',stacked=True, bins=40)
    '''
    plt.figure(1)
    plt.errorbar([1,2,3,4],[2,12,26,47],color='black')
    x=np.linspace(0.,4.,10)
    print(x)
    plt.plot(x,x)
    plt.plot(x,x**2,color='green')
    plt.plot(x,x**2*np.log(x),color='red')
    '''
    end=time.time()
    print("time elapsed=",end-start)
    plt.show()
