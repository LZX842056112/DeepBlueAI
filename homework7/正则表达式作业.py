import re

"""
匹配string中所有单词的开头字母
"""
string = 'Then your voice calls me back like a wake up call'
pattern = r'\b\S'
p = re.compile(pattern, )
print(p.findall(string))
print(re.findall(pattern, string))

"""
提取string中以m或t开头的单词, 忽略大小写
"""
string = 'This module provides regular expression matching operations similar to those found in Perl'
pattern = r'\b[mt]'
p = re.compile(pattern, re.I)
print(p.findall(string))
print(re.findall(pattern, string, re.I))

"""
提取string中连续5个以上的数字
"""
string = '小明202208月见义勇为, 替小红当了3456789点暴击伤害, 快打110报警, 抓住那个劫匪'
pattern = r'\d{5,}'
p = re.compile(pattern)
print(p.findall(string))
print(re.findall(pattern, string))

"""
提取出string中的所有域名(比如: http://www.iteoem.com/ 就是域名)
"""
string = '''
http://www.iteoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
pattern = r'http://.+?/'
p = re.compile(pattern)
print(p.findall(string))
print(re.findall(pattern, string))

"""
计算一个字符串中所有的数字的和
比如:  string = 'hello90abc 78sjh12.5'
结果:  180.5 (90 + 78 + 12.5)
"""
string = 'hello90abc 78sjh12.5'
pattern = r'\d[\.\d]*'
p = re.compile(pattern)
findall = p.findall(string)
print(findall)
print(re.findall(pattern, string))
print(sum(float(i) for i in findall))
