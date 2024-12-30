import time
import shutil
import os
import re
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

# 启动浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开 YouTube 页面（将在当前标签页打开）
driver.get("https://www.youtube.com/")

# 等待 YouTube 页面加载完毕（根据需要调整等待时间）
time.sleep(5)

# 打开一个新的标签页并切换到该标签页
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

# 切换到本地页面
driver.get("http://localhost:8501/")

# 等待本地页面加载（根据需要调整等待时间）
time.sleep(15)

# 指定要读取的文件夹路径
folder_path = r"D:\pachong\video_data_YouTuBe"  # 替换为你的文件夹路径

# 存储所有读取到的 URL
urls = []

# URL 正则表达式，匹配常见的 URL 格式
url_pattern = r"https?://[a-zA-Z0-9./?=_-]+"  # 支持 http 或 https 的 URL

# 遍历文件夹中的所有 txt 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # 读取文件内容并查找所有匹配的 URL
                content = file.read()
                found_urls = re.findall(url_pattern, content)

                # 将找到的 URL 添加到列表中
                urls.extend(found_urls)
        except Exception as e:
            print(f"无法读取文件 {filename}: {e}")

# 处理所有 URL
for x, url in enumerate(urls, start=1):
    try:
        input_box = driver.find_element(By.ID, f"text_input_5")

        # 输入 URL
        input_box.send_keys(url)

        # 定位并点击 "下载视频" 按钮
        button = driver.find_element(By.XPATH,
                                     '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[5]/div/div/div[2]/div/button/div/p')
        button.click()
        print("下载视频已点击")

        # 等待视频元素出现，最多等 600 秒
        try:
            video_element = WebDriverWait(driver, 600).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[5]/div/div/div[1]/video"))
            )
            print("视频元素已出现，可以进行下一步操作")
        except TimeoutException:
            print("等待超时，视频元素未出现")

        # 点击 "开始处理字幕" 按钮
        # 等待按钮出现并点击
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//button[div[p[text()="开始处理字幕"]]]'))
        )
        time.sleep(3)
        button.click()
        print("开始处理字幕")

        # 等待字幕视频元素出现，最多等 999999 秒
        try:
            video_element = WebDriverWait(driver, 999999).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[7]/div/div/div[2]/video"))
            )
            print("字幕视频元素已出现，可以进行下一步操作")
        except TimeoutException:
            print("等待超时，字幕视频元素未出现")

        # 等待按钮出现并点击
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[9]/div/div/div[2]/div/button/div/p'))
        )
        button.click()
        print("开始处理音频")

        # 等待音频视频元素出现，最多等 999999 秒
        try:
            video_element = WebDriverWait(driver, 999999).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[9]/div/div/div[3]/video"))
            )
            print("音频视频元素已出现，可以进行下一步操作")
        except TimeoutException:
            print("等待超时，音频视频元素未出现")

        # 提取视频ID
        match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
        if match:
            video_id = match.group(1)
        else:
            print(f"无法从 URL 提取视频 ID: {url}")
            continue  # 如果无法提取 ID，则跳过该 URL

        # 定义源文件夹和目标文件夹路径
        source_folder = r"C:/Users/Administrator/PycharmProjects/VideoLingo/output"  # 源文件夹路径
        target_folder = r"D:/pachong/video_tts_YouTuBe/" + video_id  # 目标文件夹路径

        # 检查目标文件夹是否存在，不存在则创建
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # 使用 shutil.copytree() 将源文件夹中的内容复制到目标文件夹
        try:
            shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
            print(f"文件夹内容已成功复制到 {target_folder}")
        except Exception as e:
            print(f"复制文件夹内容时出错: {e}")
        time.sleep(5)

        # # 点击 "删除并重新选择" 按钮
        # try:
        #     print("开始准备点击删除并重新选择2")
        #     delete_button = WebDriverWait(driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[5]/div/div/div[2]/div/button/div/p'))
        #     )
        #     delete_button.click()
        #     print("删除并重新选择按钮已点击")
        # except TimeoutException:
        #     print("等待超时，删除并重新选择按钮未出现")
        #     continue  # 超时则跳过当前 URL
        # 刷新页面
        driver.refresh()
        time.sleep(15)
        print("页面已刷新")
        try:
            print("开始准备点击删除并重新选择")
            delete_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//button[div[p[text()="删除并重新选择"]]]'))
            )
            delete_button.click()
            print("删除并重新选择按钮已点击")
        except TimeoutException:
            print("等待超时，删除并重新选择按钮未出现")
            continue  # 超时则跳过当前 URL
        time.sleep(15)
        print("准备第二次点击")
        try:
            print("开始准备点击删除并重新选择")
            delete_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//button[div[p[text()="删除并重新选择"]]]'))
            )
            delete_button.click()
            print("删除并重新选择按钮已点击")
        except TimeoutException:
            print("等待超时，删除并重新选择按钮未出现")
            continue  # 超时则跳过当前 URL
        driver.refresh()
        time.sleep(20)



    except Exception as e:
        print(f"定位或操作输入框时发生错误: {e}")

    print(f"视频完成导出{x}次")

# 关闭浏览器
print("文档处理完成！")
driver.quit()
