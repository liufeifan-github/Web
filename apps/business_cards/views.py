# coding=utf-8
from utils.ContextReq import ContextReq
from flask import Blueprint, request, render_template

bp = Blueprint("business_cards", __name__, url_prefix='/business_cards')

@bp.route('', methods=['GET'])
def index():
    return render_template('business_cards/index.html')

@bp.route('/query/', methods=['GET'])
def getInfo():
    Classification = request.args.get('Classification')
    name = request.args.get('name')
    data = {"Classification": Classification, "name": name}
    return ContextReq.jsonReturn(0, 'success', data)
