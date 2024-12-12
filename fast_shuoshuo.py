import sys
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox

class MarkdownGenerator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Markdown 文件生成器")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()

        # 文件名输入
        self.file_name_label = QLabel("文件名（不带扩展名）：")
        self.layout.addWidget(self.file_name_label)
        self.file_name_input = QLineEdit()
        self.layout.addWidget(self.file_name_input)

        # 标题输入
        self.title_label = QLabel("标题：")
        self.layout.addWidget(self.title_label)
        self.title_input = QLineEdit()
        self.layout.addWidget(self.title_input)

        # 内容输入
        self.content_label = QLabel("内容：")
        self.layout.addWidget(self.content_label)
        self.content_input = QTextEdit()
        self.layout.addWidget(self.content_input)

        # 生成按钮
        self.generate_button = QPushButton("生成 Markdown 文件")
        self.generate_button.clicked.connect(self.generate_markdown)
        self.layout.addWidget(self.generate_button)

        self.setLayout(self.layout)

    def generate_markdown(self):
        file_name = self.file_name_input.text() + ".md"
        title = self.title_input.text()
        content = self.content_input.toPlainText()
        now = datetime.now()
        
        if not file_name or not title or not content:
            QMessageBox.warning(self, "输入错误", "文件名、标题和内容不能为空！")
            return
        
        date_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
        time_str = now.strftime("%H:%M")
        
        markdown_content = f"""---
date: {date_str}
---
{{{{% memo title={title} date={now.strftime('%Y年%m月%d日')} time={time_str} %}}}}
{content}
{{{{% /memo %}}}}
"""
        
        save_path = r"D:\vscode\Blog\content\shuoshuo-single"
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, file_name)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        index_file_path = r"D:\vscode\Blog\content\shuoshuo\index.md"
        with open(index_file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{{{{% include \"/shuoshuo-single/{file_name}\" %}}}}")

        QMessageBox.information(self, "成功", f"Markdown 文件已创建：{file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownGenerator()
    window.show()
    sys.exit(app.exec())

