#!/usr/bin/env python3
"""
知识库搜索工具
快速搜索知识库中的文档内容
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime


def search_content(keyword, directory=".", case_sensitive=False, file_type="md"):
    """搜索文件内容"""
    results = []
    search_path = Path(directory)
    
    if not search_path.exists():
        print(f"错误: 目录 {directory} 不存在")
        return results
    
    # 遍历所有文件
    for file_path in search_path.rglob(f"*.{file_type}"):
        # 跳过隐藏目录和脚本目录
        if any(part.startswith('.') or part in ['scripts', 'node_modules', '__pycache__'] 
               for part in file_path.parts):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for line_num, line in enumerate(lines, 1):
                # 搜索关键词
                search_line = line if case_sensitive else line.lower()
                search_keyword = keyword if case_sensitive else keyword.lower()
                
                if search_keyword in search_line:
                    results.append({
                        'file': str(file_path),
                        'line': line_num,
                        'content': line.strip()
                    })
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}", file=sys.stderr)
    
    return results


def print_results(results, keyword):
    """打印搜索结果"""
    if not results:
        print(f"未找到包含 '{keyword}' 的内容")
        return
    
    print(f"\n找到 {len(results)} 处匹配:\n")
    print("=" * 80)
    
    current_file = None
    for result in results:
        if result['file'] != current_file:
            current_file = result['file']
            print(f"\n📄 {current_file}")
            print("-" * 80)
        
        print(f"  第 {result['line']:4d} 行: {result['content']}")
    
    print("\n" + "=" * 80)
    print(f"共 {len(results)} 处匹配")


def main():
    parser = argparse.ArgumentParser(description='搜索知识库内容')
    parser.add_argument('keyword', help='搜索关键词')
    parser.add_argument('-d', '--directory', default='.', help='搜索目录 (默认: 当前目录)')
    parser.add_argument('-c', '--case-sensitive', action='store_true', help='区分大小写')
    parser.add_argument('-t', '--type', default='md', help='文件类型 (默认: md)')
    
    args = parser.parse_args()
    
    print(f"正在搜索 '{args.keyword}'...")
    results = search_content(args.keyword, args.directory, args.case_sensitive, args.type)
    print_results(results, args.keyword)


if __name__ == '__main__':
    main()
