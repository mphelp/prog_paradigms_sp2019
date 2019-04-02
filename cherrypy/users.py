import cherrypy
import json

# Movies
class UsersController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_USERS(self):
        users = []
        for user_id in self.mdb.get_users():
            user = self.mdb.get_user(user_id)
            if user is not None: 
                users.append({
                    "gender": user[0],
                    "age": user[1],
                    "occupation": user[2],
                    "zipcode": user[3],
                    "result": "success",
                    "id": user_id
                })
        return json.dumps({
            "users": users,
            "result": "success"
        })

    def POST_USERS(self):
        user = json.loads(cherrypy.request.body.read(),
            encoding='latin-1')
        # Example format of user:
        # {
        #   'gender': 'F',
        #   'age': 13,
        #   'occupation': 1333,
        #   'zipcode': '5555-4444'
        # }
        try:
            new_user_id = max(self.mdb.get_users()) + 1
            self.mdb.set_user(new_user_id, [user['gender'], \
                user['age'], user['occupation'], user['zipcode']])
            return json.dumps({ "result": "success", "id": new_user_id })
        except Exception:
            return json.dumps({ "result": "error" })

    def DELETE_USERS(self):
        for user_id in self.mdb.get_users():
            try:
                self.mdb.delete_user(user_id)
            except KeyError:
                pass
        return json.dumps({ "result": "success" })

    def GET_USER(self, user_id):
        user_id = int(user_id)
        user = self.mdb.get_user(user_id)
        if user is None: 
            return json.dumps({ "result": "error" })
        else:
            return json.dumps({
                "gender": user[0],
                "age": user[1],
                "occupation": user[2],
                "zipcode": user[3],
                "result": "success",
                "id": user_id
            })


    def PUT_USER(self, user_id):
        user = json.loads(cherrypy.request.body.read(), \
            encoding='latin-1')
        print('inside of put user')
        #print(user)
        # Example format of user:
        # {
        #   'gender': 'F',
        #   'age': 13,
        #   'occupation': 1333,
        #   'zipcode': '5555-4444'
        # }
        #try:
        #    self.mdb.set_user(user_id, [user['gender'], \
        #        user['age'], user['occupation'], user['zipcode']])
        #    return json.dumps({ "result": "success" }) 
        #except Exception as e:
        #    print(str(e))
        #    return json.dumps({ 
        #       "result": "error",
        #       "msg": str(e)
        #    })
        self.mdb.set_user(user_id, [user['gender'], \
             user['age'], user['occupation'], user['zipcode']])
        return json.dumps({ "result": "success" })


    def DELETE_USER(self, user_id):
        try:
            self.mdb.delete_user(user_id)
            return json.dumps({ "result": "success" })
        except KeyError:
            return json.dumps({ "result": "error" })

