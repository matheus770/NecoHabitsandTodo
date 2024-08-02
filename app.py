import random
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import Habit, db
from utils import *
from sqlalchemy import text

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# with app.app_context():
#     db.create_all()
#     print("Tabelas criadas")
    
# with app.app_context():
#     db.session.execute(text('ALTER TABLE habits ALTER COLUMN name TYPE VARCHAR(255);'))
#     db.session.execute(text('ALTER TABLE habits ALTER COLUMN category TYPE VARCHAR(255);'))
#     db.session.commit()
#     print("Colunas alteradas")
    
@app.route('/')
def index():
    data_info_dict = obtem_dias_mes_atual()
    qtd_dias_mes = data_info_dict['dias_mes']
    nome_mes = data_info_dict['nome_mes']
    levels = [random.randint(0, 4) for _ in range(qtd_dias_mes)]
    
    habitos = Habit.query.all()
    return render_template('habits.html',habitos=habitos,num_dias_mes=qtd_dias_mes, levels=levels,nome_mes=nome_mes)
    
@app.route('/add_habit', methods=['POST'])
def add_habit():
    name = request.form.get('name')
    category = request.form.get('category')

    new_habit = Habit(name=name, category=category)
    db.session.add(new_habit)
    db.session.commit()

    return redirect(url_for('index'))
    
    

if __name__ == '__main__':
    app.run(debug=True)
