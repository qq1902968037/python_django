from django.utils.deprecation import MiddlewareMixin


class token(MiddlewareMixin):

    def process_request(self, request):
        print("请求之前调用")

    def process_response(self, request, response):
        print("响应之前调用")
        return response