import requests

# Requerimiento 1: Obtener toda la información de los usuarios
users_response = requests.get("https://reqres.in/api/users")
if users_response.status_code == 200:
    users_data = users_response.json()
    print("Información de los usuarios:")
    print(users_data)
else:
    print("Error al obtener la información de los usuarios. Código de respuesta:", users_response.status_code)

# Requerimiento 2: Crear un usuario llamado Ignacio con trabajo Profesor
new_user_data = {
    "name": "Ignacio",
    "job": "Profesor"
}
create_response = requests.post("https://reqres.in/api/users", json=new_user_data)
if create_response.status_code == 201:
    created_user = create_response.json()
    print("Usuario creado:")
    print(created_user)
else:
    print("Error al crear el usuario. Código de respuesta:", create_response.status_code)

# Requerimiento 3: Actualizar el usuario llamado morpheus con campo residence igual a zion
update_data = {
    "residence": "zion"
}
update_response = requests.put("https://reqres.in/api/users/2", json=update_data)  # Se asume que morpheus tiene id 2
if update_response.status_code == 200:
    updated_user = update_response.json()
    print("Usuario actualizado:")
    print(updated_user)
else:
    print("Error al actualizar el usuario. Código de respuesta:", update_response.status_code)

# Requerimiento 4: Eliminar el usuario llamado Tracey
delete_response = requests.delete("https://reqres.in/api/users/5")  # Se asume que Tracey tiene id 5
print("Código de respuesta al eliminar el usuario Tracey:", delete_response.status_code)
