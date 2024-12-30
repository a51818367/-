import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

# 设置 Chrome 配置文件路径
chrome_options = Options()

# 设置 User-Agent 伪装
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59"
]
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# 禁用 WebDriver 标志，防止被检测到是自动化工具
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# 设置 Chrome 配置文件
chrome_options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("profile-directory=Profile 1")  # 选择配置文件

# 设置 ChromeDriver 路径
service = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

# 启动浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

# 用户 URL 列表
user_urls = [
    "https://www.tiktok.com/@zackdfilms2.2",
    # "https://www.tiktok.com/@5.5m60",  # 添加更多的用户 URL
    # "https://www.tiktok.com/@user3",127 507
]

# 模拟滚动行为
def scroll_page():
    last_height = driver.execute_script("return document.body.scrollHeight")  # 获取页面初始高度
    while True:
        # 滚动到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 随机等待时间（例如 2 到 5 秒之间）
        wait_time = random.uniform(2, 5)  # 随机等待 2 到 5 秒
        print(f"等待 {wait_time:.2f} 秒...")
        time.sleep(wait_time)  # 等待新内容加载

        # 获取新的页面高度
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 如果新高度等于旧高度，说明已经到达页面底部，跳出循环
        if new_height == last_height:
            break

        last_height = new_height  # 更新页面高度


# 获取视频 URL
def get_video_urls(url):
    driver.get(url)

    # 随机等待 3 到 10 秒来模拟不同的用户访问速度
    initial_wait_time = random.uniform(3, 10)
    print(f"等待 {initial_wait_time:.2f} 秒，准备访问页面 {url}")
    time.sleep(initial_wait_time)

    scroll_page()

    # 获取页面源代码
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # 查找所有视频的 <a> 标签，根据类名找到视频 URL
    video_urls = []
    for a_tag in soup.find_all('a', class_='css-1g95xhm-AVideoContainer e19c29qe13'):  # 这里的类名是示例，实际可能不同
        video_url = f"https://www.tiktok.com{a_tag['href']}"
        video_urls.append(video_url)

    return video_urls


# 删除每个视频 URL 中的第一个 https://www.tiktok.com
def remove_first_tiktok_prefix(video_urls):
    cleaned_urls = []
    for url in video_urls:
        if url.count("https://www.tiktok.com") > 1:  # 检查 URL 是否包含多个 https://www.tiktok.com
            # 删除第一个 https://www.tiktok.com
            cleaned_url = url.replace("https://www.tiktok.com", "", 1)  # 只删除第一个
            cleaned_urls.append(cleaned_url)
        else:
            cleaned_urls.append(url)
    return cleaned_urls


# 保存视频 URL 到文件
def save_video_urls(username, video_urls):
    # 创建目录，如果不存在
    output_dir = r"D:\pachong\video_data_TikTok"  # 替换为实际目录路径
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 输出文件路径
    file_path = os.path.join(output_dir, f"{username}.txt")

    # 清理 URL 中的第一个 https://www.tiktok.com
    video_urls = remove_first_tiktok_prefix(video_urls)

    # 将清理后的 URL 保存到文件
    with open(file_path, 'w', encoding='utf-8') as file:
        for video_url in video_urls:
            file.write(video_url + '\n')

    print(f"视频 URL 已成功保存到文件：{file_path}")


# 对每个用户 URL 执行爬取任务
for user_url in user_urls:
    print(f"正在处理用户页面: {user_url}")
    try:
        # 随机等待时间，模拟不同的用户间隔
        random_wait_before_access = random.uniform(5, 10)
        print(f"等待 {random_wait_before_access:.2f} 秒，准备访问用户页面...")
        time.sleep(random_wait_before_access)

        video_urls = get_video_urls(user_url)

        if video_urls:
            username = user_url.split('@')[1]  # 获取目标用户名
            save_video_urls(username, video_urls)
        else:
            print(f"没有找到视频数据：{user_url}")

    except Exception as e:
        print(f"处理 {user_url} 时出错: {e}")

# 关闭浏览器
driver.quit()
