from synapseclient import Synapse
from synapseutils import syncFromSynapse
import os

# 初始化并登录 Synapse
syn = Synapse()
syn.login(authToken='Token from "https://accounts.synapse.org/authenticated/personalaccesstokens"')

# 要下载的 Synapse 文件夹 ID
folder_id = 'syn52540892'

# 本地保存目录
local_directory = "./synapse_download"

# 创建本地目录（如果不存在）
if not os.path.exists(local_directory):
    os.makedirs(local_directory)

# 递归下载文件夹内容
syncFromSynapse(syn, folder_id, path=local_directory)

print("✅ 所有文件已成功下载！")%           
