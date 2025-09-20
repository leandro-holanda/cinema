from django.db import models

NACIONALITY_CHOICES = [
    ('AF', 'Afeganistão'),
    ('AR', 'Argentina'),
    ('AU', 'Austrália'),
    ('BE', 'Bélgica'),
    ('BR', 'Brasil'),
    ('CA', 'Canadá'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CO', 'Colômbia'),
    ('DE', 'Alemanha'),
    ('DK', 'Dinamarca'),
    ('EG', 'Egito'),
    ('ES', 'Espanha'),
    ('FR', 'França'),
    ('GR', 'Grécia'),
    ('IN', 'Índia'),
    ('IT', 'Itália'),
    ('JP', 'Japão'),
    ('KR', 'Coreia do Sul'),
    ('MX', 'México'),
    ('NG', 'Nigéria'),
    ('NL', 'Holanda'),
    ('PT', 'Portugal'),
    ('RU', 'Rússia'),
    ('SE', 'Suécia'),
    ('TR', 'Turquia'),
    ('UK', 'Reino Unido'),
    ('UA', 'Ucrânia'),
    ('US', 'Estados Unidos'),
    ('ZA', 'África do Sul'),
]

class Actor(models.Model):
    name = models.CharField(max_length=250)
    birthday = models.DateField()
    nacionality = models.CharField(choices=NACIONALITY_CHOICES, max_length=2)


    def __str__(self):
        return self.name