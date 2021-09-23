def helo(environ, start_response):
    status='200 OK'
    response_headers=[('Contect-type', 'text/plain; charset=utf-8')]
    start_response(status, response_headers)
    text="\r\n".join(environ["QUERY_STRING"].split("&")).encode("utf-8")
    return [text]
