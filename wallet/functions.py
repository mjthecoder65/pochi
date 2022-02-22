from .account import create_account


def get_private_key(currency: str, address_index: int) -> str:
    return create_account(currency, address_index)["private_key"]


def get_public_key(currency: str, address_index: int) -> str:
    return create_account(currency, address_index)["public"]


def get_address(currency: str, address_index: int) -> str:
    return create_account(currency, address_index)["address"]


def get_addresses(currency: str, count: int = 10) -> str:
    return [
        create_account(currency, address_index)["address"]
        for address_index in range(count)
    ]

def get_wif(currency: str, address_index: int) -> str:
    return create_account(currency, address_index)["wif"]


def get_derivatation(currency: str, address_index: int) -> str:
    return create_account(currency, address_index)["bip44_derivation_path"]


__all__ = ["get_addresses", "get_address", "get_private_key"]
