import pdfkit, uuid, os
from dotenv import load_dotenv
from flask import Blueprint, render_template, make_response,current_app
from ...mail.email import sendpdf 

load_dotenv()

bp = Blueprint('pdf',__name__)

@bp.route("/pdfcreate", methods=['GET','POST'])
def pdfcreate():
    filename = str(uuid.uuid4())+'.pdf'
#    config = pdfkit.configuration(wkhtmltopdf=current_app.config["DOWNLOAD_PATH"])
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    dados = {
        "responsavel" : "Paulo de Tarso",
        "email" : "ptarsoneves@yahoo.com.br",
        "qtpessoas" : 3,
        "check_in" : "10 de julho de 2023",
        "check_out" : "15 de julho de 2023",
        "tarifa" : 400.00,
        "valor" : 800.00,
        "valor_pago" : 400.00,
        "forma_pago" : "depósito em conta corrente",
        "saldo" : 400.00,
        "forma_saldo" : "depósito em conta corrente"
        }
    options = {
        'page-height': '97mm',
        'page-width': '210mm',
        'encoding': 'utf-8',
        'footer-left': current_app.config["NOME_FANTASIA"],
        'footer-font-size': 6,
        'footer-line': True,
        'header-line': True,
        'header-left': current_app.config["NOME_FANTASIA"]
    }
    html = render_template("pdf/pdf_template.html",dados=dados)
    pdfkit.from_string(html,filename,configuration=config, options=options)
    pdfDownload = open(filename, 'rb').read()
    subject=f"Olá Sr(a) " + dados['responsavel'] + "! Sua reserva está confirmada, obrigado(a). Segue em anexo o voucher"
    sendpdf(email=dados['email'],file=filename,subject=subject)
    os.remove(filename)
    response = make_response(pdfDownload)
    response.mimetype="application/pdf"
#    response.headers["Content-Type"] = "application/force-download"
#    response.headers["Content-Disposition"] = "attachment; filename="+filename
    response.headers["Content-Disposition"] = "inline; filename="+filename
    return response
    return render_template('home.html')

