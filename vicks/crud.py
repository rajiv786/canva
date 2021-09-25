
class vicks:
    def __init__(self, link = 'https://chatting-c937e-default-rtdb.firebaseio.com/'):

        self.link = link
        from vicksbase import firebase as f
        self.firebase_obj = f.FirebaseApplication(self.link, None)

    def pull(self, child = None):
        result = self.firebase_obj.get(f'{child}', None)
        return result

    def push(self, data = None, child = None):
        # self.firebase_obj.put('/', child, data)
        self.firebase_obj.post(child, data)
