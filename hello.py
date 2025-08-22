from flask import Flask, request

app = Flask(__name__)

# "Base de datos" en memoria (lista de usuarios)
usuarios = ["Andres", "Maria"]

# GET -> ver usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return str(usuarios)

# POST -> agregar usuario
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    nombre = request.form.get("nombre")  # recibe desde un formulario o Postman
    usuarios.append(nombre)
    return f"Usuario {nombre} agregado!"

# PUT -> actualizar usuario
@app.route("/usuarios/<int:pos>", methods=["PUT"])
def actualizar_usuario(pos):
    nuevo_nombre = request.form.get("nombre")
    if 0 <= pos < len(usuarios):
        usuarios[pos] = nuevo_nombre
        return f"Usuario en posición {pos} actualizado a {nuevo_nombre}"
    return "Usuario no encontrado"

# DELETE -> eliminar usuario
@app.route("/usuarios/<int:pos>", methods=["DELETE"])
def eliminar_usuario(pos):
    if 0 <= pos < len(usuarios):
        eliminado = usuarios.pop(pos)
        return f"Usuario {eliminado} eliminado!"
    return "Usuario no encontrado"


if __name__ == "__main__":
    app.run(debug=True)
