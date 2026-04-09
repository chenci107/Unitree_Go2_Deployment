import os

LEGGED_GYM_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print('The LEGGED_GYM_ROOT_DIR is:',LEGGED_GYM_ROOT_DIR)
LEGGED_GYM_ENVS_DIR = os.path.join(LEGGED_GYM_ROOT_DIR, 'legged_gym', 'envs')
print('The LEGGED_GYM_ENVS_DIR is:',LEGGED_GYM_ENVS_DIR)