
USERS = {}


class Users():
    '''class to represent users model'''

    def put(self, name, phone, user_id):
        '''add a user to USERS'''
        self.user = {}
        if user_id in USERS:
            return {"message": "User with the given ID already exists"}
        self.user["name"] = name
        self.user["phone"] = phone
        self.user["user_id"] = user_id

        USERS[user_id] = self.user

        return {"message": "user subscribed successfully"}

    def get_all_users(self):
        '''Get all users from the users dictionary'''
        return USERS

    def get_user_by_id(self, user_id):
        '''Gets a user by a given field'''

        if user_id in USERS:
            return USERS[user_id]

        return {"message": "user not found"}

    def delete_user(self, user_id):
        if user_id in USERS:
            del USERS[user_id]
            return {"message": "User{} unsubscribed successfully".format(user_id)}

        return {"message": "User doesn't exist"}
