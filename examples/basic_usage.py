import os
from tron_api_safe.core.client import TronAPIClient

def main():
    # 初始化客户端（建议从环境变量获取API Key）
    api_key = os.getenv('TRON_API_KEY', '')
    client = TronAPIClient(api_key=api_key)
    
    try:
        # 测试网络连接
        network_info = client.get_network_info()
        print("网络信息:", network_info)
        
        # 获取最新区块
        latest_block = client.get_current_block()
        print("最新区块:", latest_block)
        
        # 查询账户信息（示例地址）
        sample_address = "TYukBQZ2XXCcRCReAUg3E6VtgSQA7TZfmn"
        account_info = client.get_account_info(sample_address)
        print("账户信息:", account_info)
        
    except Exception as e:
        print(f"操作失败: {e}")

if __name__ == "__main__":
    main()
