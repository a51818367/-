import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 Chrome 配置文件路径
chrome_options = Options()

# 设置 Chrome 用户数据目录
chrome_options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")  # 使用原始字符串
chrome_options.add_argument("profile-directory=Profile 1")  # 选择你要使用的配置文件

# 设置 ChromeDriver 路径
service = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

# 用于存储视频信息的列表
video_data = []

# 定义用户 URL 列表
user_urls = [
    'https://www.youtube.com/@slimkuns/videos',
    'https://www.youtube.com/@josedoblajes/videos',  # 添加更多用户的 URL
    # 'https://www.youtube.com/@anotheruser/videos',
]

# 滚动页面并确保加载更多视频
def scroll_to_load_videos(driver, max_scrolls=20):
    """
    滚动页面加载视频
    :param driver: 浏览器实例
    :param max_scrolls: 最大滚动次数，防止无限滚动
    """
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    scroll_count = 0
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")  # 滚动到页面底部
        time.sleep(2)  # 等待加载
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        # 如果页面没有变化，停止滚动
        if new_height == last_height:
            break

        last_height = new_height
        scroll_count += 1
        print(f"Scrolling... ({scroll_count}/{max_scrolls})")

# 提取视频信息
def extract_video_data(driver, user_url):
    video_data = []
    driver.get(user_url)

    # 显式等待页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/watch?v=")]')))

    # 滚动加载更多视频
    scroll_to_load_videos(driver)

    # 获取视频元素
    video_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/watch?v=")]')

    # 遍历视频元素，提取视频信息
    for video in video_elements:
        try:
            title = video.get_attribute('title')  # 获取视频标题
            link = video.get_attribute('href')  # 获取视频链接

            # 如果标题有效，添加到视频数据列表中
            if title:  # 只有非空标题才有效
                video_data.append((title, link))
        except Exception as e:
            print(f"Error extracting data for video: {e}")
    return video_data

# 保存视频数据到文件
def save_video_data(user_url, video_data, custom_output_dir=None):
    # 提取用户名作为文件名
    username = user_url.split('@')[1].split('/')[0]

    # 如果没有指定自定义输出路径，则使用默认路径
    output_dir = custom_output_dir if custom_output_dir else 'video_data'

    # 创建文件路径，确保文件夹存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 保存初步的输出到临时 txt 文件
    temp_output_file = os.path.join(output_dir, f"{username}_videos_temp.txt")
    with open(temp_output_file, 'w', encoding='utf-8') as f:
        f.write(f"Successfully opened the user page: {user_url}\n")
        f.write("Video Titles and Links:\n")
        for title, link in video_data:
            f.write(f"Title: {title} - URL: {link}\n")

    # 读取临时文件，去掉前两行
    def remove_first_two_lines(input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()  # 读取所有行

        # 跳过前两行
        remaining_lines = lines[2:]

        # 将剩余内容写入新文件
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(remaining_lines)

        print(f"File saved to {output_file}")

    # 新文件路径
    final_output_file = os.path.join(output_dir, f"{username}_videos.txt")

    # 删除前两行并保存最终文件
    remove_first_two_lines(temp_output_file, final_output_file)

    # 删除临时文件
    os.remove(temp_output_file)

# 启动 Chrome 浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

# 对每个用户 URL 执行爬取任务
for user_url in user_urls:
    print(f"Processing {user_url}...")
    video_data = extract_video_data(driver, user_url)

    # 设置自定义输出路径（如果需要）
    custom_output_dir = r"D:\pachong\video_data_YouTuBe"  # 修改为您希望保存文件的文件夹路径

    save_video_data(user_url, video_data, custom_output_dir)

# 关闭浏览器
driver.quit()

