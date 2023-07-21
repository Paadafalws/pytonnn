from rest_framework import serializers
from clientes.models import Cliente
import re
from validate_docbr import CPF



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        # Remover caracteres não numéricos do CPF
        cpf_numerico = re.sub(r'\D', '', cpf)

        # Verificar se o CPF tem 11 dígitos
        if len(cpf_numerico) != 11:
            raise serializers.ValidationError("O CPF deve conter 11 dígitos.")

        # Instanciar a classe CPF da biblioteca validate_docbr
        cpf_validador = CPF()

        # Verificar se o CPF é válido usando a função validate()
        if not cpf_validador.validate(cpf_numerico):
            raise serializers.ValidationError("O CPF é inválido.")

        return cpf_numerico            


    def validate_nome(self, nome):
        # Validar se o nome contém apenas letras e espaços
        if not re.match("^[a-zA-Z ]*$", nome):
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return nome
    def validate_rg(self, rg):
    # Validar se o nome contém apenas letras e espaços
        if not re.match(r'^\d{9,}$', rg):
            raise serializers.ValidationError("O RG deve conter apenas números e ter no mínimo 9 dígitos.")
        return rg
    def validate_celular(self, celular):
    # Validar se o nome contém apenas letras e espaços
        if not re.match(r'^\d{11,}$', celular):
            raise serializers.ValidationError("numero de celular contem 11 digitos")
        return celular