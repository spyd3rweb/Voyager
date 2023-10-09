from voyager import Voyager
import os

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
# azure_login = {
#     "client_id": "YOUR_CLIENT_ID",
#     "redirect_url": "https://127.0.0.1/auth-response",
#     "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
#     "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
# }
mc_host=os.getenv("MC_HOST","127.0.0.1")
mc_port=int(os.getenv("MC_PORT","25565"))
openai_api_key = os.getenv("OPENAI_API_KEY","sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
openai_api_base = os.getenv("OPENAI_API_BASE", default="https://api.openai.com/v1")
skill_library_dir = os.getenv("SKILL_LIBRARY_DIR", default="/data/skill_library/trial1")
ckpt_dir = os.getenv("YOUR_CKPT_DIR", default="/data/ckpt/trial1")
task = os.getenv("YOUR_TASK", default="Craft a diamond pickaxe")

# Run Voyager for a specific task with a learned skill library
# First instantiate Voyager with skill_library_dir.
voyager = Voyager(
    #azure_login=None, # azure_login,
    mc_host=mc_host,
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    skill_library_dir=skill_library_dir, # Load a learned skill library.
    ckpt_dir=ckpt_dir, # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
    resume=False, # Do not resume from a skill library because this is not learning.
)


# Run task decomposition
sub_goals = voyager.decompose_task(task=task)

# voyager.inference(sub_goals=sub_goals)
voyager.inference(sub_goals=sub_goals)