from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField,FileField
from flask_wtf.file import FileAllowed,FileRequired,DataRequired

class ReviewForm(FlaskForm):
    name = StringField('Название',validators=[DataRequired(message='Поле не должно быть пустым')],)
    text = TextAreaField('Отзыв',validators=[DataRequired(message='Поле не должно быть пустым')])
    score = SelectField('Ваша оценка для фильма',validators=[DataRequired(message='Поле не должно быть пустым')], choices=[i for i in range(1,11)])
    submit = SubmitField("Отправить отзыв")

class MovieForm(FlaskForm):
    title = StringField('Название фильма',validators=[DataRequired(message='Поле не должно быть пустым')])
    description = TextAreaField('Описание фильма',validators=[DataRequired(message='Поле не должно быть пустым')])
    image = FileField('Прикрепите афишу фильма',validators=[DataRequired(message='Поле не должно быть пустым'),FileAllowed(['jpg','jpeg','png'],message="Неверный формат файла")] )
    submit = SubmitField('Отправить фильм')