import numpy as np
import csv
from matplotlib import pyplot as plt

colors = np.array([
    [0, 113, 186],  # deep blue
    [219, 92, 48],  # orange
    [236, 175, 55], # yellow
    [123, 48, 137], # purple
    [120, 170, 61], # green
    [74, 190, 235],  # lite blue
    [192,192,192],
]) / 255

def compare_actions(real_path=None,sim_path=None):
    plt.figure(figsize=(10, 6))
    steps = np.arange(0,200,1)
    with open(real_path,'r') as fd:
        reader = csv.reader(fd)
        for i,row in zip(range(12),reader):
            row_tmp = row
            base_label = '_actions'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4,3,i+1)
            if i == 0: label = 'FL_hip' + base_label
            elif i == 1: label = 'FL_thigh' + base_label
            elif i == 2: label = 'FL_calf' + base_label
            elif i == 3: label = 'FR_hip' + base_label
            elif i == 4: label = 'FR_thigh' + base_label
            elif i == 5: label = 'FR_calf' + base_label
            elif i == 6: label = 'HL_hip' + base_label
            elif i == 7: label = 'HL_thigh' + base_label
            elif i == 8: label = 'HL_calf' + base_label
            elif i == 9: label = 'HR_hip' + base_label
            elif i == 10: label = 'HR_thigh' + base_label
            elif i == 11: label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[0], label=label+'_real', linewidth=1.0)
            plt.legend()
    with open(sim_path, 'r') as fd:
        reader = csv.reader(fd)
        for i, row in zip(range(12), reader):
            row_tmp = row
            base_label = '_actions'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4, 3, i + 1)
            if i == 0:label = 'FL_hip' + base_label
            elif i == 1:label = 'FL_thigh' + base_label
            elif i == 2:label = 'FL_calf' + base_label
            elif i == 3:label = 'FR_hip' + base_label
            elif i == 4:label = 'FR_thigh' + base_label
            elif i == 5:label = 'FR_calf' + base_label
            elif i == 6:label = 'HL_hip' + base_label
            elif i == 7:label = 'HL_thigh' + base_label
            elif i == 8:label = 'HL_calf' + base_label
            elif i == 9:label = 'HR_hip' + base_label
            elif i == 10:label = 'HR_thigh' + base_label
            elif i == 11:label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[1], label=label+"_sim", linewidth=1.0)
            plt.legend()

    plt.show()

def compare_dof_pos(real_path=None,sim_path=None):
    plt.figure(figsize=(10, 6))
    steps = np.arange(0,200,1)
    with open(real_path,'r') as fd:
        reader = csv.reader(fd)
        for i,row in zip(range(12),reader):
            row_tmp = row
            base_label = '_dof_pos'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4,3,i+1)
            if i == 0: label = 'FL_hip' + base_label
            elif i == 1: label = 'FL_thigh' + base_label
            elif i == 2: label = 'FL_calf' + base_label
            elif i == 3: label = 'FR_hip' + base_label
            elif i == 4: label = 'FR_thigh' + base_label
            elif i == 5: label = 'FR_calf' + base_label
            elif i == 6: label = 'HL_hip' + base_label
            elif i == 7: label = 'HL_thigh' + base_label
            elif i == 8: label = 'HL_calf' + base_label
            elif i == 9: label = 'HR_hip' + base_label
            elif i == 10: label = 'HR_thigh' + base_label
            elif i == 11: label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[0], label=label+'_real', linewidth=1.0)
            plt.legend()
    with open(sim_path, 'r') as fd:
        reader = csv.reader(fd)
        for i, row in zip(range(12), reader):
            row_tmp = row
            base_label = '_dof_pos'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4, 3, i + 1)
            if i == 0:label = 'FL_hip' + base_label
            elif i == 1:label = 'FL_thigh' + base_label
            elif i == 2:label = 'FL_calf' + base_label
            elif i == 3:label = 'FR_hip' + base_label
            elif i == 4:label = 'FR_thigh' + base_label
            elif i == 5:label = 'FR_calf' + base_label
            elif i == 6:label = 'HL_hip' + base_label
            elif i == 7:label = 'HL_thigh' + base_label
            elif i == 8:label = 'HL_calf' + base_label
            elif i == 9:label = 'HR_hip' + base_label
            elif i == 10:label = 'HR_thigh' + base_label
            elif i == 11:label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[1], label=label+"_sim", linewidth=1.0)
            plt.legend()

    plt.show()

def compare_dof_vel(real_path=None,sim_path=None):
    plt.figure(figsize=(10, 6))
    steps = np.arange(0,200,1)
    with open(real_path,'r') as fd:
        reader = csv.reader(fd)
        for i,row in zip(range(12),reader):
            row_tmp = row
            base_label = '_dof_vel'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4,3,i+1)
            if i == 0: label = 'FL_hip' + base_label
            elif i == 1: label = 'FL_thigh' + base_label
            elif i == 2: label = 'FL_calf' + base_label
            elif i == 3: label = 'FR_hip' + base_label
            elif i == 4: label = 'FR_thigh' + base_label
            elif i == 5: label = 'FR_calf' + base_label
            elif i == 6: label = 'HL_hip' + base_label
            elif i == 7: label = 'HL_thigh' + base_label
            elif i == 8: label = 'HL_calf' + base_label
            elif i == 9: label = 'HR_hip' + base_label
            elif i == 10: label = 'HR_thigh' + base_label
            elif i == 11: label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[0], label=label+'_real', linewidth=1.0)
            plt.legend()
    with open(sim_path, 'r') as fd:
        reader = csv.reader(fd)
        for i, row in zip(range(12), reader):
            row_tmp = row
            base_label = '_dof_vel'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4, 3, i + 1)
            if i == 0:label = 'FL_hip' + base_label
            elif i == 1:label = 'FL_thigh' + base_label
            elif i == 2:label = 'FL_calf' + base_label
            elif i == 3:label = 'FR_hip' + base_label
            elif i == 4:label = 'FR_thigh' + base_label
            elif i == 5:label = 'FR_calf' + base_label
            elif i == 6:label = 'HL_hip' + base_label
            elif i == 7:label = 'HL_thigh' + base_label
            elif i == 8:label = 'HL_calf' + base_label
            elif i == 9:label = 'HR_hip' + base_label
            elif i == 10:label = 'HR_thigh' + base_label
            elif i == 11:label = 'HR_calf' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[1], label=label+"_sim", linewidth=1.0)
            plt.legend()

    plt.show()

def compare_ang_vel(real_path=None,sim_path=None):
    plt.figure(figsize=(10, 6))
    steps = np.arange(0,200,1)
    with open(real_path,'r') as fd:
        reader = csv.reader(fd)
        for i,row in zip(range(3),reader):
            row_tmp = row
            base_label = '_ang_vel'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4,3,i+1)
            if i == 0: label = 'x' + base_label
            elif i == 1: label = 'y' + base_label
            elif i == 2: label = 'z' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[0], label=label+'_real', linewidth=1.0)
            plt.legend()
    with open(sim_path, 'r') as fd:
        reader = csv.reader(fd)
        for i, row in zip(range(3), reader):
            row_tmp = row
            base_label = '_ang_vel'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4, 3, i + 1)
            if i == 0:label = 'x' + base_label
            elif i == 1:label = 'y' + base_label
            elif i == 2:label = 'z' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[1], label=label+"_sim", linewidth=1.0)
            plt.legend()

    plt.show()

def compare_gravity(real_path=None,sim_path=None):
    plt.figure(figsize=(10, 6))
    steps = np.arange(0,200,1)
    with open(real_path,'r') as fd:
        reader = csv.reader(fd)
        for i,row in zip(range(3),reader):
            row_tmp = row
            base_label = '_gravity'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4,3,i+1)
            if i == 0: label = 'x' + base_label
            elif i == 1: label = 'y' + base_label
            elif i == 2: label = 'z' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[0], label=label+'_real', linewidth=1.0)
            plt.legend()
    with open(sim_path, 'r') as fd:
        reader = csv.reader(fd)
        for i, row in zip(range(12), reader):
            row_tmp = row
            base_label = '_gravity'
            for j in range(len(row_tmp)):
                row_tmp[j] = float(row_tmp[j])
            plt.subplot(4, 3, i + 1)
            if i == 0:label = 'x' + base_label
            elif i == 1:label = 'y' + base_label
            elif i == 2:label = 'z' + base_label
            plt.plot(steps, row_tmp[:200], color=colors[1], label=label+"_sim", linewidth=1.0)
            plt.legend()

    plt.show()

compare_actions(real_path='data/actions_real.csv',
                sim_path='actions_sim_v2.csv')
compare_dof_pos(real_path='data/dof_pos_real.csv',
                sim_path='dof_pos_sim_v2.csv')
compare_dof_vel(real_path='data/dof_vel_real.csv',
                sim_path='dof_vel_sim_v2.csv')
compare_ang_vel(real_path='data/ang_vel_real.csv',
                sim_path='ang_vel_sim_v2.csv')
compare_gravity(real_path='data/gravity_real.csv',
                sim_path='gravity_sim_v2.csv')


