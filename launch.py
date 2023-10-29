from voyager import Voyager
 
# You can also use mc_port instead of azure_login, but azure_login is highly recommended
# Change this to the port used when opening to LAN
mc_port = ...

openai_api_key = 'YOUR_API_KEY'

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
)

# for resuming from a checkpoint
# voyager = Voyager(
#     mc_port=mc_port,
#     openai_api_key=openai_api_key,
#     ckpt_dir="ckpt",
#     resume=True,
# )


# save output to file
import sys
f = open("logs/console.out", 'w')
sys.stdout = f

# start lifelong learning
voyager.learn()