import pytest
import ape_test
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from  ape_aave_address_book.protocolV3 import PoolV3Addresses

def test_V3(networks):
    with networks.ethereum.mainnet.use_provider("node"):
        address_book = PoolV3Addresses("0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e")
        print(address_book.replicate())
        b = eval(address_book.replicate())
        print(b.replicate())
        assert address_book.replicate() == b.replicate()
