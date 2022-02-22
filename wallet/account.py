from hdwallet.hdwallet import BIP44HDWallet
from decouple import config

def create_account(currency: str, address_index: int = 0) -> dict:
    currency = currency.upper()

    if currency == "ETH_KOVAN":
        currency = "ETH"

    if currency not in ("BTC", "BTCTEST", "ETH"):
        raise ValueError("Unsupported currency")

    MNEMONIC = config("MNEMONIC_META_MASK", default=None)

    wallet = BIP44HDWallet(currency, address=address_index)
    wallet.clean_derivation()
    wallet.from_mnemonic(MNEMONIC)

    account = {
        "private_key": wallet.private_key(),
        "wif": wallet.wif(),
        "public_key": wallet.public_key(),
        "address": wallet.address(),
        "bip44_derivation_path": wallet.path(),
    }

    return account


__all__ = ["create_account"]
