import os
from datetime import datetime

def create_markdown_post():
    # 获取输入
    folder_name = input("请输入新文件夹的名称：")
    title = input("请输入标题：")
    tags = input("请输入标签：")

    # 创建文件夹路径
    folder_path = os.path.join("D:\\vscode\\Blog\\content\\posts", folder_name)

    try:
        # 创建文件夹
        os.makedirs(folder_path, exist_ok=True)

        # Markdown 文件路径
        markdown_file_path = os.path.join(folder_path, "index.md")

        # 写入 Markdown 文件
        with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(f"---\n")
            md_file.write(f'title: "{title}"\n')
            md_file.write(f"showBreadcrumbs: true\n")
            md_file.write(f"date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')}\n")
            md_file.write(f"draft: false\n")
            md_file.write(f'tags: {tags}\n')
            md_file.write(f"---\n")

        print(f"文件夹 '{folder_name}' 和 Markdown 文件 'index.md' 创建成功！")
    
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    create_markdown_post()