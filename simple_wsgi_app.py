#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Save this code in a file, e.g., gunicorn_example.py

def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello, Gunicorn!"]

# This block is added for running Gunicorn
if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 8000), simple_wsgi_app)
    http_server.serve_forever()

