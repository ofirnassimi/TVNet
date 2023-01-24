# from flask import jsonify, request
# from manage import app
#
#
# class InvalidAPIUsage(Exception):
#     status_code = 400
#
#     def __init__(self, message, status_code=None, payload=None):
#         super().__init__()
#         self.message = message
#         if status_code is not None:
#             self.status_code = status_code
#         self.payload = payload
#
#     def to_dict(self):
#         rv = dict(self.payload or ())
#         rv['message'] = self.message
#         return rv
#
# @app.errorhandler(InvalidAPIUsage)
# def invalid_api_usage(e):
#     return jsonify(e.to_dict()), e.status_code