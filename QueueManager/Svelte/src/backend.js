var { DateTime } = require('luxon');

// Clientes
const juana = {
    "id": 1,
    "name": "Juana de la Caridad",
    "cel": "54346723",
    "phone": "81234567",
    "fbid": "",
    "address": "Loma 345 % Bajando y Subiendo, La Marquesa."
}
const perdo = {
    "id": 2,
    "name": "Pero Ramón Hernández",
    "cel": "59676723",
    "phone": "",
    "fbid": "",
    "address": "Loma 345 % Bajando y Subiendo, La Marquesa."
}
const Estevan = {
    "id": 3,
    "name": "Estevan Rodríguez",
    "cel": "54343423",
    "phone": "81564567",
    "fbid": "",
    "address": "Martí 455 % Carr. central y Benavides, Guáimaro Norte."
}
const vladimir = {
    "id": 4,
    "name": "Vladímir Rodríguez",
    "cel": "54873173",
    "phone": "32248118",
    "fbid": "111459581238114",
    "address": "San Ramón 299 % San José y San Martín, Camagüey"
}

// Pedidos
const p1 = {
    "name": "Juana de la Caridad",
    "cel": "54346723",
    "phone": "81234567",
    "lts": 20,
    "created": DateTime.fromISO('2021-09-12T12:24:38.382447'),
    "address": "Loma 345 % Bajando y Subiendo, La Marquesa."
}
const p2 = {
    "name": "Pero Ramón Hernández",
    "cel": "59676723",
    "phone": "",
    "lts": 40,
    "created": DateTime.fromISO('2021-09-12T13:24:38.382447'),
    "address": "Loma 345 % Bajando y Subiendo, La Marquesa."
}
const p3 = {
    "name": "Estevan Rodríguez",
    "cel": "54343423",
    "phone": "81564567",
    "lts": 25,
    "created": DateTime.fromISO('2021-09-12T14:24:38.382447'),
    "address": "Martí 455 % Carr. central y Benavides, Guáimaro Norte."
}
const p4 = {
    "name": "Vladímir Rodríguez",
    "cel": "54873173",
    "phone": "32248118",
    "lts": 30,
    "created": DateTime.fromISO('2021-09-12T15:25:38.382447'),
    "address": "San Ramón 299 % San José y San Martín, Camagüey"
}

export const clientes = [juana, perdo, Estevan, vladimir]
export const pedidos = [p1, p2, p3, p4]