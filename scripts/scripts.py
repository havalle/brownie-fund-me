from brownie import accounts, config, network, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 200000000000

LOCAL_NETWORKS = ["development", "ganache-local"]
FORKED_NETWORKS = ["mainnet-fork-alchemyapi"]


def get_account():
    if (
        network.show_active() in LOCAL_NETWORKS
        or network.show_active() in FORKED_NETWORKS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_publish_source():
    return config["networks"][network.show_active()].get("verify")


def get_price_feed_address():
    if network.show_active() not in LOCAL_NETWORKS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print("Deploying Mocks ...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed ...")
        return MockV3Aggregator[-1].address
