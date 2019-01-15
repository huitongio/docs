# 支点云平台(Pivaiot Cloud)开放文档

## 简介

支点云平台开放文档

## 文档编写约定

* 所有文档使用 markdown 编写，文件扩展名统一为 `.md`
* 所有 markdown 文件都放在 `/src` 目录下，中文文档放在 `/src/zh_CN` 目录下，英文文档放在 `/src/en_US` 目录下
* 每一个子类别在对应的语言目录下创建目录，把该类别的所有 markdown 文档放在这个目录下面
* 所有的图片等二进制文件都放在 `/assets` 目录下面，子目录和 `/src` 的子目录对应，对于不区分语言的文件，可以单独在 `/assets` 目录下建立文件类型的目录归纳在一起

## markdown 文档模板定义

```yaml
title: 文档标题
subtitle: 文档副标题
tags:
    - 标签1
    - 标签2
---
文档内容(使用 markdown 格式)
```

## 文档目录规则

* `h1/h2/h3` 将会自动生成页面阅读导航菜单
* 目录修改路径为 `/src/_menu`，`/src/_menu/en_US.yml` 为英文版目录，`/src/_menu/zh_CN.yml` 为中文版目录
* 最多支持三级菜单（文章名为第三级菜单），`:` 必须使用英文输入法的符号，该符号左边为显示在头部导航目录名称。
* 对于只有少于三级目录的只需在最后一级目录名称下写上 `path:` 即可
* 从属关系需严格使用两个空格缩进

## 目录配置模板

```yaml
一级目录:
  二级目录:
    三级目录(文章名):
      path: /path/to/article.md
```
