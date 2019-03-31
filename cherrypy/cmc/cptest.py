import cherrypy

class MyController:
    name = "default"

    def GET_INDEX(self):
        return "hello world! " + self.name

    def PUT_INDEX(self):
        msg = str(cherrypy.request.body.read())
        self.name = msg
        return "name is now: " + self.name

dispatcher = cherrypy.dispatch.RoutesDispatcher()

conf = { 'global': {'server.socket_host':'student04.cse.nd.edu',
                    'server.socket_port':51002},
          '/':{'request.dispatch':dispatcher}}

myController = MyController()

dispatcher.connect('hellow', '/helloworld/', controller=myController, action='GET_INDEX', conditions=dict(method=['GET']))

dispatcher.connect('hellowname', '/helloworld/', controller=myController, action='PUT_INDEX', conditions=dict(method=['PUT']))

cherrypy.config.update(conf)
app = cherrypy.tree.mount(None, config=conf)
cherrypy.quickstart(app)

