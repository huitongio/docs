---
title: MQTT 协议数据接入接口(JSON)
subtitle: 使用 JSON 格式接入  物联网平台
tags: 
    - IoT
    - MQTT
    - JSON
---

# 1. 文档更新记录

## 1.1 版本记录

| 作者 | 发布日期 | 版本 | 备注 |
| :-- | :-- | :-- | :-- |
| Le | 2019-01-31 | 1.0 | 文档定稿 |

## 1.2 问题反馈

如有任何疑问或者问题反馈，请发邮件至 thisiswangle@gmail.com 或者发起 [issue](https://github.com/pivaiot/pivaiot-docs/blob/master/src/zh-CN/%E6%95%B0%E6%8D%AE%E6%8E%A5%E5%85%A5/mqtt-json-api.md)

# 2. 概要

## 2.1 MQTT 协议介绍

[MQTT](http://mqtt.org/) 是一个轻量级的发布订阅消息传输协议，非常适合物联网各类设备使用。 物联网平台提供功能完整的 MQTT 接入，支持 QoS 0/1/2，并且预置了一系列 Topic，以便快速接入系统。

## 2.2 MQTT 客户端和编程库

* mosquitto(客户端/服务器端/编程库)
* paho-mqtt(Python)
* MQTT.js(Javascript)
* eclipse paho(Java)

## 2.3 连接 MQTT 服务器(MQTT Connect)

使用设备 did (作为 username)和密钥（作为 passowrd）连接 MQTT 服务器，服务器将会返回状态码和消息内容给客户端，包括：

* 0x00, Connected, 登录成功
* 0x01, Connection Refused, miss username or password or not match, 登录失败

# 3. 数据接入接口

## 3.1 JSON 数据格式

单条数据上传

```json
{
    "data": {
        "did": "p9iLhSAxU5t9jnwMnBiJFX",
        "ts": 1549006220220,   // UNIX 时间戳，单位是毫秒
        "stringkey1": "value",
        "doubleKey2": 12.3333,
        "longKey3": 89,
        "boolKey4": false
    }
}
```

多条数据上传(批量)

```json
{
    "data": [{
        "did": "p9iLhSAxU5t9jnwMnBiJFX",
        "ts": 1549006220220,   // UNIX 时间戳，单位是毫秒
        "stringkey1": "value",
        "doubleKey2": 12.3333,
        "longKey3": 89,
        "boolKey4": false
    }]
}
```

其中：

* `did` 和 `ts` 字段是必传字段，其它字段将根据数据点定义清空进行上传
* 若上传的字段没有定义，服务器将会忽略这个字段, 未来可能会启用严格模式，即上传消息中存在未定义字段，将会舍弃当前整个消息

## 3.2 数据上传接口

数据上传接口需要使用平台内置的 topic, 如下：

```json
/v1/devices/{did}/data
```

例如设备(p9iLhSAxU5t9jnwMnBiJFX)有以下几个数据点:

| 键值 | 名称 | 数据类型 | 读写类型 | 示例 |
| :-- | :-- | :-- | :-- | :-- |
| ir1 | 红外信号 1 | INTEGER | 只读（设备只上报）|  11 |
| ir2 | 红外信号 2 | INTEGER | 只读（设备只上报）| 12 |
| smoke | 烟感信息 | INTEGER | 只读（设备只上报）| 0 |
| battery_remaining | 电池剩余电量 | INTEGER | 只读（设备只上报）| 6330 |
| feedback | 反馈信号 | BOOL | 只读（设备只上报）| false |
| light_on | 指示灯 | BOOL | 读写 | false |

上传数据格式如下：

```json
{
    "data": {
        "did": "p9iLhSAxU5t9jnwMnBiJFX",
        "ts": 1549006220220,
        "ir1": 11,
        "ir2": 12,
        "smoke": 0,
        "battery_remaining": 6330,
        "feedback": false
    }
}
```

或者通过网关一次上传多个设备的数据:

```json
{
    "data": [
        {
            "did": "p9iLhSAxU5t9jnwMnBiJFX",
            "ts": 1549006220220,
            "ir1": 11,
            "ir2": 12,
            "smoke": 0,
            "battery_remaining": 6330,
            "feedback": false
        },
        {
            "did": "p9iLhSAxU5t9jnwMnBiJFY",
            "ts": 1549006220220,
            "ir1": 11,
            "ir2": 12,
            "smoke": 0,
            "battery_remaining": 6330,
            "feedback": false
        },
    ]
}
```

## 3.3 数据点控制接口

平台提供数据控制接口以便控制设备，包括：

* 设置设备数据点的值（可以使用数据上传接口）
* 获取设备数据点当前的值
* 订阅设备数据点的变化(一般是读写类型的数据点)


### 3.3.1 设置设备数据点的值

使用设备数据上传接口


### 3.3.2 获取设备数据点当前的值

发送消息到 topic

```json
/v1/devices/{did}/data_points/request/$request_id
```

设备订阅 topic，可以获取设备的返回数据

```json
/v1/devices/{did}/data_points/response/+
```

例如数据为:

```json
{
    "data": {
        "did": "p9iLhSAxU5t9jnwMnBiJFX",
        "ts": 1549006220220,
        "ir1": 11,
        "ir2": 12,
        "smoke": 0,
        "battery_remaining": 6330,
        "feedback": false
    }
}
```

### 3.3.3 订阅数据点变化

设备订阅 topic

```json
/v1/devices/{did}/data_points

```

一旦数据点被改变，设备立即可以接收到变化的数据

```
{
    "data": {
        "did": "p9iLhSAxU5t9jnwMnBiJFX",
        "ts": 1549006220220,
        "light_on": false
    }
}
```

(完)
