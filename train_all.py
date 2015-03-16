#! /usr/bin/env python
import os, sys
import subprocess
import datetime
import time

# path define 
# global call

## ------ path of caffe program ----- ##
sys_path = '/home/kv/research/'
caffe_rootdir = sys_path + 'trackers_ranking/caffe_for_trackerRank/'
caffe_path = caffe_rootdir + 'build/tools/'

task_name = os.getcwd().split('/')[-1]
task_path = os.getcwd()
## ------ path of task package ----- ##
print 'The task is called', task_name
# local dir path
solver_dir = task_path + '/solvers/'
model_dir = task_path + '/models/'
result_dir = task_path + '/results/'
log_dir    = task_path + '/logs/'

# program and options
caffe_exe = caffe_path + 'caffe.bin'

# traverse the solver dir
for root, dirs, files in os.walk(solver_dir):
    for idx, solver in enumerate(files):
        print '--------------------------------------------------------------------'
        solver_name = solver
        solver_list = solver_name.split('_')
        arch = solver_list[0]
        feat = solver_list[1]
        print 'loading solver', arch, "# ", idx
        flag_mode = 'train'
        flag_solver = '--solver=' + solver_dir + solver_name
        # train
        t = datetime.datetime.now()
        s = t.strftime('_%Y-%m-%d-%H-%M-%S')
        result_log_name =  '_'.join([arch, feat]) +s+ '.log'
        start_time = time.time()
        f = open(log_dir + result_log_name, 'wb')
        print 'call', caffe_exe, flag_mode, flag_solver
        subprocess.call([caffe_exe, flag_mode, flag_solver], stderr=f)
        f.close()
        print 'train', solver_name, 'is done\n  cost', time.time()-start_time, 'secs in total'
        print '--------------------------------------------------------------------\n'



