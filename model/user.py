class user():

    #def __init__(self, id, picture, username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile, follower, following):
    def __init__(self, id, username, password, login_count, is_admin, is_active, profile,title):   
        self.id = id
        self.username = username
        self.password = password
        self.login_count = login_count
        self.is_admin = is_admin
        self.is_active = is_active
        self.profile = profile
        self.title = title
        # self.first_name = first_name
        # self.last_name = last_name
        # self.birthday = birthday
        # self.join_date = join_date
        # self.last_login = last_login
        # self.login_count = login_count
        # self.is_admin = is_admin
        # self.is_active = is_active
        # self.profile = profile
        # self.follower = follower
        # self.following = following
