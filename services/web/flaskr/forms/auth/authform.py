from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from ...database.db import get_db

class FormRegister(FlaskForm):

    def validate_usuario(self, check_user):
        db=get_db()
        usuario=check_user.data
        query = ("SELECT * FROM user WHERE username= %s")
        db.execute(query,(usuario,))
        user = db.fetchone()
        if user:
            raise ValidationError("Usuário já existe! Tente outro nome de usuário.")

    def validate_email(self, check_email):
        db=get_db()
        email=check_email.data
        query = ("SELECT * FROM user WHERE email= %s")
        db.execute(query,(email,))
        mail = db.fetchone()
        if mail:
            raise ValidationError("E-mail já existe! Cadastre outro.")

    usuario = StringField(label="Nome do Usuário:", validators=[Length(min=2, max=100), DataRequired()])
    email = EmailField(label="E-mail:", validators=[Email(), DataRequired()])
    senha = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    cnfsenha = PasswordField(label="Confirme a senha:", validators=[EqualTo('senha'), DataRequired()])
    submit = SubmitField(label="Cadastrar")

class FormLogin(FlaskForm):
    usuario = StringField(label="Nome do Usuário:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:",validators=[DataRequired()])
    submit = SubmitField(label="Login")

class FormLostInfoemail(FlaskForm):
    def validate_email(self, check_email):
        db=get_db()
        mail=check_email.data
        query = ("SELECT * FROM user WHERE email = %s")
        db.execute(query,(mail,))
        usuario = db.fetchone()
        if usuario == None:
            raise ValidationError("E-mail não está cadastrado!")

    email = EmailField(label="E-mail:", validators=[Email(), DataRequired()])
    submit = SubmitField(label="Enviar")

class FormLostChangepass(FlaskForm):
    senha = PasswordField(validators=[Length(min=6), DataRequired()])
    cnfsenha = PasswordField(validators=[EqualTo('senha'), DataRequired()])
    submit = SubmitField(label="Confirma")

