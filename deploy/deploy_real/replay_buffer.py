import numpy as np
import matplotlib.pyplot as plt
import csv

colors = np.array([
    [0, 113, 186],  # deep blue
    [219, 92, 48],  # orange
    [236, 175, 55], # yellow
    [123, 48, 137], # purple
    [120, 170, 61], # green
    [74, 190, 235],  # lite blue
    [192,192,192],
]) / 255

class ReplayBuffer():
    def __init__(self,max_replay_buffer_size,flag='real'):
        self.max_replay_buffer_size = max_replay_buffer_size
        self.ang_vel = np.zeros((self.max_replay_buffer_size,3))
        self.gravity_orientation = np.zeros((self.max_replay_buffer_size,3))
        self.dof_pos = np.zeros((self.max_replay_buffer_size,12))
        self.dof_vel = np.zeros((self.max_replay_buffer_size,12))
        self.actions = np.zeros((self.max_replay_buffer_size,12))
        self.flag = flag
        self.clear()

    def clear(self):
        self._top = 0
        self._size = 0

    def _advance(self):
        self._top = (self._top + 1) % self.max_replay_buffer_size
        if self._size < self.max_replay_buffer_size:
            self._size += 1

    def add_sample(self,ang_vel=None,gravity_orientation=None,dof_pos=None,dof_vel=None,actions=None):
        self.ang_vel[self._top] = ang_vel
        self.gravity_orientation[self._top] = gravity_orientation
        self.dof_pos[self._top] = dof_pos
        self.dof_vel[self._top] = dof_vel
        self.actions[self._top] = actions
        self._advance()

    def plot_ang_vel(self,record=True):
        steps = np.arange(0,self.max_replay_buffer_size,1)
        for i in range(3):
            plt.subplot(1,3,i+1)
            plt.plot(steps,self.ang_vel[:,i],color=colors[0],linewidth=1.0,label='ang_vel_{}'.format(self.flag))
            plt.legend()
        if record:
            with open('data/ang_vel_{}.csv'.format(self.flag),'w',newline='') as file_obj:
                writer = csv.writer(file_obj)
                for i in range(3):
                    writer.writerow(self.ang_vel[:,i])
        plt.show()

    def plot_gravity(self,record=True):
        steps = np.arange(0,self.max_replay_buffer_size,1)
        for i in range(3):
            plt.subplot(1,3,i+1)
            plt.plot(steps,self.gravity_orientation[:,i],color=colors[0],linewidth=1.0,label='gravity_{}'.format(self.flag))
            plt.legend()
        if record:
            with open('data/gravity_{}.csv'.format(self.flag),'w',newline='') as file_obj:
                writer = csv.writer(file_obj)
                for i in range(3):
                    writer.writerow(self.gravity_orientation[:,i])
        plt.show()

    def plot_dof_pos(self,record=True):
        steps = np.arange(0,self.max_replay_buffer_size,1)
        for i in range(12):
            plt.subplot(4,3,i+1)
            base_label = '_dof_pos_' + self.flag
            if i == 0: label = 'FL_hip' + base_label
            elif i == 1: label = 'FL_thigh' + base_label
            elif i== 2: label = 'FL_calf' + base_label
            elif i == 3: label = 'FR_hip' + base_label
            elif i == 4: label = 'FR_thigh' + base_label
            elif i == 5: label = 'FR_calf' + base_label
            elif i == 6: label = 'HL_hip' + base_label
            elif i == 7: label = 'HL_thigh' + base_label
            elif i == 8: label = 'HL_calf' + base_label
            elif i == 9: label = 'HR_hip' + base_label
            elif i == 10: label = 'HR_thigh' + base_label
            elif i == 11: label = 'HR_calf' + base_label
            plt.plot(steps,self.dof_pos[:,i],color=colors[0],label=label,linewidth=1.0)
            plt.legend()
        if record:
            with open('data/dof_pos_{}.csv'.format(self.flag),'w',newline='') as file_obj:
                writer = csv.writer(file_obj)
                for i in range(12):
                    writer.writerow(self.dof_pos[:,i])
        plt.show()

    def plot_dof_vel(self,record=True):
        steps = np.arange(0,self.max_replay_buffer_size,1)
        for i in range(12):
            plt.subplot(4,3,i+1)
            base_label = '_dof_vel_' + self.flag
            if i == 0: label = 'FL_hip' + base_label
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
            plt.plot(steps,self.dof_vel[:,i],color=colors[0],label=label,linewidth=1.0)
            plt.legend()
        if record:
            with open('data/dof_vel_{}.csv'.format(self.flag),'w',newline='') as file_obj:
                writer = csv.writer(file_obj)
                for i in range(12):
                    writer.writerow(self.dof_vel[:,i])
        plt.show()

    def plot_actions(self,record=True):
        steps = np.arange(0,self.max_replay_buffer_size,1)
        for i in range(12):
            plt.subplot(4,3,i+1)
            base_label = '_actions_' + self.flag
            if i == 0: label = 'FL_hip' + base_label
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
            plt.plot(steps,self.actions[:,i],color=colors[0],label=label,linewidth=1.0)
            plt.legend()
        if record:
            with open('data/actions_{}.csv'.format(self.flag),'w',newline='') as file_obj:
                writer = csv.writer(file_obj)
                for i in range(12):
                    writer.writerow(self.actions[:,i])
        plt.show()







