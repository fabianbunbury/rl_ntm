# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython


# %%
#IPython magic to reload libraries
get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

# Extra code so Juypter doesn't crash on mac os
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
sys.path.insert(0, "~/Desktop/neural_turing_machines/With_Zach\rl_ntm")


# %%
import sys
sys.path.insert(0, 'utils')  # noqa
import tensorflow
import tasks

import ntm
import interfaces


# %%
# Training Params
train_iter = 5
batch_size = 2

# Task Params
max_epsiode_length = 100


# %%
Task = tasks.Copy(string_len=5, max_char=5, max_step=100)
Controller = ntm.NTM()


# %%
#Define interfaces



# %%
memory_content = 0

for i in range(train_iter):
    
    # Collect experince using current policy/controller
    for j in range(batch_size):
        episode_steps = 0
        observation, reward, target, done, info = Task.reset()
        Task.render()

        while True:
            episode_steps += 1
            
            inputs = (observation, memory_content)
            
            Controller.input(inputs)
            outputs = Controller.output()
            
            input_control = outputs[0]  
            memory_control = outputs[1]
            memory_content = outputs[2]
            output_control = outputs[3]
            output_content = outputs[4]

            actions = (input_control, output_control, output_content)
            observation, reward, target, done, info = Task.step(actions)
            
            if done:
                done = False
                break
        

