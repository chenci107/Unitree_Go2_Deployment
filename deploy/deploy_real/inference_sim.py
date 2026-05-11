import sys
from legged_gym import LEGGED_GYM_ROOT_DIR
import os
import sys
from legged_gym import LEGGED_GYM_ROOT_DIR

import isaacgym
from legged_gym.envs import *
from legged_gym.utils import get_args, export_policy_as_jit, task_registry, Logger

import numpy as np
import torch
from deploy.deploy_real.replay_buffer import ReplayBuffer


def play(args):
    env_cfg, train_cfg = task_registry.get_cfgs(name=args.task)
    # override some parameters for testing
    env_cfg.env.num_envs = min(env_cfg.env.num_envs, 100)
    env_cfg.terrain.num_rows = 5
    env_cfg.terrain.num_cols = 5
    env_cfg.terrain.curriculum = False
    env_cfg.noise.add_noise = False
    env_cfg.domain_rand.randomize_friction = False
    env_cfg.domain_rand.push_robots = False

    env_cfg.env.test = True

    # prepare environment
    env, _ = task_registry.make_env(name=args.task, args=args, env_cfg=env_cfg)
    obs = env.get_observations()

    policy = torch.jit.load(
        "/home/cc/code/isaac_gym_all_code/LENGTH_CHANGED_ALL_TASKS/deployment_all/unitree_rl_gym_0528/deploy/pre_train/go2/motion.pt",
        map_location='cuda:0')
    policy.eval()

    # replay_buffer = ReplayBuffer(max_replay_buffer_size=200,flag='sim_v2')

    for i in range(1 * int(env.max_episode_length)):
        actions = torch.tensor([0.1, 0.8, -1.5,
                 -0.1, 0.8, -1.5,
                0.1, 1.0, -1.5,
                -0.1, 1.0, -1.5]).unsqueeze(0).expand(100,-1).to('cuda:0')
        if i < 100:
            actions = torch.tensor([
                0.1,0.8,-1.5,
                -0.1,0.8,1.5,
                0.1,1.0,-1.5,
                -0.1,1.0,1.5
            ]).unsqueeze(0).expand(100,-1).to('cuda:0')
            obs, _, rews, dones, infos = env.step(actions.detach())
        elif i == 100:
            print('Start running...')
            actions = policy(obs.detach())
            obs, _, rews, dones, infos = env.step(actions.detach())
        elif i > 100:
            actions = policy(obs.detach())
            obs, _, rews, dones, infos = env.step(actions.detach())

    #     replay_buffer.add_sample(ang_vel=obs[0, 45:45 + 3].detach().cpu().numpy(),
    #                              gravity_orientation=obs[0, 45 + 3:45 + 6].detach().cpu().numpy(),
    #                              dof_pos=obs[0, 45 + 6:45 + 6 + 12].detach().cpu().numpy(),
    #                              dof_vel=obs[0, 45 + 6 + 12:45 + 6 + 12 + 12].detach().cpu().numpy(),
    #                              actions=actions[0, :].detach().cpu().numpy()
    #                              )
    # replay_buffer.plot_ang_vel()
    # replay_buffer.plot_gravity()
    # replay_buffer.plot_dof_pos()
    # replay_buffer.plot_dof_vel()
    # replay_buffer.plot_actions()
    #











if __name__ == '__main__':
    EXPORT_POLICY = True
    RECORD_FRAMES = False
    MOVE_CAMERA = False
    args = get_args()
    args.task = 'go2'
    play(args)