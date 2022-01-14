# coding=utf-8
import simplejson


class ContextReq:

    # json返回
    @staticmethod
    def jsonReturn(status_code=-101, msg="", data=None):
        if data is None:
            data = {}
        return_dict = {"code": status_code, "msg": msg, "data": data}
        return simplejson.dumps(return_dict, ensure_ascii=False)
