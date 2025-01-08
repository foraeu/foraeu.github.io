// 处理折叠面板
document.addEventListener('DOMContentLoaded', function() {
    const panels = document.querySelectorAll('.collapse-panel');
    panels.forEach(panel => {
        const content = panel.querySelector('.collapse-content');
        content.style.maxHeight = null;
        
        panel.querySelector('.collapse-header').addEventListener('click', function() {
            panel.classList.toggle('active');
            if (panel.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = null;
            }
        });
    });
});

//代码块复制
document.addEventListener('DOMContentLoaded', () => {
    // 为每个代码块添加复制按钮
    document.querySelectorAll('pre').forEach(pre => {
        // 创建包装容器
        const wrapper = document.createElement('div');
        wrapper.className = 'code-header';
        
        // 创建复制按钮
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = '复制';
        
        // 包装pre元素
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        wrapper.appendChild(button);
        
        // 添加点击事件
        button.addEventListener('click', async () => {
            try {
                const code = pre.querySelector('code').textContent;
                await navigator.clipboard.writeText(code);
                
                button.textContent = '已复制！';
                button.classList.add('copied');
                
                setTimeout(() => {
                    button.textContent = '复制';
                    button.classList.remove('copied');
                }, 2000);
            } catch (err) {
                button.textContent = '复制失败';
                console.error('复制失败:', err);
            }
        });
    });
});
