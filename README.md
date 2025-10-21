cat > README.md << 'EOF'
# MiPrimerBlog_Ruiz
Proyecto **Django 5 (MVT)** estilo blog para la entrega de Coderhouse.

## Requisitos
- Python 3.12+
- Django 5.2.7
- (Opcional) Git y GitHub

## Instalación (local)
```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
