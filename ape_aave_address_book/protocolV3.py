from ape.api import Address
from ape.types import RawAddress
from ape import Contract

class PoolV3Addresses:

    def __init__(
            self,
            pool_addresses_provider: RawAddress,
            pool: RawAddress | None = None,
            #pool_impl: AddressType | None = None,
            #aave_protocol_data_provider: AddressType | None = None,
            pool_configurator: RawAddress | None = None,
            #pool_configurator_impl: AddressType | None = None,
            oracle: RawAddress | None = None,
            price_oracle_sentinel: RawAddress | None = None,
            acl_admin: RawAddress | None = None,
            acl_manager: RawAddress | None = None,
            #collector: AddressType | None = None,
            #emission_manager: AddressType | None = None,
            #default_incentives_controller: AddressType | None = None,
            #[key: `default_a_token_impl_rev_${number}`]: AddressType | None = None,
            #[key: `default_variable_debt_token_impl_rev_${number}`]: AddressType | None = None,
            #reservesData: ReserveData[] | None = None,
            #externalLibraries: null | Record<string, AddressInfo> | None = None,
            ) -> None:
        self.pool_addresses_provider = Address(pool_addresses_provider)
        c = Contract(self.pool_addresses_provider)
        self.pool = Address(c.getPool() if pool is None else pool)
        self.pool_configurator = Address(c.getPoolConfigurator() if pool_configurator is None else pool_configurator)
        self.oracle = Address(c.getPriceOracle() if oracle is None else oracle)
        self.price_oracle_sentinel = Address(c.getPriceOracleSentinel() if price_oracle_sentinel is None else price_oracle_sentinel)
        self.acl_admin = Address(c.getACLAdmin() if acl_admin is None else acl_admin)
        self.acl_manager = Address(c.getACLManager() if acl_manager is None else acl_manager)

    def replicate(self) -> str:
        return f"""
PoolV3Addresses(
    pool_addresses_provider="{self.pool_addresses_provider}",
    pool="{self.pool}",
    pool_configurator="{self.pool_configurator}",
    oracle="{self.oracle}",
    price_oracle_sentinel="{self.price_oracle_sentinel}",
    acl_admin="{self.acl_admin}",
    acl_manager="{self.acl_manager}",
    )"""
