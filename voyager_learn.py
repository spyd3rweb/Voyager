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
openai_api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
openai_api_base = os.getenv("OPENAI_API_BASE", default="https://api.openai.com/v1")
skill_library_dir = os.getenv("SKILL_LIBRARY_DIR", default="/data/skill_library/trial1")
ckpt_dir = os.getenv("YOUR_CKPT_DIR", default="/data/ckpt/trial1")
resume=(os.getenv("RESUME_SKILL_LIBRARY", default="False")).lower() == "true"

# Getting Started
voyager = Voyager(
    #azure_login=None, # azure_login,
    mc_host=mc_host,
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    ckpt_dir=ckpt_dir,
    resume=resume
)

# Resume from a checkpoint during learning
# voyager = Voyager(
#     azure_login=azure_login,
#     openai_api_key=openai_api_key,
#     ckpt_dir="YOUR_CKPT_DIR",
#     resume=True,
# )

# start lifelong learning
voyager.learn()