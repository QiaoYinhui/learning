#!/usr/bin/env python3
"""
索引生成工具
自动生成知识库的全局索引
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def extract_metadata(file_path):
    """从文件中提取元数据（标题、标签、日期）"""
    metadata = {
        'title': '',
        'tags': [],
        'date': '',
        'category': ''
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = []
            for i, line in enumerate(f):
                lines.append(line)
                if i >= 20:  # 只读取前 20 行
                    break
            
            content = ''.join(lines)
            
            # 提取标题（第一个 # 开头的行）
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                metadata['title'] = title_match.group(1).strip()
            
            # 提取标签
            tag_pattern = re.compile(r'#([a-zA-Z0-9\-_]+)')
            metadata['tags'] = tag_pattern.findall(content)
            
            # 提取日期
            date_patterns = [
                r'>\s*日期[：:]\s*(\d{4}-\d{2}-\d{2})',
                r'>\s*创建日期[：:]\s*(\d{4}-\d{2}-\d{2})',
                r'>\s*学习日期[：:]\s*(\d{4}-\d{2}-\d{2})',
                r'(\d{4}-\d{2}-\d{2})'
            ]
            for pattern in date_patterns:
                date_match = re.search(pattern, content)
                if date_match:
                    metadata['date'] = date_match.group(1)
                    break
            
    except Exception as e:
        print(f"读取文件 {file_path} 时出错: {e}", file=sys.stderr)
    
    return metadata


def scan_directory(directory="."):
    """扫描目录，收集所有文档信息"""
    search_path = Path(directory)
    documents = []
    
    main_dirs = ['learning-notes', 'work', 'resources', 'inventory', 'skills', 'insights', 'faq', 'archive']
    
    for main_dir in main_dirs:
        dir_path = search_path / main_dir
        if not dir_path.exists():
            continue
        
        for file_path in dir_path.rglob('*.md'):
            if file_path.name == 'README.md':
                continue
            
            if any(part.startswith('.') or part in ['scripts', 'node_modules', '__pycache__'] 
                   for part in file_path.parts):
                continue
            
            metadata = extract_metadata(file_path)
            
            # 确定分类
            relative_path = file_path.relative_to(search_path)
            category = relative_path.parts[0] if len(relative_path.parts) > 0 else 'other'
            
            documents.append({
                'path': str(relative_path),
                'title': metadata['title'] or file_path.stem,
                'tags': metadata['tags'],
                'date': metadata['date'],
                'category': category
            })
    
    return documents


def generate_index(documents, output_file="INDEX.md"):
    """生成索引文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 知识库索引\n\n")
        f.write(f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> 文档总数: {len(documents)}\n\n")
        
        # 按分类组织
        by_category = defaultdict(list)
        for doc in documents:
            by_category[doc['category']].append(doc)
        
        # 分类映射
        category_names = {
            'learning-notes': '📚 学习经验',
            'work': '💼 工作记录',
            'resources': '🔖 资源收藏',
            'inventory': '📋 文档清单',
            'skills': '🎯 技能树',
            'insights': '💭 思考与复盘',
            'faq': '❓ 问题解答库',
            'archive': '🗄️ 归档区'
        }
        
        # 生成分类索引
        f.write("## 按分类浏览\n\n")
        for category in ['learning-notes', 'work', 'resources', 'inventory', 'skills', 'insights', 'faq', 'archive']:
            if category in by_category:
                category_name = category_names.get(category, category)
                f.write(f"### {category_name}\n\n")
                
                docs = sorted(by_category[category], key=lambda x: x['date'] or '', reverse=True)
                for doc in docs:
                    title = doc['title']
                    path = doc['path']
                    date = f" ({doc['date']})" if doc['date'] else ""
                    tags = " " + " ".join([f"`#{tag}`" for tag in doc['tags'][:3]]) if doc['tags'] else ""
                    
                    f.write(f"- [{title}]({path}){date}{tags}\n")
                
                f.write("\n")
        
        # 标签索引
        all_tags = defaultdict(list)
        for doc in documents:
            for tag in doc['tags']:
                all_tags[tag].append(doc)
        
        if all_tags:
            f.write("## 按标签浏览\n\n")
            for tag in sorted(all_tags.keys()):
                f.write(f"### #{tag}\n\n")
                for doc in all_tags[tag][:10]:  # 每个标签最多显示 10 个
                    f.write(f"- [{doc['title']}]({doc['path']})\n")
                if len(all_tags[tag]) > 10:
                    f.write(f"- ... 还有 {len(all_tags[tag]) - 10} 个文档\n")
                f.write("\n")
        
        # 最近添加
        recent_docs = [doc for doc in documents if doc['date']]
        recent_docs.sort(key=lambda x: x['date'], reverse=True)
        
        if recent_docs:
            f.write("## 最近更新\n\n")
            for doc in recent_docs[:20]:
                f.write(f"- [{doc['title']}]({doc['path']}) - {doc['date']}\n")
    
    print(f"索引已生成: {output_file}")
    print(f"共索引 {len(documents)} 个文档")


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    output_file = sys.argv[2] if len(sys.argv) > 2 else "INDEX.md"
    
    if not Path(directory).exists():
        print(f"错误: 目录 {directory} 不存在")
        sys.exit(1)
    
    print("正在扫描文档...")
    documents = scan_directory(directory)
    
    print("正在生成索引...")
    generate_index(documents, output_file)


if __name__ == '__main__':
    main()
