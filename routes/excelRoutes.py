from flask import Blueprint, request, jsonify
from services.chatgptService import chat_with_gpt
from services.excelService import create_excel

excel_blueprint = Blueprint('excel', __name__)

@excel_blueprint.route('/generate_excel', methods=['POST'])
def generate_excel():
    # Obtener el prompt del cliente
    prompt = request.json.get("prompt", "")
    gpt_response = chat_with_gpt(prompt)

    # Procesar respuesta en filas
    rows = [line.split(", ") for line in gpt_response.split("\n")]

    # Crear Excel
    filename = "reporte.xlsx"
    create_excel(rows, filename)

    return jsonify({"message": "Archivo Excel creado exitosamente.", "filename": filename})