# coding=utf-8
from utils.ContextReq import ContextReq
from flask import Blueprint, request, render_template

bp = Blueprint("billing_statistics", __name__, url_prefix='/billing_statistics')


@bp.route('', methods=['GET'])
def index():
    return render_template('billing_statistics/index.html')
