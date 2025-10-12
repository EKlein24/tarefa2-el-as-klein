# Tarefa 2: Xeración de usuarios con Faker

Este proxecto é unha resolución da tarefa onde se solicita desenvolver un programa que xere datos ficticios de 15 usuarios. Para iso utilízase a biblioteca **Faker** en Python.

## Requisitos

- Python 3.8 ou superior.
- Biblioteca [`Faker`](https://faker.readthedocs.io/), que se pode instalar executando:

```bash
pip install -r requirements.txt
```

## Estrutura do código

O ficheiro principal é **`main.py`**, que realiza as seguintes accións:

1. Xera 15 usuarios ficticios cun código único entre 1 e 15.
2. Almacena os datos (nome, dirección, correo electrónico e teléfono) nun dicionario.
3. Mostra por pantalla os datos de todos os usuarios xerados.
4. Elixe aleatoriamente a un dos usuarios e amosa unha mensaxe anunciando que foi o afortunado.

## Execución

1. **Crear un contorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
2. **Instalar as dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Executar o programa:**
   ```bash
   python main.py
   ```

## Uso de Git e GitHub

Esta solución está preparada para ser versionada con Git e aloxada nun repositorio público de GitHub. Algúns consellos:

- Realiza varios *commits* durante o desenvolvemento para amosar o progreso.
- Inclúe un ficheiro `.gitignore` (por exemplo, para ignorar o contorno virtual `venv/`).
- Cando remates, podes comprimir o contido do repositorio (agás o contorno virtual) nun ficheiro `.zip` co formato **`tarefa2_nome_apelidos.zip`** e subilo xunto coa URL do repositorio como se require na tarefa.

## Autor

Substitúe este apartado polo teu nome e apelidos.