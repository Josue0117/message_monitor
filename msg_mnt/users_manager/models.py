from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    nick_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    user_age=models.IntegerField()

    ACADEMIC=1
    RS_USER=2
    VL_GROUP=3
    ROL = (
       (ACADEMIC, 'Academico'),
       (RS_USER, 'Usuario RS'),
       (VL_GROUP, 'Grupo vulnerable'),
    )
    user_rol=models.PositiveSmallIntegerField(choices=ROL,default=ACADEMIC,)

    MALE=1
    FEMALE=2
    OTHER=3
    GENDER = (
        (MALE, 'Hombre'),
        (FEMALE, 'Mujer'),
        (OTHER, 'Otro'),
    )
    user_gender=models.PositiveSmallIntegerField(choices=GENDER,default=FEMALE,)
