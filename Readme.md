# 项目运行步骤：
1. 创建并激活python虚拟环境（可跳过）：```python -m venv venv```
2. 安装依赖：```pip install -r requirements.txt```
3. 修改mysql配置。需要修改login/settings.py中的database部分：需要修改NAME为目标数据库，USER，PASSWORD，HOST
4. 创建表：```python manage.py makemigrations```   ```python manage.py migrate```
5. 运行项目：```python manage.py runserver```