from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='E-mail',max_length=255)
    assunto = forms.CharField(label='Assunto',max_length=255)
    mensagem = forms.CharField(label='Menssagem', widget= forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-Mail:{email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to= ['contato@seudominio.com',],
            headers={'reply-to': email},
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm):


    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']