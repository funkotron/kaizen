class NoIfModifiedSinceMiddleware(object):
    def process_request(self, request):
        request.META.pop('HTTP_IF_MODIFIED_SINCE', None)