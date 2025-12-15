# Netlify 部署指南

## 🎯 问题解决

### 问题：numpy 安装失败

**原因**：Netlify 构建镜像可能使用 Python 3.12，而 numpy 1.24.3 没有为 Python 3.12 提供预构建的轮子，导致需要从源代码编译，但 Netlify 没有编译工具。

**解决方案**：
1. ✅ 使用 Python 3.11（有预构建的 numpy 轮子）
2. ✅ 更新 requirements.txt 使用兼容的版本范围
3. ✅ 创建 `runtime.txt` 指定 Python 版本
4. ✅ 创建 `netlify.toml` 配置文件

## 📋 部署步骤

### 方法一：通过 GitHub 自动部署（推荐）

#### 1. 确保代码已推送到 GitHub

```bash
cd E:\testtool_1\MicTester_v2.10_Web
git add .
git commit -m "Add Netlify deployment configuration"
git push
```

#### 2. 在 Netlify 上创建新站点

1. 登录 [Netlify](https://app.netlify.com)
2. 点击 "Add new site" → "Import an existing project"
3. 选择 "GitHub" 并授权
4. 选择你的仓库：`MicTester_v2.10_Web`
5. 配置构建设置：
   - **Build command**: `pip install -r requirements.txt`
   - **Publish directory**: `.` (或留空)
   - **Functions directory**: `netlify/functions`

#### 3. 设置环境变量（可选）

在 Netlify 站点设置 → Environment variables 中添加：
- `PYTHON_VERSION`: `3.11`

#### 4. 部署

点击 "Deploy site"，Netlify 会自动：
1. 检测到 `runtime.txt` 并使用 Python 3.11
2. 安装 requirements.txt 中的依赖
3. 部署应用

### 方法二：手动部署

#### 1. 安装 Netlify CLI

```bash
npm install -g netlify-cli
```

#### 2. 登录 Netlify

```bash
netlify login
```

#### 3. 初始化站点

```bash
cd E:\testtool_1\MicTester_v2.10_Web
netlify init
```

#### 4. 部署

```bash
netlify deploy --prod
```

## ⚙️ 配置文件说明

### runtime.txt
```
python-3.11.7
```
指定使用 Python 3.11.7（有预构建的 numpy 轮子）

### netlify.toml
```toml
[build]
  command = "pip install -r requirements.txt"
  functions = "netlify/functions"
  publish = "."

[build.environment]
  PYTHON_VERSION = "3.11"
```

### requirements.txt
已更新为使用版本范围，确保兼容性：
- `numpy>=1.24.0,<1.26.0` - 兼容 Python 3.11
- 添加了 `serverless-wsgi` 用于 Netlify Functions

## 🔧 重要说明

### Netlify Functions 限制

Netlify 主要支持静态网站和 Serverless Functions。对于 Flask 应用：

1. **推荐方案**：使用 Netlify Functions 包装 Flask 应用
   - 已创建 `netlify/functions/api.py`
   - 使用 `serverless-wsgi` 包装 Flask 应用

2. **API 路由**：
   - 所有 `/api/*` 请求会被重定向到 `/.netlify/functions/api`
   - 前端需要更新 API 调用路径

### 前端 API 调用更新

如果使用 Netlify Functions，需要更新 `static/app.js` 中的 API 调用：

```javascript
// 原来的调用
fetch('/api/config')

// Netlify Functions 调用
fetch('/.netlify/functions/api/api/config')
```

或者使用环境变量：

```javascript
const API_BASE = window.location.hostname === 'localhost' 
  ? '' 
  : '/.netlify/functions/api';

fetch(`${API_BASE}/api/config`)
```

## 🚨 替代方案

如果 Netlify Functions 方案太复杂，可以考虑：

### 方案 A：使用 Render（推荐用于 Flask）

1. 注册 [Render](https://render.com)
2. 连接 GitHub 仓库
3. 选择 "Web Service"
4. 设置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment: Python 3.11

### 方案 B：使用 Railway

1. 注册 [Railway](https://railway.app)
2. 从 GitHub 部署
3. 自动检测 Flask 应用

### 方案 C：使用 Heroku

1. 注册 [Heroku](https://heroku.com)
2. 使用 Heroku CLI 部署
3. 添加 `Procfile`: `web: python app.py`

## 📝 部署检查清单

- [x] `runtime.txt` 指定 Python 3.11
- [x] `netlify.toml` 配置文件已创建
- [x] `requirements.txt` 使用兼容版本
- [x] `netlify/functions/api.py` 已创建
- [ ] 前端 API 路径已更新（如果使用 Functions）
- [ ] 环境变量已设置（如果需要）
- [ ] 测试部署是否成功

## 🔍 故障排查

### 问题：numpy 仍然安装失败

**解决**：
1. 检查 `runtime.txt` 是否指定 Python 3.11
2. 在 Netlify 构建日志中查看实际使用的 Python 版本
3. 尝试更新 numpy 版本：`numpy>=1.24.0,<1.26.0`

### 问题：API 请求 404

**解决**：
1. 检查 `netlify.toml` 中的 redirects 配置
2. 确认 `netlify/functions/api.py` 存在
3. 查看 Netlify Functions 日志

### 问题：静态文件无法加载

**解决**：
1. 确保 `static/` 和 `templates/` 目录在仓库中
2. 检查 `netlify.toml` 的 publish 设置

## 📚 参考资源

- [Netlify Python Functions](https://docs.netlify.com/functions/overview/)
- [serverless-wsgi](https://github.com/Miserlou/serverless-wsgi)
- [Netlify Build Configuration](https://docs.netlify.com/configure-builds/file-based-configuration/)

