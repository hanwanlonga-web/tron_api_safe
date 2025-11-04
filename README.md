# 安装依赖
pip install requests pycryptodome base58 ecdsa

# 基本使用
from tron_api_safe import TronAPIClient

client = TronAPIClient()
account = client.get_account_info("TYukBQZ2XXCcRCReAUg3E6VtgSQA7TZfmn")
