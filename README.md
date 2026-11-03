# 个人知识库

> 记录学习、工作和成长的个人知识管理系统  
> 创建于 2026-11-03

## 📖 关于

这是一个基于 Git 的个人知识库，用于系统化地管理学习笔记、工作经验、资源收藏和个人成长记录。通过结构化的目录组织和标签系统，帮助你快速定位信息、积累知识、持续成长。

## 🚀 快速开始

### 知识库结构

```
learning/
├── 📚 learning-notes/    # 学习经验（技术、课程、读书、论文）
├── 💼 work/              # 工作记录（日志、项目、会议）
├── 🔖 resources/         # 资源收藏（文章、工具、视频、模板）
├── 📋 inventory/         # 文档位置清单（本地文件、云存储）
├── 🎯 skills/            # 技能树管理（技能清单、学习计划）
├── 💭 insights/          # 思考与复盘（周/月/年复盘、决策记录）
├── ❓ faq/               # 问题解答库（编程、工具、故障排查）
├── 🗄️ archive/           # 归档区（已完成、过时内容）
└── 🛠️ scripts/           # 辅助工具（搜索、统计、索引生成）
```

### 使用流程

1. **新建文档**：从 `resources/templates/` 复制模板
2. **分类存放**：根据内容类型放入对应目录
3. **添加标签**：在文档头部添加 `#标签`
4. **更新索引**：运行 `python3 scripts/generate_index.py`

## 📚 知识板块

### [📚 学习经验](learning-notes/)
记录技术学习、课程笔记、读书笔记和论文阅读

- [技术学习](learning-notes/tech/) - 编程、框架、AI、运维
- [课程笔记](learning-notes/courses/) - 在线课程和培训
- [读书笔记](learning-notes/books/) - 技术书籍和管理书籍
- [论文阅读](learning-notes/papers/) - 学术论文

### [💼 工作记录](work/)
记录工作日志、项目档案和会议纪要

- [工作日志](work/logs/) - 每日工作记录
- [项目档案](work/projects/) - 项目文档和复盘
- [会议纪要](work/meetings/) - 重要会议记录

### [🔖 资源收藏](resources/)
收集有价值的参考资料和工具

- [文章收藏](resources/articles/) - 技术文章和博客
- [工具推荐](resources/tools/) - 好用的工具和软件
- [视频笔记](resources/videos/) - 技术视频和演讲
- [文档模板](resources/templates/) - 可复用的模板

### [📋 文档位置清单](inventory/)
记录电脑和云端重要文件的位置

- [本地文件](inventory/local-files.md) - 本地重要文件索引
- [云存储](inventory/cloud-storage.md) - 云端资料索引
- [按类别分类](inventory/by-category/) - 工作、学习、个人文件

### [🎯 技能树](skills/)
可视化能力成长路径

- [技能清单](skills/skill-tree.md) - 技能和熟练度评估
- [学习计划](skills/learning-plans/) - 阶段性学习目标

### [💭 思考与复盘](insights/)
培养反思习惯，提炼方法论

- [周复盘](insights/weekly/) - 每周回顾
- [月复盘](insights/monthly/) - 每月总结
- [年复盘](insights/yearly/) - 年度回顾
- [决策记录](insights/decisions/) - 重要决策分析

### [❓ 问题解答库](faq/)
记录常见问题的解决方案

- [编程问题](faq/programming/) - 编程语言和框架
- [工具问题](faq/tools/) - 开发工具使用
- [故障排查](faq/troubleshooting/) - 系统故障排查

### [🗄️ 归档区](archive/)
存放已完成和过时的内容

## 🛠️ 辅助工具

### 搜索工具
```bash
# 搜索关键词
python3 scripts/search.py "关键词"

# 指定目录搜索
python3 scripts/search.py "关键词" -d learning-notes

# 区分大小写
python3 scripts/search.py "Keyword" -c
```

### 统计工具
```bash
# 查看知识库统计
python3 scripts/stats.py

# 统计指定目录
python3 scripts/stats.py learning-notes
```

### 索引生成
```bash
# 生成全局索引
python3 scripts/generate_index.py

# 指定输出文件
python3 scripts/generate_index.py . MY_INDEX.md
```

## 📝 文档模板

在 `resources/templates/` 目录下提供了以下模板：

- [学习笔记模板](resources/templates/learning-note.md)
- [项目总结模板](resources/templates/project-summary.md)
- [周复盘模板](resources/templates/weekly-review.md)
- [决策记录模板](resources/templates/decision-record.md)

使用方法：
```bash
# 复制模板到新位置
cp resources/templates/learning-note.md learning-notes/tech/python/my-note.md

# 编辑新文档
vim learning-notes/tech/python/my-note.md
```

## 🏷️ 标签系统

使用 `#标签` 格式为文档添加标签，便于分类和检索。

### 标签分类

- **领域标签**：`#programming` `#ai` `#devops` `#management`
- **技术标签**：`#python` `#react` `#docker` `#kubernetes`
- **状态标签**：`#active` `#archived` `#todo` `#review`
- **优先级标签**：`#important` `#reference`
- **类型标签**：`#note` `#tutorial` `#faq` `#project`

### 使用建议

1. 每个文档 2-5 个标签
2. 使用小写和连字符：`#machine-learning`
3. 在文档头部统一列出

## 📊 索引和导航

- [📑 全局索引](INDEX.md) - 按分类和标签浏览所有文档
- [📝 更新日志](CHANGELOG.md) - 知识库变更记录

## 💡 使用技巧

### 快速定位文档

1. **使用索引**：查看 [INDEX.md](INDEX.md) 按分类浏览
2. **使用搜索**：`python3 scripts/search.py "关键词"`
3. **使用标签**：在文档中搜索 `#标签名`

### 保持知识库健康

1. **定期更新索引**：每周运行一次索引生成脚本
2. **定期归档**：将过时内容移到归档区
3. **定期复盘**：每月回顾知识库使用情况
4. **保持命名规范**：遵循统一的文件命名规范

### 最佳实践

1. **及时记录**：学习和工作后尽快整理笔记
2. **结构化思考**：使用模板保持格式统一
3. **关联知识**：在文档间建立链接
4. **持续维护**：定期更新和整理内容

## 📈 统计信息

运行统计工具查看知识库的最新状态：

```bash
python3 scripts/stats.py
```

## 🔗 相关资源

- [AGENTS.md](AGENTS.md) - 知识库使用指南（待创建）
- [贡献指南](CONTRIBUTING.md) - 如何贡献内容（待创建）

## 📄 许可证

本项目仅供个人使用。

---

**开始使用**：从 [学习经验](learning-notes/) 或 [工作记录](work/) 开始记录你的知识旅程！
