def application(environ, start_response):
    query = environ['QUERY_STRING']
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    result = []
    if query is not None:
        if query.find('&') >= 0:
            result = [x + '\n' for x in query.split('&')]
        else:
            result.append(query + '\n')
    start_response(status, headers)
    return result

