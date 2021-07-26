import requests
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    city = StringField('City Name:')
    submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
    city = False
    form = InfoForm()
    if form.validate_on_submit():
        # city = form.city.data
         # # Reset the form's breed data to be False
        # form.city.data = ''
        api_url = f'https://api.openweathermap.org/data/2.5/weather?appid=32544a9752c598380e82439fb92a749c&q={city}'
        show_in_json_format = requests.get(api_url).json()
        weather_desc = show_in_json_format['weather'][0]['description']
        weather_temp = show_in_json_format['main']['temp']
    return render_template('index.html', city=city, form=form, api_url=api_url,show_in_json_format=show_in_json_format, weather_desc=weather_desc, weather_temp=weather_temp )

if __name__ == '__main__':
    app.run(debug=True)






