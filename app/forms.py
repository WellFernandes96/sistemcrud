from django.forms import ModelForm
from app.models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['modelo', 'marca', 'preco' ]