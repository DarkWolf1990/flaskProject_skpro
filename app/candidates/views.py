from flask import Blueprint, render_template
from .dao.candidates_dao import CandidateDAO

# Создаём блупринт
candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder='./templates')
