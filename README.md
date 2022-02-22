# Semi-Sequence-Alignment-with-Cuda  
## What I have done
As the topic, semi sequence alignment with cuda technique. However, I don't do this by one program but two.  
1. the program [semi_interval](./src/semi_interval/main.cu), will calculate out best score with semi x,y first, then generate x,y's semi inteval.  
2. the program [alignment](./src/semi_interval/main.cu), will align the sequence x,y with the interval, although this is global align, but we have semi interval to do this, so result will as same as just do local sequence alignment.  
## Config
you can edit config in [config.h](./src/headers/config.h), this config is a part of program, so it will optialize with compiler.  
In this file, you can edit output file location, score matrix, cuda, sequence x,y's start and end is free or fixed and so on.
 
## How to use  
You need to go to source directory [src](./src/), then use `make`.  
* `make cpu.exe` just use cpu run global alignment score, there is no semi function, so it just let you can compare cpu's performance with gpu's or, the global alignment score is realy the same as the program run with cuda(set x,y's start,end to fixed).  
* `make semi_interval.exe` compiler config and calcuate best score and its interval with cuda.  
* `make alignment.exe` generate best score's alignment with cuda and interal generated by `semi_interval.exe`, and this program also check the alignment's socre.  
## Performance  
In this version, I change the array storage to fit coalescing, the this improve the performace, following is the comparison.  
And I also make #if to let memory of afg_unit reduce, the improve is crazy.  
```cmd
x: fixed start, fixed end, size= 16641
y: fixed start, fixed end, size=118436
```
Pragram           | Branch  | Time 
--------------|:-----:|:----:
cpu.exe    | - | 65.37s 
semi_interval.exe | reduce memory of afg_unit |  1.40s
semi_interval.exe | coalescing |  11.57s
alignment.exe | coalescing | 24.38s
semi_interval.exe |no coalescing |  35.58s
alignment.exe |no coalescing | 40.35s

x start | x end | y start | y end |Time
:-----:|:-----:|:-----:|:-----:|:-----:
fixed|fixed|fixed|fixed|1.54s
free|free|fixed|fixed|4.14s
fixed|fixed|free|free|4.13s
free|free|free|free|7.07s

## Test  
### enviroment 
**`OS`** `win10`  
**`nvidia-smi`**  
```cmd
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 471.41       Driver Version: 471.41       CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ... WDDM  | 00000000:01:00.0 Off |                  N/A |
| N/A   59C    P8     8W /  N/A |    134MiB /  4096MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```
### result  
**`make semi_interval.exe`**  
```txt
X sequence: ../res/x.txt , Global interval=[1, 16641]
Y sequence: ../res/y.txt , Global interval=[1, 118436]

Time taken: 1.40s
Best interval saved in: ../res/best.txt

Best score: -90273
score= -90273; x=[1, 16641]; y=[1, 118436]
```
**`make cpu.exe`**
```txt
Time taken: 65.37s
Best global alignment score: -90273
```
**`make alignment.exe`**
```txt
Load semi interval from ../res/best.txt , Index=100, Score=-90273
X sequence: ../res/x.txt , Semi interval=[1, 16641]
Y sequence: ../res/y.txt , Semi interval=[1, 118436]

Time taken: 24.38s
Best score: -90273
The score of alignment ../res/alignment.txt is -90273
```
