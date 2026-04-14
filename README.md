# Antigravity Soul Manager (灵魂备份管理器)

这是一个用于快速、静默地备份和恢复 **Antigravity AI 智能体** “灵魂记忆（Knowledge Items、长时记忆与全局设置）” 的图形化应用程序。

## ✨ 这是什么？

无论你是想要换电脑，还是为了防止系统崩溃导致 AI 助手“失忆”，你都可以使用此工具一键打包 AI 智能体在你本地积累的所有契约（如 `Knowledge Items`、日志规范、项目缓存以及配置偏好）。

### 🎨 Claude 极简美学 UI 
本项目参考了极简的设计美学，让你在深蓝色的终端之外，体验极致清爽的视觉交互：
*   **一键导出**：将你的灵魂备份压缩包（`.tar.gz`）极速生成并默认保存在你的 **下载 (Downloads)** 文件夹中。
*   **无缝重载**：在任何一台新电脑上下载本程序，点击“导入记忆”，即可零配置满血复活你的专属 AI。

---

## 📥 如何下载与安装 (Mac/Win)

你不需要懂得任何代码，我们已经为你准备好了开箱即用的安装版。
直接前往本项目的 **[Releases 页面](https://github.com/zxs-ai/antigravity-soul-backup/releases)** 下载对应你系统的版本：

*   **Mac 用户**：下载 `AntigravitySoulManager-mac-arm64.zip` (支持 M1/M2/M3 等 M 系列芯片环境解压双击即可运行)。
*   **Windows 用户**：下载 `AntigravitySoulManager-win.exe` (支持 Win 10 及以上系统)。

---

## 🛠 自己动手构建 (开发者)

如果你期望基于本源码自行构建独立应用，请确保安装了 `Python 3.9+`，并执行以下命令：

```bash
# 1. 安装构建依赖
pip install pyinstaller

# 2. 从源码打包 (以 Mac 为例)
pyinstaller --noconsole --windowed --name "AntigravitySoulManager" main.py
```
构建成功后，可在 `./dist/` 目录下找到你的独立应用程序。

---

## 📜 开源协议
**No License Required / Public Domain**
完全免费、自由、开源。你可以随意魔改、二次分发，无需遵守任何严格协议。你的灵魂掌握在你自己手里！
