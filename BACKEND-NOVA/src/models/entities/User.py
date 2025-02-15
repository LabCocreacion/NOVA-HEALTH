from utils.DateFormat import DateFormat

class User():

    def __init__(self, id, name=None, lastname=None, email=None, identificacion=None, numberphone=None, address=None, creationdate=None, isactive=None, password=None, project=None, rol=None, instituto=None) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.identificacion = identificacion
        self.numberphone = numberphone
        self.address = address
        self.creationdate = creationdate
        self.isactive = isactive
        self.password = password
        self.project = project
        self.rol = rol
        self.instituto = instituto
    
    def to_JSON(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'lastname' : self.lastname,
            'email' : self.email,
            'identificacion' : self.identificacion,
            'numberphone' : self.numberphone,
            'address' : self.address,
            'creationdate' : DateFormat.convert_date(self.creationdate),
            'isactive' : self.isactive,
            'password' : self.password,
            'project' : self.project,
            'rol' : self.rol,
            'instituto' : self.instituto
        }
        