### ARIMA时间预测专题

https://www.bilibili.com/video/BV1dT4y1V7qW?p=10&spm_id_from=pageDriver

https://www.cnblogs.com/tianqizhi/p/9277376.html

#### 对数据的要求

需要满足数据平稳性, 平稳性即序列的均值和方差不发生明显变化

#### 平稳性检验

严平稳的条件只是理论上的存在，现实中用得比较多的是宽平稳的条件。

宽平稳也叫弱平稳或者二阶平稳（均值和方差平稳），它应满足：

- 常数均值
- 常数方差
- 常数自协方差

ARIMA 模型对时间序列的要求是平稳型。因此，当你得到一个非平稳的时间序列时，首先要做的即是做时间序列的差分，直到得到一个平稳时间序列。如果你对时间序列做d次差分才能得到一个平稳序列，那么可以使用ARIMA(p,d,q)模型，其中d是差分次数。

求差分的方法

```python
sentiment_short[``'diff_1'``] ``=` `sentiment_short[``'UMCSENT'``].diff(``1``)``#求差分值，一阶差分。   1指的是1个时间间隔，可更改。
sentiment_short[``'diff_2'``] ``=` `sentiment_short[``'diff_1'``].diff(``1``)``#再求差分，二阶差分。

sentiment_short.plot(subplots``=``True``, figsize``=``(``18``, ``12``))
```