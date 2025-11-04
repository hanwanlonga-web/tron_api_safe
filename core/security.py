import hashlib
import hmac
import os
from typing import Optional
import re

class SecurityManager:
    def __init__(self):
        self.sanitized_patterns = [
            r'[<>"\']',  # HTML标签和引号
            r'eval\(',   # eval函数
            r'exec\(',   # exec函数
            r'__.*__',   # 双下划线属性
        ]
    
    def validate_address(self, address: str) -> bool:
        """验证波场地址格式"""
        if not address or len(address) != 34:
            return False
        return address.startswith('T') and all(c in '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' for c in address)
    
    def sanitize_input(self, input_str: str) -> str:
        """输入净化"""
        if not isinstance(input_str, str):
            raise SecurityException("输入必须是字符串类型")
        
        for pattern in self.sanitized_patterns:
            input_str = re.sub(pattern, '', input_str)
        
        return input_str.strip()
    
    def safe_private_key_handling(self, private_key: str) -> str:
        """安全处理私钥（实际使用中应该使用硬件安全模块）"""
        if len(private_key) != 64:
            raise SecurityException("私钥格式不正确")
        return private_key
