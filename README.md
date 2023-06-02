# API Documentation

## Users API

### Retrieve API Documentation

**URL**: `/users/docs/`

**Method**: GET

**Description**: Retrieves the API documentation for the Users API.

### Parameters

This endpoint does not require any parameters.

### Response

The response will be the API documentation in HTML format.

## Users Endpoints

### Retrieve a List of Users

**URL**: `/users/api/users/`

**Method**: GET

**Description**: Retrieves a list of all users.

#### Response

The response will be a JSON array containing user objects. Each user object will have the following fields:

- `id` (integer): The unique identifier of the user.
- `name` (string): The name of the user.
- `email` (string): The email address of the user.
- `password` (string): The password of the user.
- `phone` (string): The phone number of the user.
- `username` (string): The username of the user.
- `address` (string): The address of the user.
- `nationality` (string): The nationality of the user.
- `date_of_birth` (date): The date of birth of the user.
- `created_at` (datetime): The date and time when the user was created.
- `updated_at` (datetime): The date and time when the user was last updated.

Example Response:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "password": "********",
    "phone": "1234567890",
    "username": "john_doe",
    "address": "123 Main St",
    "nationality": "USA",
    "date_of_birth": "1990-01-01",
    "created_at": "2023-06-01T10:00:00Z",
    "updated_at": "2023-06-02T15:30:00Z"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "password": "********",
    "phone": "9876543210",
    "username": "jane_smith",
    "address": "456 Elm St",
    "nationality": "UK",
    "date_of_birth": "1995-03-15",
    "created_at": "2023-06-01T12:30:00Z",
    "updated_at": "2023-06-02T11:45:00Z"
  }
]
```

**URL**: `/users/api/users/`

**Method**: POST

**Description**: Creates a new user.

#### Request Body

The request body should be a JSON object containing the following fields:

- `name` (string): The name of the user.
- `email` (string): The email address of the user.
- `password` (string): The password of the user.
- `phone` (string): The phone number of the user.
- `username` (string): The username of the user.
- `address` (string): The address of the user.
- `nationality` (string): The nationality of the user.
- `date_of_birth` (date): The date of birth of the user.

Example Request Body:

```json
{
  "name": "New User",
  "email": "newuser@example.com",
  "password": "********",
  "phone": "9876543210",
  "username": "new_user",
  "address": "123 Main St",
  "nationality": "USA",
  "date_of_birth": "1990-01-01"
}
```

#### Response

La respuesta será un objeto JSON que contiene los detalles del usuario recién creado. El objeto de usuario tendrá los siguientes campos:

- `id` (entero): El identificador único del usuario.
- `name` (cadena): El nombre del usuario.
- `email` (cadena): La dirección de correo electrónico del usuario.
- `password` (cadena): La contraseña del usuario.
- `phone` (cadena): El número de teléfono del usuario.
- `username` (cadena): El nombre de usuario del usuario.
- `address` (cadena): La dirección del usuario.
- `nationality` (cadena): La nacionalidad del usuario.
- `date_of_birth` (fecha): La fecha de nacimiento del usuario.

Ejemplo de respuesta:

```json
{
  "id": 1,
  "name": "Nuevo Usuario",
  "email": "nuevousuario@example.com",
  "password": "********",
  "phone": "9876543210",
  "username": "nuevo_usuario",
  "address": "123 Calle Principal",
  "nationality": "USA",
  "date_of_birth": "1990-01-01"
}
```

**URL**: `/users/api/users/<id>/`

**Method**: GET

**Description**: Retrieves the details of a user.

#### Parameters

- `id` (integer): The unique identifier of the user.

#### Response

The response will be a JSON object containing the details of the user. The user object will have the following fields:

```json
{
  "id": 1,
  "name": "John Doe",
  ...
}
```

**URL**: `/users/api/users/<id>/`

**Method**: PUT

**Description**: Updates the details of a user.

#### Parameters

- `id` (integer): The unique identifier of the user.

#### Request Body

The request body should be a JSON object containing the following fields:

- `name` (string): The name of the user.

Example Request Body:

```json
{
  "name": "New Name"
}
```

#### Response

The response will be a JSON object containing the details of the user. The user object will have the following fields:

```json
{
  "id": 1,
  "name": "New Name",
  ...
}
```

**URL**: `/users/api/users/<id>/`

**Method**: DELETE

**Description**: Deletes a user.

#### Parameters

- `id` (integer): The unique identifier of the user.

#### Response

The response will be a JSON object containing the details of the user. The user object will have the following fields:

```json
{
  "id": 1,
  "name": "John Doe",
  ...
}
```
# django-rest-crud
