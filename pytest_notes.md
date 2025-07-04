# 1.入门Pytest

## 1.1 什么是Pytest？

一个功能强大的 Python 测试框架，主要用于编写和运行自动化测试。它广泛应用于单元测试、集成测试等各种测试场景

## 1.2 Pytest和Unittest之间的联系与差异

| 对比项       | pytest                                                       | unittest                          | 联系/差异说明        |
| ------------ | ------------------------------------------------------------ | --------------------------------- | -------------------- |
| 所属         | 第三方库                                                     | Python 标准库                     | 都是 Python 测试框架 |
| 测试用例结构 | 基于函数，也支持类                                           | 基于类（需继承 TestCase）         | 结构不同             |
| 断言方式     | 直接使用 assert 语句                                         | 使用 self.assertEqual 等方法      | 断言语法不同         |
| 自动发现     | 支持（test_ 开头的函数/类/方法）                             | 支持（test 开头的方法）           | 都支持自动发现       |
| 参数化       | 支持（@pytest.mark.parametrize）                             | 不直接支持                        | pytest 更灵活        |
| 插件生态     | 丰富（如 pytest-cov、pytest-xdist 等）                       | 插件较少                          | pytest 扩展性更强    |
| 兼容性       | 可运行 unittest 测试用例                                     | 不能直接运行 pytest 用例          | pytest 兼容 unittest |
| 详细错误信息 | 支持（pytest用**ast抽象语法树**技术实现了**断言重写**，让测试报告更详细） | 错误信息较简略                    | pytest 更友好        |
| 运行方式     | 直接运行 pytest 命令                                         | 需调用 unittest.main() 或用命令行 | 运行方式不同         |
| 学习曲线     | 简单，易上手                                                 | 相对繁琐                          | pytest 更易用        |

## 1.3 常见测试类型

+ **单元测试**和**集成测试**关注代码和模块本身
+ **接口测试**专注于 API 层，测试系统对外或对内的 API 接口。
+ **系统测试**、**性能测试**、**安全测试**等则关注整个系统的整体表现和健壮性

## 1.4 测试结果详解

+ 执行环境：框架版本，项目根目录，用例数量
+ 执行过程：脚本名称，**用例结果**，执行进度
+ 失败详情：用力内容，断言提示
+ 整体摘要：结果情况，花费时间

## 1.5 用例结果缩写

| 缩写 | 全称    | 含义说明                              |
| ---- | ------- | ------------------------------------- |
| .    | Passed  | 测试用例通过                          |
| F    | Failed  | 测试用例失败                          |
| E    | Error   | 测试用例执行出错（fixture执行报错）   |
| x    | XFailed | 预期内的失败（被标记为 xfail 的用例） |
| X    | XPassed | 预期外的通过（xfail 但通过）          |
| s    | Skipped | 跳过的测试用例                        |
| p    | Passed  | 通过（有些插件或配置下显示）          |

# 2.进阶Pytest

## 2.1 用例规则

### 2.1.1 用例发现规则

>  测试框架在识别并加载测试用例的过程称之为用例发现

发现用例步骤：

+ 遍历所有的目录（` venv`虚拟环境目录和` .`开头的目录不会搜索）
+ 寻找其中以` test_`开头或者以` _test`结尾的python脚本（用例文件）
+ 遍历用例文件中所有以` Test`开头的类，并收集其中以` test_`开头的**方法**和其他以` test_`开头的**函数**

### 2.1.2 用例内容规则

+ 可调用（函数，方法，类或者对象）
+ 名字以` test_`开头
+ 没有参数（参数有其他含义）
+ 没有返回值（默认为None）

## 2.2 配置框架

### 2.2.1 什么是配置框架？

pytest 的配置框架是指 pytest 提供的一套机制，用于**集中管理和定制测试运行的行为**。

- 设置测试的查找规则
- 配置测试报告格式
- 定义测试用例的执行顺序
- 添加自定义参数、钩子函数等

### 2.2.2 常见的配置方式

+ 配置文件` pytest.ini`、` pyproject.toml`、` setup.cfg`、`conftest.py`等
+ 命令行参数`pytest -v --maxfail=2 --disable-warnings`

### 2.2.3 常用参数

| 参数                    | 作用说明                                                  | 示例                           |
| ----------------------- | --------------------------------------------------------- | ------------------------------ |
| `-v`                    | 显示详细信息（verbose 模式）                              | `pytest -v`                    |
| `-q`                    | 安静模式，只显示简要结果                                  | `pytest -q`                    |
| `-s`                    | 允许测试过程中输入内容和print输出                         | `pytest -s`                    |
| `-k "表达式"`           | 只运行名称匹配表达式的测试用例                            | `pytest -k "login"`            |
| `-m "标记名"`           | 只运行被指定 mark 标记的测试用例                          | `pytest -m "slow"`             |
| `--maxfail=N`           | 失败 N 次后停止测试                                       | `pytest --maxfail=2`           |
| `--tb=style`            | 设置 traceback（错误回溯）风格（auto/short/long/line/no） | `pytest --tb=short`            |
| `--disable-warnings`    | 禁用警告信息                                              | `pytest --disable-warnings`    |
| `--capture=method`      | 控制输出捕获方式（no/sys/stdout/stderr）                  | `pytest --capture=no`          |
| `--html=report.html`    | 生成 HTML 格式的测试报告（需安装 pytest-html 插件）       | `pytest --html=report.html`    |
| `--junitxml=report.xml` | 生成 JUnit XML 格式的测试报告                             | `pytest --junitxml=report.xml` |
| `--collect-only`        | 只收集测试用例，不执行                                    | `pytest --collect-only`        |
| `--lf`                  | 只运行上次失败的测试用例（last-failed）                   | `pytest --lf`                  |
| `--ff`                  | 先运行上次失败的用例，再运行其他用例（failed-first）      | `pytest --ff`                  |
| `-x`                    | 首次失败时立即停止测试                                    | `pytest -x`                    |
| `--durations=N`         | 显示执行最慢的 N 个测试用例                               | `pytest --durations=5`         |
| `-n NUM`                | 多进程并发执行测试（需安装 pytest-xdist 插件）            | `pytest -n 4`                  |

## 2.3 标记

### 2.3.1 什么是标记（mark）？

**mark（标记）** 是一种非常实用的机制，用于给测试用例（函数、类、模块）打上标签，从而实现**分组、过滤、定制行为**等功能。

- **分组测试用例**：比如把慢速用例、冒烟用例、接口用例分组。
- **条件执行**：比如只运行被某个 mark 标记的用例。
- **定制行为**：比如预期失败（xfail）、跳过（skip）等。

### 2.3.2 常见用法

+ 自定义标记

  ```python
  @pytest.mark.slow
  def test_big_data():
      ...
  
  @pytest.mark.api
  @pytest.mark.slow   #组合标记
  def test_login_api():
      ...
  ```

+ 运行指定标记的用例
  ```python
  pytest -m slow
  pytest -m "slow or api"
  ```


### 2.3.3 常见内置标记

| 标记名                      | 作用说明         |
| --------------------------- | ---------------- |
| `@pytest.mark.skip`         | 跳过该测试用例   |
| `@pytest.mark.skipif`       | 条件成立时跳过   |
| `@pytest.mark.xfail`        | 预期该用例会失败 |
| `@pytest.mark.parametrize`  | 参数化测试用例   |
| `@pytest.mark.userfixtures` | 使用夹具fixtures |

```python
@pytest.mark.skip(reason="暂时不测")
def test_temp():
    ...
@pytest.mark.xfail(reason="已知bug")
def test_bug():
    ...
```

### 2.3.4 注册自定义标记（避免警告）

为避免警告，建议在 `pytest.ini` 中注册自定义标记：

```ini
[pytest]
markers =
    slow: 标记慢速用例
    api: 标记接口用例
```

## 2.4 数据驱动测试

> 数据驱动测试=参数化测试+数据文件

怎么理解这句话？

参数化测试就是对于同一个测试用例传入不同的参数来验证其在不同输入下的行为，加上数据文件就等于数据驱动测试的意思就是参数化测试中的参数从数据文件中读取，因此数据文件决定了测试用例执行的次数和每次执行时传入的参数

```python
import pytest
import requests

# 参数化测试登录接口
@pytest.mark.parametrize("username, password, expected_code", [
    ("admin", "123456", 200),    # 正确账号
    ("test", "wrong_pwd", 401),  # 错误密码
    ("", "", 400),               # 空账号密码
])
def test_login(username, password, expected_code):
    url = "https://api.example.com/login"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    assert response.status_code == expected_code
```

## 2.5 夹具fixtures

**夹具**（fixture）是一种用于在测试函数执行前准备测试环境、在测试后进行清理的机制。夹具可以用来提供测试所需的数据、对象、资源（如数据库连接、临时文件等），从而让测试代码更加简洁、可复用和易于维护。

### 2.5.1 夹具的定义和使用

```python
@pytest.fixture
def log_fixture():
	print(datetime.now(), '测试开始')
    yield
    print(datetime.now(), '测试结束')
# 两种使用夹具的方法 
def test_1(log_fixture):
    pass

@pytest.mark.usefixtures('f')
def test_2():
    pass
```

### 2.5.2 高级特性

+ 自动使用：不需要在测试函数中显式声明夹具名，pytest 会自动为夹具作用域内的测试用例应用该夹具。

```python
import pytest

@pytest.fixture(autouse=True)
def auto_setup():
    print("自动执行夹具")
```

+ 夹具依赖：夹具可以依赖其他夹具，只需在参数列表中声明即可，pytest 会自动解析依赖关系并注入。

```python
@pytest.fixture
def db():
    return "数据库连接"

@pytest.fixture
def user(db):
    return f"使用{db}创建的用户"

def test_user(user):
    assert "数据库连接" in user
```

+ 返回内容：夹具的返回值会被传递给使用它的测试函数或其他夹具。
  + 使用yield返回值时会分离前后置操作，使用return返回值时就是简单的前置夹具

```python
@pytest.fixture
def data():
    print('123')
    yield 123
    print('456')

def test_sum(data):
    assert data == 456
```

+ 范围共享：夹具可以通过 `scope` 参数控制其生命周期和共享范围（注意全局共享夹具不能放到测试用例脚本中，应该放在conftests.py中），范围内部的所有测试用例还能**共享参数**
  + `function`（默认）：每个测试函数都会调用一次夹具。
  + `class`：每个测试类调用一次。
  + `module`：每个模块调用一次。
  + `session`：整个测试会话只调用一次。

## 2.6 钩子

> 在 pytest 中，**hook**（钩子）是一种插件机制，在conftest.py配置文件中自定义，允许你在 pytest 的测试执行流程中**插入自定义代码**，以实现对测试运行过程的深度定制和扩展。

### 2.6.1 pytest定义好的常见钩子

| 钩子函数名                    | 作用/时机      |
| ----------------------------- | -------------- |
| pytest_configure              | 初始化配置时   |
| pytest_collection_modifyitems | 用例收集后     |
| pytest_runtest_setup          | 每个用例执行前 |
| pytest_runtest_call           | 每个用例执行时 |
| pytest_runtest_teardown       | 每个用例执行后 |
| pytest_terminal_summary       | 测试报告输出时 |

### 2.6.2 示例

````python
# conftest.py

def pytest_runtest_setup(item):
    print(f"\n[setup] 开始执行用例: {item.name}")

def pytest_runtest_teardown(item):
    print(f"\n[teardown] 结束执行用例: {item.name}")
````

## 2.7 插件管理

> **pytest 插件**是对 pytest 功能的扩展，可以添加、修改或增强 pytest 的行为。

### 2.7.1 插件的启动和禁用

+ 启用：` -p plugin`
+ 金庸: ` -p no:plugin`

### 2.7.2 插件的使用方法

+ 命令行参数：运行 pytest 时直接通过命令行传递这些参数来启用或配置插件功能。

  ```python
  pytest --html=report.html
  pytest --cov=my_package tests/
  ```

+ 配置文件

  ```ini
  # pytest.ini
  [pytest]
  addopts = --cov=my_package --html=report.html
  markers =
      slow: 标记慢测试
      smoke: 标记冒烟测试
  ```

+ 夹具：许多插件会提供自定义夹具，供测试用例直接使用。只需在测试函数参数中声明夹具名，pytest 会自动注入。

  ```python
  def test_example(mocker):
      mock_obj = mocker.Mock()
      mock_obj.method.return_value = 123
      assert mock_obj.method() == 123
  ```

+ mark：插件可以定义自定义的 mark（标记），用于标记测试用例，实现分组、过滤、特殊处理等功能。

  ```python
  import pytest
  
  @pytest.mark.slow
  def test_slow_case():
      ...
  
  @pytest.mark.smoke
  def test_smoke_case():
      ...
  ```

### 2.7.3 常见插件

+ pytest-html：**生成**html格式的测试报告

```python
--html=./reports/my_report.html #自定义报告文件位置
--self-contained-html #合并多个测试报告
```

+ pytest-xdist：**并行**和**分布式**运行测试用例，大幅提升测试执行效率

> 适用于任务本身耗时较长，超过进程调度成本很多时才能提升效率
>
> 在测试用例间存在资源竞争或者顺序依赖时不能使用分布式测试

```python
pytest -n auto #指定参与分布式测试的python worker数量，auto则是自动检测
```

+ pytest-rerunfailures：用于**自动重跑失败的测试用例**，以提升测试的稳定性，尤其适合处理偶发性失败（如网络波动、环境抖动等）导致的测试不通过。

  ```python
  pytest --reruns 3 #指定失败用例最多重跑的次数,即最多执行 4 次：1 次原始 + 3 次重跑
  pytest --reruns 3 --reruns-delay 3 #指定每次重跑之间延迟3秒
  ```

+ pytest-result-log：用于将测试执行过程和结果以**结构化 JSON 格式**记录下来，便于自动化处理和分析。

  ```python
  pytest --report-log=results.json #自定义报告文件位置
  ```

## 2.8 Allure测试报告框架

> **Allure是一个开源的、灵活的测试报告框架**，用于生成漂亮、交互式的测试报告

+ 配置

  ```python
  --alluredir=allure-results --clean-alluredir
  ```

+ 生成报告并查看

  ```python
  allure generate allure-results -o allure-report --clean
  allure open allure-report
  ```

+ 重要装饰器

  | 装饰器                | 作用说明                    | 典型用途                  |
  | --------------------- | --------------------------- | ------------------------- |
  | `@allure.epic`        | 史诗级需求（最高分组）      | 大型项目/模块分组（可选） |
  | `@allure.feature`     | 功能模块（一级分组）        | 主要功能模块分组          |
  | `@allure.story`       | 子功能/业务场景（二级分组） | 具体业务流程、用例分组    |
  | `@allure.title`       | 用例标题                    | 让报告更易读，覆盖函数名  |
  | `@allure.severity`    | 用例严重级别                | 标记优先级，便于筛选      |
  | `@allure.step`        | 步骤描述                    | 详细还原用例执行过程      |
  | `@allure.description` | 用例详细描述                | 说明用例背景、前置条件等  |

  + 前五个装饰器主要用于生成有层级结构的报告方便筛选和搜索

  + step装饰器用于**详细还原测试用例的执行过程**，让报告中每一步操作都清晰可见，便于问题定位和复现。

  + description装饰器用于描述用例的细节，类似于注释

    ```python
    import allure
    
    # 1. epic：最高级别分组，适合大型项目或系统模块
    @allure.epic("用户中心")
    
    # 2. feature：功能模块分组
    @allure.feature("登录功能")
    
    # 3. story：具体业务场景或用例分组
    @allure.story("手机号登录")
    
    # 4. title：自定义用例标题，报告中显示更友好
    @allure.title("手机号登录成功-正常流程")
    
    # 5. severity：用例严重级别，便于筛选和关注重点用例
    @allure.severity(allure.severity_level.CRITICAL)
    
    # 6. description：用例详细说明，支持多行文本和HTML
    @allure.description("""
    <b>前置条件：</b>用户已注册并激活<br>
    <b>测试步骤：</b>
    1. 打开登录页面<br>
    2. 输入正确的手机号和密码<br>
    3. 点击登录按钮<br>
    <b>预期结果：</b>登录成功，跳转到首页
    """)
    def test_login_by_phone_success():
        # 7. step：详细记录用例执行过程，每一步都可见
        with allure.step("打开登录页面"):
            # 这里可以写打开页面的代码
            pass
    
        with allure.step("输入手机号和密码"):
            # 这里可以写输入手机号和密码的代码
            phone = "13800000000"
            password = "correct_password"
            # 假设输入操作
            pass
    
        with allure.step("点击登录按钮"):
            # 这里可以写点击登录按钮的代码
            pass
    
        with allure.step("断言登录成功"):
            # 这里可以写断言逻辑
            assert True  # 假设登录成功
    
    ```

# 3.测试框架的封装

> **测试框架的封装**，指的是在自动化测试项目中，将**通用、重复、底层**的代码抽象出来，形成统一的模块或类，供测试用例调用。可以提升复用性、可维护性、开发效率和团队协作能力，是自动化测试项目规范化、规模化的基础。

## 3.1 YAML文件的基本语法

> YAML（YAML Ain’t Markup Language）是一种专为数据表达设计的文本格式，常用于配置文件、数据驱动测试等场景。它**完全兼容JSON**且比 JSON、XML 更直观，层级结构清晰，非常适合人类阅读和编辑。

```yaml
# 字符串
name: "张三"

# 数字
age: 28

# 布尔值
is_admin: true

# 空值
nickname: null

# 列表（数组）
hobbies:
  - 篮球
  - 阅读
  - 编程

# 字典（对象）
address:
  city: 北京
  district: 海淀区
  zipcode: 100080

# 嵌套结构：字典中包含列表
education:
  schools:
    - name: 清华大学
      degree: 本科
      year: 2017
    - name: 北京大学
      degree: 硕士
      year: 2020

# 列表中包含字典
projects:
  - title: "自动化测试平台"
    language: Python
    stars: 120
  - title: "个人博客"
    language: JavaScript
    stars: 80

# 多行字符串（保留换行）
bio: |
  张三是一名软件测试工程师，
  擅长接口测试和自动化测试开发。
  爱好编程和技术分享。

# 多行字符串（折叠成一行）
summary: >
  这是一个折叠的多行字符串，
  换行会被空格替代，
  适合写简短的描述信息。
```

## 3.2 接口测试用例设计

### 3.2.1 用例内容

> 名字+标记+输出参数+预期结果+步骤

| 用例名称 | 标记      | 步骤                                      | 输入参数                      | 预期结果             |
| -------- | --------- | ----------------------------------------- | ----------------------------- | -------------------- |
| 登录成功 | login, P0 | 1. 调用登录接口，输入正确用户名和密码     | username=tom, password=123456 | code=0, msg=success  |
| 密码错误 | login, P1 | 1. 调用登录接口，输入正确用户名和错误密码 | username=tom, password=wrong  | code=1, msg=密码错误 |
| 缺少参数 | login, P2 | 1. 调用登录接口，不传密码                 | username=tom                  | code=2, msg=参数缺失 |

### 3.2.2 YAML表示用例

## 3.3 Asserpy第三方断言包

> assertpy 支持链式调用，提升可读性
>
> assert_that('hello world').is_not_empty().starts_with('he').ends_with('ld').contains('lo')

+ 基本断言

| 方法                   | 说明      | 示例                              |
| ---------------------- | --------- | --------------------------------- |
| is_equal_to(value)     | 等于      | assert_that(5).is_equal_to(5)     |
| is_not_equal_to(value) | 不等于    | assert_that(5).is_not_equal_to(6) |
| is_true()              | 为 True   | assert_that(True).is_true()       |
| is_false()             | 为 False  | assert_that(False).is_false()     |
| is_none()              | 为 None   | assert_that(None).is_none()       |
| is_not_none()          | 不为 None | assert_that(1).is_not_none()      |

+ 数值断言

| 方法                   | 说明          | 示例                               |
| ---------------------- | ------------- | ---------------------------------- |
| is_greater_than(value) | 大于          | assert_that(10).is_greater_than(5) |
| is_less_than(value)    | 小于          | assert_that(5).is_less_than(10)    |
| is_between(a, b)       | 在区间 [a, b] | assert_that(5).is_between(1, 10)   |

+ 字符串断言

| 方法                  | 说明       | 示例                                       |
| --------------------- | ---------- | ------------------------------------------ |
| contains(sub)         | 包含子串   | assert_that('hello').contains('he')        |
| does_not_contain(sub) | 不包含子串 | assert_that('hello').does_not_contain('x') |
| starts_with(prefix)   | 以...开头  | assert_that('hello').starts_with('he')     |
| ends_with(suffix)     | 以...结尾  | assert_that('hello').ends_with('lo')       |
| is_empty()            | 为空字符串 | assert_that('').is_empty()                 |
| is_not_empty()        | 非空字符串 | assert_that('hi').is_not_empty()           |
| is_lower()            | 全小写     | assert_that('abc').is_lower()              |
| is_upper()            | 全大写     | assert_that('ABC').is_upper()              |

+ 列表断言

| 方法                     | 说明            | 示例                                     |
| ------------------------ | --------------- | ---------------------------------------- |
| contains(*items)         | 包含元素        | assert_that([1,2,3]).contains(2)         |
| does_not_contain(*items) | 不包含元素      | assert_that([1,2,3]).does_not_contain(4) |
| is_empty()               | 为空            | assert_that([]).is_empty()               |
| is_not_empty()           | 非空            | assert_that([1]).is_not_empty()          |
| is_length(n)             | 长度为 n        | assert_that([1,2,3]).is_length(3)        |
| is_subset_of(other)      | 是 other 的子集 | assert_that([1,2]).is_subset_of([1,2,3]) |

+ 字典断言

| 方法                      | 说明           | 示例                                           |
| ------------------------- | -------------- | ---------------------------------------------- |
| contains_key(key)         | 包含指定键     | assert_that({'a':1}).contains_key('a')         |
| contains_value(value)     | 包含指定值     | assert_that({'a':1}).contains_value(1)         |
| does_not_contain_key(key) | 不包含指定键   | assert_that({'a':1}).does_not_contain_key('b') |
| is_length(n)              | 键值对数量为 n | assert_that({'a':1, 'b':2}).is_length(2)       |

+ 类型断言

| 方法                     | 说明               | 示例                                   |
| ------------------------ | ------------------ | -------------------------------------- |
| is_type_of(type)         | 是指定类型         | assert_that(1).is_type_of(int)         |
| is_instance_of(type)     | 是指定类型的实例   | assert_that([]).is_instance_of(list)   |
| is_not_instance_of(type) | 不是指定类型的实例 | assert_that(1).is_not_instance_of(str) |

+ 其他断言

| 方法                    | 说明         | 示例                                     |
| ----------------------- | ------------ | ---------------------------------------- |
| is_in(*values)          | 在指定值中   | assert_that(2).is_in(1,2,3)              |
| is_not_in(*values)      | 不在指定值中 | assert_that(4).is_not_in(1,2,3)          |
| matches(regex)          | 匹配正则     | assert_that('abc123').matches(r'\w+\d+') |
| is_close_to(value, tol) | 在容差范围内 | assert_that(1.01).is_close_to(1.0, 0.02) |

+ 断言失败自定义提示

```python
assert_that(5).is_equal_to(6).described_as('数值不相等')
```

## 3.4 工作流程

+ 请求接口
  + 向被测系统的接口发送请求，通常包括设置请求方法URL、请求头、请求参数、请求体等。
  + 模拟客户端或其他系统对接口的真实调用，获取接口的响应数据。
+ 断言响应
  + 对接口返回的响应内容（状态码，响应体中的字段值等）进行校验，判断接口是否按照预期工作。
  + 保证接口的功能和数据正确，及时发现接口异常。
+ 变量提取（参数关联）
  + 从接口响应中提取某些关键数据（如token、user_id等），用于后续接口的请求参数，实现接口之间的数据关联。
  + 实现接口测试用例之间的数据传递，支持更复杂的业务流程测试。
  + **接口关联**，本质上就是在接口自动化测试中，实现“前一个接口的输出作为后一个接口的输入”。