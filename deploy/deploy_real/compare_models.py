import torch
import time

def compare_model_cpu():
    policy = torch.jit.load('/home/unitree/code/unitree_rl_gym_0528/deploy/pre_train/go2/motion.pt')

    obs = torch.ones((1,45))
    for _ in range(100):
        _ = policy(obs)
    print('Network has been warmed up.')

    obs_1 = torch.ones((1,45))

    start = time.perf_counter()
    for _ in range(100):
        action_1 = policy(obs_1)
    end = time.perf_counter()
    avg_time = (end - start) * 1000 / 100
    print(f"Corrected CPU Inference time:{avg_time:.3f} ms")

def compare_model_gpu():
    policy = torch.jit.load('/home/unitree/code/unitree_rl_gym_0528/deploy/pre_train/go2/motion.pt').to('cuda:0')

    obs = torch.ones((1,45)).to('cuda:0')
    for _ in range(100):
        _ = policy(obs)
    torch.cuda.synchronize()
    print('Network has been warmed up.')

    obs_1 = torch.ones((1, 45)).to('cuda:0')
    torch.cuda.synchronize()
    start = time.perf_counter()
    for _ in range(100):
        action_1 = policy(obs_1)
    torch.cuda.synchronize()
    end = time.perf_counter()
    avg_time = (end - start) * 1000 / 100
    print(f"Corrected GPU Inference time:{avg_time:.3f} ms")


compare_model_cpu() # PC: 0.328ms, Laptop: 0.338ms
compare_model_gpu() # PC: 0.034ms, Laptop: 0.058ms

'''
THE RESULTS OF PC:
The action_1 is: tensor([[ 36.6393,   1.7832, -68.3584, -28.8572, -21.8910, -97.2222,  24.6654,
           5.0617, -47.2452, -21.3659,  -1.2255, -50.7423]],
       grad_fn=<AddmmBackward0>)
The action_2 is: tensor([[-0.1841, -0.9892,  1.3843, -0.1827, -0.6742,  1.0593,  0.3288, -0.0868,
          1.1183,  0.1400, -0.0097,  1.2969]], grad_fn=<AddmmBackward0>)

'''