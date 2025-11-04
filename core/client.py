import requests
import json
from typing import Dict, Any, Optional
from .security import SecurityManager
from .exceptions import SecurityException, NetworkException

class TronAPIClient:
    """
    安全的波场API客户端
    """
    
    def __init__(self, 
                 api_key: Optional[str] = None,
                 base_url: str = "https://api.trongrid.io",
                 timeout: int = 30):
        
        self.security = SecurityManager()
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'SafeTronAPI/1.0'
        }
        
        if api_key:
            self.headers['TRON-PRO-API-KEY'] = api_key
    
    def _safe_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """安全请求封装"""
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            
            # 净化输入参数
            if 'params' in kwargs:
                kwargs['params'] = {
                    k: self.security.sanitize_input(str(v)) 
                    for k, v in kwargs['params'].items()
                }
            
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise NetworkException(f"网络请求失败: {str(e)}")
        except json.JSONDecodeError as e:
            raise NetworkException(f"JSON解析失败: {str(e)}")
    
    def get_account_info(self, address: str) -> Dict[str, Any]:
        """获取账户信息"""
        if not self.security.validate_address(address):
            raise SecurityException("无效的波场地址")
        
        endpoint = f"v1/accounts/{address}"
        return self._safe_request('GET', endpoint)
    
    def get_transaction_info(self, tx_id: str) -> Dict[str, Any]:
        """获取交易信息"""
        endpoint = f"v1/transactions/{tx_id}"
        return self._safe_request('GET', endpoint)
    
    def get_current_block(self) -> Dict[str, Any]:
        """获取最新区块"""
        endpoint = "v1/blocks/latest"
        return self._safe_request('GET', endpoint)
    
    def get_network_info(self) -> Dict[str, Any]:
        """获取网络信息"""
        endpoint = "v1/networks"
        return self._safe_request('GET', endpoint)
    
    def validate_contract(self, contract_address: str) -> Dict[str, Any]:
        """验证合约地址"""
        if not self.security.validate_address(contract_address):
            raise SecurityException("无效的合约地址")
        
        endpoint = f"v1/contracts/{contract_address}"
        return self._safe_request('GET', endpoint)
