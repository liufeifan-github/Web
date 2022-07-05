#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
#
# @Time    : 2022/7/4 18:13
# @Author  : Feifan Liu
# @Email   : lff18731218157@163.com
# @File    : views.py
# @Version : 1.0

# Copyright (C) 2022 北京盘拓数据科技有限公司 All Rights Reserved
from utils.ContextReq import ContextReq
from flask import Blueprint, request
from PIL import Image
import pytesseract

bp = Blueprint("servers", __name__, url_prefix='/servers')


@bp.route('', methods=['GET'])
def index():
    return "hello"


@bp.route('/ocr/', methods=['POST'])
def getInfo():
    file_obj = request.files.get("file")
    file_name = request.args.get('file_name', "test.png")
    if file_obj is None:
        return ContextReq.jsonReturn(-1, 'upload file is empty')
    # 直接使用文件上传对象保存
    file_path = "./files/{}".format(file_name)
    file_obj.save(file_path)
    tesseract_cmd = 'D:/lff/software/tesseract/tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    result = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
    data = {"result": result}
    return ContextReq.jsonReturn(0, 'success', data)
