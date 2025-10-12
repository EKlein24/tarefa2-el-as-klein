#!/usr/bin/env python3
import random

try:
    from faker import Faker
except ImportError as e:
    raise SystemExit(
        "O paquete 'faker' non está instalado. Instálao con 'pip install Faker' antes de executar este programa."
    ) from e


def crear_usuarios(num_usuarios: int = 15, locale: str = "es_ES") -> dict[int, dict[str, str]]:
    """Crea un dicionario con datos ficticios de usuarios.

    Args:
        num_usuarios: Número total de usuarios a xerar.
        locale: Localización de Faker para xerar datos (por defecto 'es_ES').

    Returns:
        Un dicionario onde as claves son números consecutivos desde 1
        ata `num_usuarios` e os valores son dicionarios cos datos de
        cada usuario.
    """
    faker = Faker(locale)
    usuarios: dict[int, dict[str, str]] = {}
    for codigo in range(1, num_usuarios + 1):
        usuarios[codigo] = {
            "nome": faker.name(),
            "direccion": faker.address().replace("\n", ", "),
            "correo": faker.email(),
            "telefono": faker.phone_number(),
        }
    return usuarios


def mostrar_usuarios(usuarios: dict[int, dict[str, str]]) -> None:
    """Mostra por pantalla os datos de todos os usuarios.

    Args:
        usuarios: Dicionario cos datos de usuarios a mostrar.
    """
    print("Datos dos usuarios xerados:")
    print("-" * 40)
    for codigo, datos in usuarios.items():
        print(f"Código: {codigo}")
        print(f"  Nome: {datos['nome']}")
        print(f"  Dirección: {datos['direccion']}")
        print(f"  Correo electrónico: {datos['correo']}")
        print(f"  Teléfono: {datos['telefono']}")
        print("-" * 40)


def escoller_gañador(usuarios: dict[int, dict[str, str]]) -> tuple[int, dict[str, str]]:
    """Selecciona aleatoriamente a un usuario e devolve o seu código e datos.

    Args:
        usuarios: Dicionario de usuarios entre os que elixir.

    Returns:
        Unha tupla co código do usuario gañador e o seu dicionario de datos.
    """
    codigo_gañador = random.choice(list(usuarios.keys()))
    return codigo_gañador, usuarios[codigo_gañador]


def main() -> None:
    # Crear usuarios ficticios
    usuarios = crear_usuarios()
    # Mostrar todos os usuarios
    mostrar_usuarios(usuarios)
    # Seleccionar un gañador
    codigo_gañador, datos_gañador = escoller_gañador(usuarios)
    # Anunciar o gañador
    print(f"O usuario chamado {datos_gañador['nome']} foi o afortunado!")


if __name__ == "__main__":
    main()