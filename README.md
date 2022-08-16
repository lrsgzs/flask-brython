# flask-brython

### 因为这个库(flask-brython)，所以在使用brython时，更方便了。
### Because of this library (flask-brython), it is more convenient to use brython.

## 安装
## Install

```shell
$ pip install flask-brython
```

## 使用
## use

```python
...
from flask_brython import *
...
brython = Brython(app)
...
```

### 加载
### load

```html
...
{{ brython.load() }}
...
```

### 创建brython在线python代码运行器
### Create brython online python code runner

```html
...
{{ brython. create(code="print('helloworld')") }}
<!-- code参数是你要运行的代码 -->
<!-- The 'code' parameter is the code you want to run -->
...
```
