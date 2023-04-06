## 数据分析

本项目包括一个基于 Django 的 Web 应用，用于展示和分析温湿度传感器数据。通过访问 `http://localhost:8000/analysis/` 页面，您可以查看温湿度传感器数据的最大值、最小值和平均值。

### 安装

在运行该 Django 应用之前，请确保已经按照前面的说明完成了 Mosquitto 代理服务器和 Python 脚本的安装和配置。

然后，按照以下步骤来安装和配置 Django 应用：

1. 进入项目根目录。

2. 执行以下命令来安装必要的 Python 依赖项：

```pip install -r requirements.txt```

### 使用

在完成安装和配置之后，您可以通过以下步骤来运行 Django 应用：

1. 进入项目根目录。

2. 执行以下命令来启动 Django 开发服务器：

```python manage.py runserver```

3. 在 Web 浏览器中访问 `http://localhost:8000/analysis/` 页面，查看温湿度传感器数据的最大值、最小值和平均值。

### 注意事项

- 该 Django 应用使用 SQLite 数据库来存储温湿度传感器数据，请确保您已经正确配置了 Mosquitto 代理服务器和 Python 脚本，以确保数据正常地存储到 SQLite 数据库中。

- 该 Django 应用使用 Django 2.2 版本进行开发，如果您使用的是其他版本的 Django，可能需要进行适当的修改。
