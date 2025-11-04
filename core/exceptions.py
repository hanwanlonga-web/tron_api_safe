class TronAPIException(Exception):
    """基础异常类"""
    pass

class SecurityException(TronAPIException):
    """安全相关异常"""
    pass

class NetworkException(TronAPIException):
    """网络请求异常"""
    pass
