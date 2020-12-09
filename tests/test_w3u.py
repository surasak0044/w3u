from w3utils.w3utils import (
    token_info,
    get_abi,
    get_contract_src,
    get_transactions_by_account,
)


def test_erc20_address():
    assert token_info("DAI") == "0x6b175474e89094c44da98b954eedeac495271d0f"


def test_erc20_symbol():
    assert token_info("0x6b175474e89094c44da98b954eedeac495271d0f") == "DAI"


def test_erc20_dec():
    assert token_info("DAI", True) == 18


def test_get_transactions_by_account():
    assert (
        get_transactions_by_account("0x7fBaF24Be5Fb8eaefA5aDd9AF3F7052d3fF52E40") != 1
    )


def test_get_abi():
    assert get_abi("0x6b175474e89094c44da98b954eedeac495271d0f") != 1


def test_get_contract_src():
    assert get_contract_src("0x6b175474e89094c44da98b954eedeac495271d0f") != 1
