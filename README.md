# my-cli-tool

一个简洁的 Python 命令行工具示例，演示了标准的 CLI 项目结构：参数解析、版本号、可安装打包配置等。

## 功能

- 通过 `argparse` 解析命令行参数
- 支持 `--name` 自定义问候对象
- 支持 `--version` 查看版本
- 通过 `pyproject.toml` 配置可直接安装的命令入口

## 安装

```bash
pip install -e .
```

## 使用

```bash
# 默认问候
my-cli-tool
# Hello, World!

# 自定义问候对象
my-cli-tool --name Alice
# Hello, Alice!

# 查看版本
my-cli-tool --version
# my-cli-tool 0.1.0
```

## 项目结构

```
my-cli-tool/
├── my_cli_tool/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## 许可

[MIT](LICENSE)
