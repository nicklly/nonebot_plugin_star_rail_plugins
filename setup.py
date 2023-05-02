#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="nonebot_plugin_star_rail_calendar",
    version="1.0.0",
    keywords=["pip", "nonebot_plugin_star_rail_calendar"],
    description="查看《崩坏：星穹铁道》官方活动",
    long_description="查看《崩坏：星穹铁道》官方活动",
    license="GPL Licence",
    url="https://github.com/nicklly/nonebot_plugin_star_rail_calendar",
    author="TonyKun",
    author_email="1134741727@qq.com",
    packages=find_packages(include=["template", "template.*"]),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "nonebot2 >= 2.0.0b1",
        "nonebot-adapter-onebot >= 2.0.0b1",
        "playwright == 1.32.1",
        "httpx == 0.23.3",
        "apscheduler == 3.10.1",
        'jinja2 == 3.1.2'
    ],
)