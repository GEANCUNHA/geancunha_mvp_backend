from asyncio import tasks
import json
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable
from flask_restx import Api, Resource, fields, reqparse
from flask import Blueprint



app = Flask(__name__, template_folder='../geancunha_mvp_frontend/templates', static_folder='../geancunha_mvp_frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

tasks_blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')
tasks_namespace = Api(tasks_blueprint, title='Gean Cunha MVP API', description='API para gerenciar tarefas', default='Rotas para gerenciar as tarefas')


task_model = tasks_namespace.model('Task', {
    'id': fields.Integer,
    'description': fields.String,
    'responsavel': fields.String,
})




@tasks_namespace.route('/')
class TasksResource(Resource):
    @tasks_namespace.marshal_with(task_model, as_list=True)
    @tasks_namespace.doc(tags=['Tasks'])    
    @tasks_namespace.doc(responses={200: 'Redirect'})
    def get(self):
        """Lista todas as tarefas"""
        tasks = Task.query.all()
        return tasks
    
    @tasks_namespace.expect(task_model)
    @tasks_namespace.marshal_with(task_model)
    @tasks_namespace.doc(tags=['Tasks'])
    def post(self):
        """Adiciona uma nova tarefa"""
        new_task = Task(
            description=tasks_namespace.payload['description'],
            responsavel=tasks_namespace.payload['responsavel']
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201
    
    
  

    @tasks_namespace.doc(params={'task_id': 'ID da tarefa que será excluída'})
    @tasks_namespace.doc(description="Excluir uma tarefa pelo ID.")
    @tasks_namespace.doc(responses={200: 'Success', 404: 'Tarefa não encontrada'})
    @tasks_namespace.expect({'task_id': fields.Integer(required=True, description='ID da tarefa')})
    def delete(self):
        """
        Excluir uma tarefa pelo ID.
        """
        task_id = tasks_namespace.payload.get('task_id')
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'success': True, 'message': 'Tarefa excluída com sucesso'}, 200
        else:
            return {'success': False, 'message': 'Tarefa não encontrada'}, 404



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    responsavel = db.Column(db.String(200))


@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/gettasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'description': task.description, 'responsavel': task.responsavel} for task in tasks]
    return jsonify({'tasks': task_list})

@app.route('/addtasks', methods=['POST'])
def add_task():
      
         task_description = request.json.get('task')
         task_responsavel = request.json.get('responsavel')
         new_task = Task (description=task_description, responsavel=task_responsavel)
         db.session.add(new_task)
         db.session.commit()
         return jsonify({'success:': True, 'message': 'Tarefa adicionada com sucesso!'})
      
@app.route('/deletetask/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Tarefa excluída com sucesso!'})
    else:
        return jsonify({'success': False, 'message': 'Tarefa não encontrada'}), 404         



app.register_blueprint(tasks_blueprint)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)






