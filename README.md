

# HeyRoom

小黑屋留学网站

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/shaojintian/heyroom/">
    <img src="static/logos/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">"完美的"README模板</h3>
  <p align="center">
    一个"完美的"README模板去快速开始你的项目！
    <br />
    <a href="https://github.com/shaojintian/heyroom"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/shaojintian/heyroom">查看Demo</a>
    ·
    <a href="https://github.com/shaojintian/heyroom/issues">报告Bug</a>
    ·
    <a href="https://github.com/shaojintian/heyroom/issues">提出新特性</a>
  </p>

</p>


 本篇README.md面向开发者
 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与项目](#如何参与项目)
  - [如何提交自己的代码到master](#如何提交自己的代码到master)
- [版本控制](#版本控制)
- [作者及其联系](#作者及其联系)
- [鸣谢](#鸣谢)

### 上手指南

以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。关于如何将该项目部署到在线环境，请参考部署小节。

###### 开发前的配置要求

1. Django 2.2.7
2. Python 3.7
3. Mysql 8.0.13
4. MongoDB 4.0.3

###### **安装步骤**


1. Clone the repo

```sh
git clone https://github.com/shaojintian/heyroom.git
```
2. Run the project
```bash
 python manage.py runserver localhost:8080
```

### 文件目录说明
eg:

```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /account/
├── /bbs/
├── /docs/
│  ├── /rules/
│  │  ├── backend.txt
│  │  └── frontend.txt
├── manage.py
├── /oa/
├── /static/
├── /templates/
├── useless.md
└── /util/

```





### 开发的架构 

请阅读[ARCHITECTURE.md](https://github.com/shaojintian/heyroom/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

1. 腾讯云服务器172.81.235.217
2. 域名www.liuxueheyroom



### 使用到的框架

- Django
- xadmin
- restful API

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与项目



1. Fork the Project
2. Create your Feature Branch (`git checkout -b xxx-dev`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin xxx-dev`)
5. Open a Pull Request

#### 如何提交自己的代码到master

1. 按上述创建好自己的branch
2. git update from master 
3. 修改你的branch的代码
4. 确保无误后，提交到你的分支: 
```bash
git commit -m "..." 
git push origin xxx-dev
```

5. 更新你的分支后，更新你的branch到master:
```bash
切换到master分支
GitHub Desktop -> Branch -> Merge into Current Branch -> 选择xxx-dev
```




### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

邵靳天@铭丰科技

知乎:笃行er  &ensp; qq:1075803623     

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/shaojintian/heyroom/blob/master/LICENSE.txt)

### 鸣谢

 感谢铭丰科技小伙伴和其他项目的支持和陪伴
 - [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [abcadamk1](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:shaojintian/heyroom
[contributors-shield]: https://img.shields.io/github/contributors/shaojintian/heyroom.svg?style=flat-square
[contributors-url]: https://github.com/shaojintian/heyroom/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shaojintian/heyroom.svg?style=flat-square
[forks-url]: https://github.com/shaojintian/heyroom/network/members
[stars-shield]: https://img.shields.io/github/stars/shaojintian/heyroom.svg?style=flat-square
[stars-url]: https://github.com/shaojintian/heyroom/stargazers
[issues-shield]: https://img.shields.io/github/issues/shaojintian/heyroom.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/shaojintian/heyroom.svg
[license-shield]: https://img.shields.io/github/license/shaojintian/heyroom.svg?style=flat-square
[license-url]: https://github.com/shaojintian/heyroom/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian




