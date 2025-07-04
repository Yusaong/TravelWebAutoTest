# Selenium

## 一、什么是 Selenium？

Selenium 是一款**开源的 Web 自动化工具**，核心能力是模拟人类在浏览器中的操作（如点击、输入、滑动等），可理解为 “自动化浏览器操作员”。

它能自动完成打开网页、填写表单、点击按钮、抓取数据等一系列浏览器行为，广泛用于测试与自动化场景。

## 二、Selenium 能做什么？

- **自动化测试**：替代人工执行 Web 应用的功能测试（如登录流程、支付逻辑、响应时间等），提高测试效率。
- **数据采集（爬虫）**：对反爬严格的网站（如需要登录、动态加载内容的网站），通过模拟真实用户操作绕过限制，实现数据抓取。
- **自动化操作**：例如自动抢票、定时签到、批量处理网页任务等重复性操作。

## 三、工作流程

1. 编写自动化脚本（指定要执行的操作）
2. 脚本调用浏览器驱动（如 ChromeDriver）
3. 驱动打开真实浏览器，执行脚本中的操作
4. 返回操作结果（如页面数据、截图等）

## 四、优缺点分析

| 类型   | 具体说明                                                     |
| ------ | ------------------------------------------------------------ |
| ✅ 优点 | 1. 支持多浏览器（Chrome、Firefox、Edge 等） 2. 兼容多编程语言（Python、Java、C# 等） 3. 能完全模拟真实用户操作（包括 JS 渲染、动态加载） 4. 适用场景广，从测试到爬虫均能覆盖 |
| ❌ 缺点 | 1. 速度较慢（相比接口测试，需加载完整页面） 2. 维护成本高（页面结构变化易导致脚本失效） 3. 对前端依赖强，元素定位易受布局调整影响 |

## 五、核心操作指南

### 1. 环境初始化（以 Python 为例）

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def init_browser():
    # 浏览器设置
    options = Options()
    options.add_argument('--no-sandbox')  # 关闭沙盒，避免权限问题
    options.add_experimental_option("detach", True)  # 脚本结束后不关闭浏览器
    
    # 初始化浏览器（需提前下载对应版本的 ChromeDriver）
    browser = webdriver.Chrome(
        service=Service(r'chromedriver.exe'),  # 驱动路径
        options=options
    )
    
    browser.implicitly_wait(10)  # 全局隐式等待：10秒内持续查找元素，超时报错
    return browser

# 实例化浏览器并操作
browser = init_browser()
browser.get("https://baidu.com")  # 打开百度
```

### 2. 浏览器基础操作

| 操作            | 代码示例                                                  | 说明                                               |
| --------------- | --------------------------------------------------------- | -------------------------------------------------- |
| 打开网页        | `browser.get("url")`                                      | 加载指定 URL                                       |
| 调整窗口位置    | `browser.set_window_position(100, 100)`                   | 以屏幕左上角为原点，设置窗口坐标                   |
| 调整窗口大小    | `browser.set_window_size(800, 600)`                       | 设置宽、高（像素）                                 |
| 最大化 / 最小化 | `browser.maximize_window()` / `browser.minimize_window()` | 全屏或最小化窗口                                   |
| 刷新页面        | `browser.refresh()`                                       | 等效于 F5 刷新                                     |
| 截图            | `browser.get_screenshot_as_file("截图名.png")`            | 保存当前页面截图                                   |
| 打开新标签页    | `browser.execute_script("window.open('');")`              | 通过 JS 脚本打开新标签                             |
| 切换标签页      | `browser.switch_to.window(browser.window_handles[1])`     | `window_handles` 为标签页列表，索引 0 是第一个标签 |
| 关闭当前标签    | `browser.close()`                                         | 仅关闭当前标签，不退出浏览器                       |
| 退出浏览器      | `browser.quit()`                                          | 关闭所有标签并退出浏览器                           |

### 3. 元素定位（核心操作）

元素定位是 Selenium 的核心，需先定位到网页元素（如输入框、按钮），才能执行后续操作。以下是 8 种定位方式的详细说明：

#### （1）ID 定位

- 用法：通过元素的 `id` 属性定位（`id` 通常唯一）
- 代码：`browser.find_element(By.ID, "元素id值")`
- 注意：并非所有元素都有 `id`，且部分网站 `id` 可能动态生成（此时不可用）。

#### （2）NAME 定位

- 用法：通过元素的 `name` 属性定位
- 代码：`browser.find_element(By.NAME, "元素name值")`
- 注意：`name` 属性重复率较高，可能返回多个结果（需用索引筛选，如 `elements[0]`）。

#### （3）CLASS_NAME 定位

- 用法：通过元素的 `class` 属性定位
- 代码：`browser.find_element(By.CLASS_NAME, "元素class值")`
- 注意：`class` 值中不能包含空格（空格代表多类名）；可能存在多个匹配元素。

#### （4）TAG_NAME 定位

- 用法：通过 HTML 标签名定位（如 `div`、`input`、`a`）
- 代码：`browser.find_element(By.TAG_NAME, "标签名")`
- 注意：标签名重复率极高（如页面可能有多个 `div`），需结合索引筛选（如 `elements[2]`）。

#### （5）LINK_TEXT 定位

- 用法：仅用于 `<a>` 标签（链接），通过完整链接文本定位
- 代码：`browser.find_element(By.LINK_TEXT, "完整链接文字")`
- 示例：定位文本为 “百度首页” 的链接：`find_element(By.LINK_TEXT, "百度首页")`。

#### （6）PARTIAL_LINK_TEXT 定位

- 用法：仅用于 `<a>` 标签，通过模糊匹配链接文本定位（包含指定文字即可）
- 代码：`browser.find_element(By.PARTIAL_LINK_TEXT, "部分链接文字")`
- 示例：定位包含 “首页” 的链接：`find_element(By.PARTIAL_LINK_TEXT, "首页")`。

#### （7）CSS_SELECTOR 定位（推荐）

- 用法：通过元素属性、层级关系等灵活定位，功能强大且速度快。
- 常用语法：
  - `#id`：通过 id 定位（如 `#username` 定位 id="username" 的元素）
  - `.class`：通过 class 定位（如 `.btn` 定位 class="btn" 的元素）
  - `标签名`：通过标签定位（如 `input` 定位所有 `<input>` 元素）
  - `[属性=值]`：通过任意属性定位（如 `[name='password']` 定位 name="password" 的元素）
  - 模糊匹配：`[属性*=值]`（包含）、`[属性^=值]`（开头）、`[属性$=值]`（结尾）
- 快捷方式：在浏览器开发者工具中右键元素 → Copy → Copy selector，直接获取唯一选择器。

#### （8）XPATH 定位（万能方案）

- 用法：通过元素路径或属性定位，支持复杂场景（如动态元素）。
- 常用语法：
  - 绝对路径：`/html/body/div[1]/input`（从根节点开始，不推荐，易失效）
  - 相对路径：`//input[@name='username']`（定位 name="username" 的 `<input>`）
  - 文本匹配：`//div[text()='登录']`（文本为 “登录” 的 `<div>`）
  - 模糊文本：`//a[contains(text(), '注册')]`（文本包含 “注册” 的 `<a>`）
- 快捷方式：在浏览器开发者工具中右键元素 → Copy → Copy Xpath / Copy full Xpath。

### 4. 元素交互（定位后操作）

定位到元素后，可执行输入、点击等操作：

| 操作类型     | 示例代码                        | 说明                                              |
| ------------ | ------------------------------- | ------------------------------------------------- |
| 输入内容     | `element.send_keys("Selenium")` | 向输入框等元素输入文本内容                        |
| 清空内容     | `element.clear()`               | 清空输入框中的现有内容                            |
| 点击元素     | `button.click()`                | 点击按钮、链接等可交互元素                        |
| 获取文本     | `print(button.text)`            | 获取元素内的可见文本（如按钮文字、标签内容）      |
| 判断可见性   | `print(element.is_displayed())` | 判断元素是否在页面上可见（返回布尔值）            |
| 判断是否可用 | `print(input_box.is_enabled())` | 判断元素是否可交互（如输入框是否禁用）            |
| 判断是否选中 | `print(checkbox.is_selected())` | 判断复选框 / 单选框是否被选中（仅适用于此类元素） |

对于复杂场景（如元素被遮挡、需滚动到元素位置），可通过执行 JavaScript 代码实现交互：

```python
# 使用 JavaScript 点击元素（适用于被遮挡的元素）
element = browser.find_element(By.ID, "hidden_button")  # 定位被遮挡的按钮
browser.execute_script("arguments[0].click();", element)  # 执行 JS 点击

# 滚动到元素位置
target_element = browser.find_element(By.XPATH, "//div[@id='target']")
browser.execute_script("arguments[0].scrollIntoView();", target_element)  # 滚动到目标元素
```

### 5. 特殊场景处理

#### （1）弹窗交互

网页弹窗（如 alert、confirm、prompt）需通过 `switch_to.alert` 处理：

| 弹窗类型 | 操作方法                                                     | 说明                                |
| -------- | ------------------------------------------------------------ | ----------------------------------- |
| Alert    | `alert.accept()`                                             | 警告框，仅包含确认按钮              |
| Confirm  | `alert.accept()` 或 `alert.dismiss()`                        | 确认框，包含确认和取消按钮          |
| Prompt   | `alert.send_keys("文本")` 输入内容后，再调用 `accept()` 或 `dismiss()` | 提示框，包含输入框和确认 / 取消按钮 |

```python
import time

# 打开含弹窗的页面
browser.get("https://sahitest.com/demo/promptTest.htm")
# 点击按钮触发弹窗
browser.find_element(By.XPATH, "/html/body/form/input[1]").click()
time.sleep(2)  # 等待弹窗加载

# 操作弹窗
alert = browser.switch_to.alert
print(alert.text)  # 打印弹窗文本
alert.send_keys("输入弹窗内容")  # 向 prompt 弹窗输入内容
alert.accept()  # 点击“确定”
# alert.dismiss()  # 点击“取消”
```

#### （2）iframe 嵌套页面

iframe 是网页中的 “子页面”，需先切换到 iframe 才能操作其中元素：

| 操作步骤                | 代码示例                                                     | 说明                             |
| ----------------------- | ------------------------------------------------------------ | -------------------------------- |
| 1. 定位 iframe 元素     | `iframe = browser.find_element(By.XPATH, "//iframe[@id='myiframe']")` | 通过 ID、XPath 等方式定位 iframe |
| 2. 切换到 iframe 内部   | `browser.switch_to.frame(iframe)`                            | 进入 iframe 上下文               |
| 3. 操作 iframe 内的元素 | `browser.find_element(By.XPATH, "//button").click()`         | 在 iframe 内定位并操作元素       |
| 4. 退出 iframe          | `browser.switch_to.default_content()`                        | 返回主页面上下文                 |

```python
# 打开含 iframe 的页面
browser.get("https://sahitest.com/demo/iframesTest.htm")
# 1. 定位 iframe 元素
iframe = browser.find_element(By.XPATH, "/html/body/iframe")
# 2. 切换到 iframe 内部
browser.switch_to.frame(iframe)

# 3. 操作 iframe 内的元素（如点击链接）
browser.find_element(By.XPATH, "/html/body/table/tbody/tr/td[1]/a[1]").click()

# 4. 退出 iframe（返回主页面）
browser.switch_to.default_content()
# 5. 操作主页面元素
browser.find_element(By.XPATH, "/html/body/input[2]").click()
```

#### （3）等待机制（解决元素加载延迟）

网页元素可能因网络或动态加载延迟出现，需设置等待避免 “元素未找到” 错误。

| 对比项   | 隐式等待（Implicit Wait）                   | 显式等待（Explicit Wait）                |
| -------- | ------------------------------------------- | ---------------------------------------- |
| 作用范围 | 全局生效（对所有元素定位有效）              | 局部生效（仅针对指定元素 / 条件）        |
| 设置方式 | `browser.implicitly_wait(10)`（等待 10 秒） | `WebDriverWait(browser, 10).until(条件)` |
| 等待条件 | 仅等待元素 “存在”                           | 可等待元素 “可见”“可点击”“文本出现” 等   |
| 灵活性   | 低（无法定制条件）                          | 高（支持复杂条件）                       |
| 适用场景 | 页面元素加载速度较一致的场景                | 部分元素加载慢（如图片、动态内容）       |

**显式等待示例**：

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等待 10 秒，直到元素（id="kw"）可点击
wait = WebDriverWait(browser, 10)
search_input = wait.until(
    EC.element_to_be_clickable((By.ID, "kw"))
)
search_input.send_keys("显式等待示例")
```

## 六、优缺点总结

| 优势                               | 劣势                                     |
| ---------------------------------- | ---------------------------------------- |
| 支持多浏览器（Chrome、Firefox 等） | 速度较慢（需加载完整页面，比接口测试慢） |
| 兼容多语言（Python、Java、C# 等）  | 维护成本高（页面结构变化易导致脚本失效） |
| 能模拟真实用户操作（绕过部分反爬） | 对前端依赖强（元素定位受布局影响大）     |

## 七、实用技巧

1. **无头模式**：设置 `options.add_argument('--headless=new')`，可在无界面模式下运行（节省资源，适合服务器）。
2. **规避检测**：部分网站会检测 Selenium，可通过设置 `options.add_experimental_option("excludeSwitches", ["enable-automation"])` 规避。
3. **动态元素处理**：结合显式等待（如等待元素可见），避免因加载延迟导致定位失败。
4. **元素等待优先级**：优先使用显式等待（灵活），全局可搭配隐式等待（保底）。