import random
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import CategoryHabit, Habit, HabitCategories, HabitEntries, HabitEntry, db
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
    ano_atual = data_info_dict['ano_atual']
    mes_atual = data_info_dict['mes_atual']
    
    habitos = Habit.query.all() 
    
    habito_levels = {}
    
    for habito in habitos:
        levels = []
        for dia in range(1, qtd_dias_mes + 1):
            date = datetime(ano_atual, mes_atual, dia).date()
            entry = HabitEntry.query.join(HabitEntries).filter(
                HabitEntries.id_habit == habito.id,
                HabitEntry.date == date
            ).first()
            if entry and entry.status:
                levels.append(1)  
            else:
                levels.append(0) 
        habito_levels[habito.id] = levels
    
    return render_template('habits.html', habitos=habitos, num_dias_mes=qtd_dias_mes, habito_levels=habito_levels, nome_mes=nome_mes)
    
@app.route('/add_habit', methods=['POST'])
def add_habit():
    name = request.form.get('name')
    category = request.form.get('category')
    try:
        #* Verifica se já existe uma categoria com o mesmo nome
        existing_category = CategoryHabit.query.filter_by(name=category).first()
        
        if not existing_category:
            #* Se não existir, cria uma nova categoria
            new_category = CategoryHabit(name=category)
            db.session.add(new_category)
            db.session.commit()  # Commit para salvar a nova categoria

        #* Obtém a categoria existente ou recém-criada
        category = existing_category if existing_category else new_category
        
        #* Verifica se já existe um hábito com o mesmo nome
        existing_habit = Habit.query.filter_by(name=name).first()
        
        if not existing_habit:
            #* Se não existir, cria um novo hábito
            new_habit = Habit(name=name)
            db.session.add(new_habit)
            db.session.commit()  #* Commit para salvar o novo hábito

            #* Associa o hábito à categoria
            new_habit.categories.append(category)
            db.session.commit()  #* Commit para salvar a associação

        return redirect(url_for('index'))
    except Exception as e:
        print(f"Erro: {e}")
        return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True)
