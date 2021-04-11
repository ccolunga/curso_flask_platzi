from flask_login import UserMixin

from .firestore_service import get_user


class UserData:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password
        self.email = user_data.email

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        #print(f"- - -ID- - - {user_doc.id}")
        #print(f"- - -EMAIL- - - {user_doc.to_dict()['email']}")
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()['password'],
            email=user_doc.to_dict()['email']
        )
        # print(f'user_data.username')
        # print(f'user_data.password')
        return UserModel(user_data)
