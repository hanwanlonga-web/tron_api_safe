# 安装依赖
pip install requests pycryptodome base58 ecdsa

# 基本使用
from tron_api_safe import TronAPIClient

client = TronAPIClient()
account = client.get_account_info("TYukBQZ2XXCcRCReAUg3E6VtgSQA7TZfmn")


⚠️ 重要安全建议
私钥安全：永远不要在代码中硬编码私钥

环境变量：使用环境变量存储敏感信息

HTTPS Only：确保所有请求都使用HTTPS

定期更新：保持依赖库最新版本

代码审计：定期进行安全审计
