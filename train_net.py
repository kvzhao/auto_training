#! /usr/bin/env python
import os, sys
import subprocess
import datetime

# path define 
# global call
sys_path = '/home/kv/workspace/'
caffe_rootdir = sys_path + 'trackers_ranking/caffe_for_trackerRank/'
caffe_path = caffe_rootdir + 'build/tools/'

task_name = 'trackerRanking/'
task_dir =  caffe_rootdir + task_name
# local dir path
solver_dir = task_name + 'solvers/'
model_dir = task_name + 'models/'
result_dir = task_name + 'results/'

# program and options
caffe_exe = caffe_path + 'caffe.bin'
solver_name = 'conv6fc2_csknet_solver.prototxt'
flag_mode = 'train'
flag_solver = '--solver=' + solver_dir + solver_name

# train
t = datetime.datetime.now()
s = t.strftime('_%H:%M:%S_%m_%d_%Y')
result_log_name = solver_name.split('_')[0] + s + '.log'
f = open(result_dir + result_log_name, 'wb')
subprocess.call([caffe_exe, flag_mode, flag_solver], stderr=f)


