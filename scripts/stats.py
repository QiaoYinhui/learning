#!/usr/bin/env python3
"""
知识库统计工具
统计知识库的文档数量、标签分布等信息
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime


def count_files(directory="."):
    """统计文件数量"""
    search_path = Path(directory)
    file_counts = defaultdict(int)
    total_size = 0
    
    for file_path in search_path.rglob('*'):
        if file_path.is_file() and not any(part.startswith('.') or part in ['scripts', 'node_modules', '__pycache__'] 
                                            for part in file_path.parts):
            ext = file_path.suffix.lower() or '(无扩展名)'
            file_counts[ext] += 1
            total_size += file_path.stat().st_size
    
    return file_counts, total_size


def extract_tags(directory="."):
    """提取所有标签"""
    search_path = Path(directory)
    tags = Counter()
    tag_files = defaultdict(list)
    
    tag_pattern = re.compile(r'#([a-zA-Z0-9\-_]+)')
    
    for file_path in search_path.rglob('*.md'):
        if any(part.startswith('.') or part in ['scripts', 'node_modules', '__pycache__'] 
               for part in file_path.parts):
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                found_tags = tag_pattern.findall(content)
                
                for tag in found_tags:
                    tags[tag] += 1
                    if str(file_path) not in tag_files[tag]:
                        tag_files[tag].append(str(file_path))
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}", file=sys.stderr)
    
    return tags, tag_files


def count_by_category(directory="."):
    """按分类统计文档数量"""
    search_path = Path(directory)
    categories = defaultdict(int)
    
    main_dirs = ['learning-notes', 'work', 'resources', 'inventory', 'skills', 'insights', 'faq', 'archive']
    
    for main_dir in main_dirs:
        dir_path = search_path / main_dir
        if dir_path.exists():
            count = len([f for f in dir_path.rglob('*.md') if f.is_file()])
            categories[main_dir] = count
    
    return categories


def get_recent_files(directory=".", days=7):
    """获取最近修改的文件"""
    search_path = Path(directory)
    recent_files = []
    cutoff_time = datetime.now().timestamp() - (days * 24 * 60 * 60)
    
    for file_path in search_path.rglob('*.md'):
        if any(part.startswith('.') or part in ['scripts', 'node_modules', '__pycache__'] 
               for part in file_path.parts):
            continue
        
        mtime = file_path.stat().st_mtime
        if mtime >= cutoff_time:
            recent_files.append({
                'path': str(file_path),
                'mtime': datetime.fromtimestamp(mtime)
            })
    
    recent_files.sort(key=lambda x: x['mtime'], reverse=True)
    return recent_files


def format_size(size_bytes):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def print_statistics(directory="."):
    """打印统计信息"""
    print("\n" + "=" * 80)
    print("📊 知识库统计报告")
    print("=" * 80)
    
    # 文件统计
    file_counts, total_size = count_files(directory)
    print(f"\n📁 文件统计")
    print("-" * 80)
    total_files = sum(file_counts.values())
    print(f"总文件数: {total_files}")
    print(f"总大小: {format_size(total_size)}")
    print("\n按文件类型:")
    for ext, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ext:15s}: {count:4d} 个文件")
    
    # 分类统计
    categories = count_by_category(directory)
    print(f"\n📂 分类统计")
    print("-" * 80)
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:20s}: {count:3d} 个文档")
    
    # 标签统计
    tags, tag_files = extract_tags(directory)
    if tags:
        print(f"\n🏷️  标签统计 (Top 20)")
        print("-" * 80)
        for tag, count in tags.most_common(20):
            print(f"  #{tag:20s}: {count:3d} 次使用")
    
    # 最近修改
    recent = get_recent_files(directory, days=7)
    if recent:
        print(f"\n🕒 最近 7 天修改的文件")
        print("-" * 80)
        for file_info in recent[:10]:
            print(f"  {file_info['mtime'].strftime('%Y-%m-%d %H:%M')}  {file_info['path']}")
    
    print("\n" + "=" * 80)


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not Path(directory).exists():
        print(f"错误: 目录 {directory} 不存在")
        sys.exit(1)
    
    print_statistics(directory)


if __name__ == '__main__':
    main()
