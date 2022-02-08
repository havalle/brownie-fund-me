from brownie import FundMe
from scripts.scripts import get_account, get_publish_source, get_price_feed_address


def deploy_fund_me():
    account = get_account()
    price_feed_address = get_price_feed_address()

    # Deploy contract
    fund_me = FundMe.deploy(
        price_feed_address, {"from": account}, publish_source=get_publish_source()
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
