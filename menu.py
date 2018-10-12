import json
import os

import yaml # pip install pyyaml

'''
列出posts目录下面所有的目录和md文件来生成文档的列表，文档列表使用 Gitbook 的 SUMMARY 格式, 具体方法如下:
    1. 如果是目录
        1.1 则读取目录下的 `meta.json`, 来获取目录路径所对应的显示名称，如果没有 `meta.json` 文件, 则使用路径名代替显示名称
        1.2 递归读取目录
    2. 如果是markdown文件，则解析文件，获得文件的显示名称

把读取到的内容按照 Gitbook SUMMARY 的格式写入到 SUMMARY.md 文件中
'''

def readfile(path):
    with open(path, 'r') as f:
        return f.read()


def writefile(path, content):
    with open(path, 'w') as f:
        f.write(content)


def getdirtitle(path):
    obj = json.loads(readfile("%s/meta.json" % path))
    return obj['name']


def getfiletitle(path):
    objs = yaml.load_all(readfile(path))
    for obj in objs:
        return obj['title']


def listitems(padding="* ", path="posts"):
    items = []
    files = os.listdir(path)
    for f in files:
        filepath = '%s/%s' % (path, f)
        isdir = os.path.isdir(filepath)
        if isdir:
            title = getdirtitle(filepath)
            items.extend(listitems('  %s' % padding, filepath))
        else:
            if not filepath.endswith('.md'):
                continue
            title = getfiletitle(filepath)

        items.append((padding, title, filepath))

    return items


def createsummary(items):
    items = map(lambda a: "%s[%s](%s)" % (a[0], a[1], a[2]), items)
    items = list(items)
    items.append('# 目录\n')
    items.reverse()

    writefile('SUMMARY.md', '\n'.join(items))


def createmenu(items):
    items = map(lambda a: dict(level=int((len(a[0])-2)/2), title=a[1], \
            url=a[2].replace('.md', '.html')), items)
    items = list(items)
    items.reverse()
    jsonstring = json.dumps(items, indent=2, ensure_ascii=False)

    writefile('menu.json', jsonstring)


if __name__ == '__main__':
    items = listitems()

    createsummary(items)
    createmenu(items)

