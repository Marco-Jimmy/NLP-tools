# NLP-tools
自己闲着没事，写一点非常基本的NLP的小工具，没啥实用价值。

## count_frequency 高频词统计
```python
from count_frequency import word_freq_stat

with open('example_text.txt', 'r', encoding=ENCODE) as f:
    example = f.read()  # 读取示例文件，内容为爱因斯坦百度百科

word_freq_stat(example, 20)
```
输出结果为：
```
362	爱因斯坦
77	相对论
55	美国
39	理论
38	人
36	问题
34	运动
33	说
32	德国
29	发表
28	狭义
28	广义
28	原理
27	世界
26	时
25	光
24	时间
24	论文
24	速度
23	物理学
```
