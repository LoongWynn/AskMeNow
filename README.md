# Ask Me Now

## 项目介绍
利用 LLM 赋能开发者进行代码开发已经成为一个热点领域，然而，现在已提供的代码分析增强LLM服务大多基于公网云服务，对于企业内部关键代码，暴露至公网存在较大安全风险，因此设计一套能够在内网部署分析的混合云代码分析增强LLM服务存在较大的需求。

本项目基于代码托管平台，通过API拉取代码文件，并利用 issue hook，自动创建和关闭 conversation，为开发者提供快捷、安全的可内网部署分析的代码分析增强 LLM 服务。

## 技术特点
- 基于容器化技术，可以根据不同的需求，进行裸金属机单机部署、容器化单机部署、容器化单机混合部署、k8s集群部署、Helm集群部署等。

- 依赖封装完整，可以根据不同的需求，在线、离线和混合式部署，并支持在线更新和离线更新基础语言模型。

- 面向 OneAPI 和 OpenVino（未测试）进行自动语言模型量化，增强在 Intel 硬件上 LLM 推理性能，同时支持 CPU（未测试）和 GPU 部署。

## 使用到的Intel软硬件技术
- Intel&reg; Extension for Pytorch
- Intel&reg; Extension for Transformers
- OneAPI&trade; Toolkit
- OpenVINO&trade; Toolkit
- IPEX-LLM

- 英特尔锐炫&trade; A770 显卡
- 英特尔&reg; 酷睿&trade; Ultra 处理器

## 成果展示
请访问 [AskMeNow](https://github.com/LoongWynn/AskMeNow) Github 示例程序，服务器配置为双路英特尔锐炫&trade; A770 显卡。
离线本地部署请参考 [本地部署说明](./local_deploy.md)
