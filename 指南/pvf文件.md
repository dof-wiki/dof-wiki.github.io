# PVF 文件

## 什么是 PVF 文件

pvf 文件是指游戏根目录下的 `Script.pvf`
该文件存储了游戏的各项配置, 包括客户端和服务端的. 它是将多个文本文件/二进制文件压缩, 加密 (可选) 后得到的一个二进制文件

pvf 格式是游戏厂商自定义的一种格式, 解包, 打包都需要专门的工具. 经过多年的发展, 民间已经出现了多款 pvf 编辑器, 甚至是 IDE. 目前最常用最强大的是 [pvfutility(闭源软件, 官网已下线, 目前只能找到作者的 gitee 仓库)](https://gitee.com/icshare/pvf-utility)


## PVF 文件结构

整个 pvf 文件由以下项目构成:

| 序号 | 项目 | 长度 | 类型 |
| -- | -- | -- | -- |
| 1 | uuid_length | 4 | int |
| 2 | uuid | uuid_length | bytes |
| 3 | version | 4 | int |
| 4 | 文件树信息长度 | 4 | int |
| 5 | 文件树crc | 4 | uint |
| 6 | 文件数量 | 4 | int |
| 7 | 文件树信息 | 文件数信息长度 | bytes |
| 8 | 文件内容 | - | bytes |


**文件树信息**

这一部分存储的是 pvf 的目录结构, 或者说每个文件的元信息

| 序号 | 项目 | 长度 | 类型 |
| -- | -- | -- | -- |
| 1 | fn | 4 | uint |
| 2 | path_length | 4 | uint |
| 3 | path | path_length | bytes |
| 4 | file_length | 4 | int |
| 5 | 文件crc | 4 | uint |
| 6 | 相对偏移量 | 4 | uint |

> 相对偏移量是指相对于 8.文件内容 的起始位置的偏移量

> 具体如何解包可以参考一些开源软件: 
> - [Zageku/DNF_pvf_python](https://github.com/Zageku/DNF_pvf_python)
