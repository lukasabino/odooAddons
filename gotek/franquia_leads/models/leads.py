from odoo import fields, models

class ViabilidadeDados(models.Model):
    _name = "franquia.leads"

    CNPJ = fields.Integer(string="CNPJ")
    NOME_EMPRESARIAL= fields.Char(string="Razao Social")
    LOGRADOURO = fields.Char(string="Logradouro")
    COMPLEMENTO = fields.Char(string="Complemento")
    NUMERO = fields.Char(string="Complemento")
    BAIRRO = fields.Char(string="Bairro")
    MUNICIPIO = fields.Char(string="Municipio")
    UF = fields.Char(string="UF")
    CEP = fields.Integer(string="CEP")
    TELEFONE = fields.Char(string="Telefone")
    EMAIL = fields.Char(string="Email")