# 气象数据的各种插值问题


{{< figure src="/img/20230527/20230527_avatar.png" title="文章封面, 由作者通过 Canva 网站制作" >}}

到目前为止，我接触到的气象相关数据有`站点数据`、`等经纬度网格数据`和 `WRF（天气研究与预报）数据`。

> 注：为叙述简便，`等经纬度网格数据` 下简称 `网格数据`，`WRF（天气研究与预报）数据` 简称 `WRF 数据`，`站点数据` 不变。

<br/>

`站点数据`通常用 [`Pandas`](https://docs.xarray.dev/en/stable/getting-started-guide/quick-overview.html) 读取，结构就像这样：

```
   lat  lon  val
0   15  136  156
1   18  125  325
2   25  114  514
3   24  124  222
4   23  126  745
5   18  111  824
```

其中 `lat` 表示纬度，`lon` 表示经度，`val` 表示站点观测值。<br/><br/>

`网格数据`通常用 [`Xarray`](https://docs.xarray.dev/en/stable/getting-started-guide/quick-overview.html) 读取，结构就像这样：

```
<xarray.DataArray (lat: 5, lon: 6)>
array([[ nan,  nan,  nan,  nan,  nan, 156.],
       [824.,  nan,  nan, 325.,  nan,  nan],
       [ nan,  nan,  nan,  nan, 745.,  nan],
       [ nan,  nan, 222.,  nan,  nan,  nan],
       [ nan, 514.,  nan,  nan,  nan,  nan]])
Coordinates:
  * lat      (lat) int64 15 18 23 24 25
  * lon      (lon) int64 111 114 124 125 126 136
```

其中，`lat` 和 `lon` 是这个数据的两个维度，即纬度和经度，`Coordinates` 展示了这两个维度对应的坐标信息。<br/><br/>

`WRF 数据`通常用 [`netCDF4`](https://unidata.github.io/netcdf4-python/) 读取，结构就像这样：

```
```

与等经纬度网格相比，`WRF 数据`的维度和坐标形式不太一样，它是按兰博特投影存储数据的。<br/><br/>

在实际使用过程中，经常会有这样的需求：

- 将`网格数据`插值到另一个坐标、分辨率不同的`网格数据`上
- 将`网格数据`插值到`站点数据`上
- 将 `WRF 数据`插值到`站点数据`上
- 将`站点数据`插值到`网格数据`上
- ...

> 注：将其他数据插值到 `WRF 数据` 上的需求较少。

下面分别讲述这几种需求如何做，点击下表的`数据名称`可以下载使用到的示例数据：

| 数据名称 | 下载来源 |
| ----    | ----    |
| [`网格数据`]() | |
| [`站点数据`]() | |
| [`WRF 数据`]() | [https://wrf.nrs.gov.bc.ca/](https://wrf.nrs.gov.bc.ca/) |

<br/>

### 将`网格数据`插值到另一个坐标、分辨率不同的`网格数据`上


### 将`网格数据`插值到`站点数据`上


### 将 `WRF 数据`插值到`站点数据`上


### 将`站点数据`插值到`网格数据`上（反距离权重插值）



