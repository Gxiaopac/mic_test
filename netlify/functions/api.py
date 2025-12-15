"""
Netlify Serverless Function for Flask API
将 Flask 应用包装为 Netlify Function
"""
import sys
import os
import json

# 添加项目根目录到路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, project_root)

# 设置工作目录
os.chdir(project_root)

try:
    from serverless_wsgi import handle_request
    from app import app
    
    def handler(event, context):
        """Netlify Function 处理函数"""
        # Netlify 会将 /api/* 重定向到 /.netlify/functions/api/api/*
        # 需要移除多余的 /api 前缀
        path = event.get('path', '')
        if path.startswith('/api/api/'):
            event['path'] = path.replace('/api/api/', '/api/', 1)
        elif path.startswith('/.netlify/functions/api/api/'):
            event['path'] = path.replace('/.netlify/functions/api/api/', '/api/', 1)
        
        return handle_request(app, event, context)
except ImportError as e:
    # 如果导入失败，返回错误信息
    def handler(event, context):
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': f'Import error: {str(e)}', 'message': 'Please ensure serverless-wsgi is installed'})
        }
