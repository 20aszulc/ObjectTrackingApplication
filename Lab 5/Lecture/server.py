from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_tp_response


'''Route Config'''
if __name__ == '__main__':
        with Configurator() as config:
            
        #We're using Jinja to template:
        config.include("pyramid_jinja2")
        config.add_jinja2_renderer(".html")


        #home route 
        config.add_route("get_home", "/")
        config.add_view(get_home, route_name="get_home")

        #REST Collegection Route
        config.add_route("get_actors", "factors")
        config.add_view(get_actors, route_name="get_actors", renderer="json")

        #REST instance route
        config.add_route("get_actor")
        config.add_view(get_actor, route_name="get_actor", renderer="json")

        #Map the static content
        config.add_static_view(name="/", path="./public", cache_max_age=3600)

        #Creat WSGI config
        app = config.make_wsgi_app()

server = make_server("0.0.0.0", 80, app)
print("web server on local hours")
server.serve_forever()