# GitHub 上传指南

## 📋 为什么会有这么多文件？

你看到的文件包括：

1. **源代码文件**（需要上传）：
   - `app.py` - Flask 后端服务器
   - `templates/` - HTML 模板
   - `static/` - CSS 和 JavaScript 文件
   - `config.json` - 配置文件
   - `requirements.txt` - 依赖列表
   - `README.md` - 说明文档

2. **Git 仓库文件**（不需要上传，已自动忽略）：
   - `.git/` - Git 仓库元数据（本地使用）

3. **会被忽略的文件**（通过 .gitignore）：
   - `test_results/` - 测试结果（用户生成的文件）
   - `__pycache__/` - Python 缓存文件
   - `*.xlsx` - Excel 报告文件
   - 其他临时文件

## 🚀 上传到 GitHub 的步骤

### 方法一：使用命令行（推荐）

#### 1. 在 GitHub 上创建新仓库

1. 登录 GitHub (https://github.com)
2. 点击右上角的 "+" → "New repository"
3. 填写仓库信息：
   - Repository name: `MicTester_v2.10_Web`（或你喜欢的名字）
   - Description: `麦克风批量测试工具 - Web版本`
   - 选择 Public 或 Private
   - **不要**勾选 "Initialize this repository with a README"（因为我们已经有了）
4. 点击 "Create repository"

#### 2. 在本地执行以下命令

```bash
# 进入项目目录
cd E:\testtool_1\MicTester_v2.10_Web

# 添加所有文件到暂存区（.gitignore 会自动排除不需要的文件）
git add .

# 提交更改
git commit -m "Initial commit: 麦克风测试工具 Web版本 v2.10"

# 添加远程仓库（将 YOUR_USERNAME 替换为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/MicTester_v2.10_Web.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

#### 3. 如果遇到认证问题

如果提示需要输入用户名和密码，可以使用以下方法：

**方法 A：使用 Personal Access Token（推荐）**

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成后复制 token
5. 推送时，用户名输入你的 GitHub 用户名，密码输入 token

**方法 B：使用 SSH（更安全）**

```bash
# 生成 SSH 密钥（如果还没有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 复制公钥内容
cat ~/.ssh/id_ed25519.pub

# 在 GitHub → Settings → SSH and GPG keys → New SSH key 中添加

# 使用 SSH URL 添加远程仓库
git remote set-url origin git@github.com:YOUR_USERNAME/MicTester_v2.10_Web.git
```

### 方法二：使用 GitHub Desktop（图形界面）

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 打开 GitHub Desktop
3. File → Add Local Repository
4. 选择 `E:\testtool_1\MicTester_v2.10_Web`
5. 点击 "Publish repository"
6. 填写仓库信息并发布

## 📝 后续更新代码

如果以后修改了代码，需要更新到 GitHub：

```bash
# 查看更改
git status

# 添加更改的文件
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到 GitHub
git push
```

## ⚠️ 注意事项

1. **config.json 是否上传？**
   - 如果配置文件包含敏感信息，建议不上传
   - 可以在 `.gitignore` 中添加 `config.json`
   - 或者创建一个 `config.json.example` 作为模板

2. **test_results 目录**
   - 已自动忽略，不会上传测试结果文件
   - 这些是用户生成的文件，不需要版本控制

3. **Python 缓存文件**
   - `__pycache__/` 已自动忽略
   - 这些是 Python 自动生成的，不需要上传

## 🔍 检查哪些文件会被上传

在提交前，可以查看哪些文件会被上传：

```bash
git status
```

绿色显示的文件会被上传，红色显示的文件会被忽略（根据 .gitignore）。

## 📦 推荐的文件结构

上传后，GitHub 仓库应该包含：

```
MicTester_v2.10_Web/
├── .gitignore              # Git 忽略规则
├── app.py                  # Flask 后端
├── config.json             # 配置文件（可选）
├── requirements.txt        # Python 依赖
├── README.md               # 说明文档
├── 使用说明.txt            # 中文使用说明
├── 启动服务器.bat          # 启动脚本
├── 安装依赖.bat            # 安装脚本
├── templates/
│   └── index.html          # 前端页面
└── static/
    ├── app.js              # 前端逻辑
    └── style.css           # 样式文件
```

## 🎯 快速命令总结

```bash
# 初始化（已完成）
git init

# 添加文件
git add .

# 提交
git commit -m "Initial commit"

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 推送
git push -u origin main
```

---

**提示**：如果遇到任何问题，可以查看 GitHub 的帮助文档或使用 `git help` 命令。

