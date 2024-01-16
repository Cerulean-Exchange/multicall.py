import os
from enum import IntEnum
from typing import Dict

from aiohttp import ClientTimeout

# If brownie is installed and connected, we will use brownie's Web3
# Otherwise, we will use w3 from web3py.
try:
    from brownie import network, web3  # type: ignore

    if network.is_connected():
        w3 = web3
    else:
        from web3.auto import w3
except ImportError:
    from web3.auto import w3

GAS_LIMIT: int = int(os.environ.get("GAS_LIMIT", 50_000_000))

MULTICALL2_BYTECODE = "0x608060405234801561001057600080fd5b50600436106100b45760003560e01c806372425d9d1161007157806372425d9d1461013d57806386d516e814610145578063a8b0574e1461014d578063bce38bd714610162578063c3077fa914610182578063ee82ac5e14610195576100b4565b80630f28c97d146100b9578063252dba42146100d757806327e86d6e146100f8578063399542e91461010057806342cbb15c146101225780634d2301cc1461012a575b600080fd5b6100c16101a8565b6040516100ce919061083b565b60405180910390f35b6100ea6100e53660046106bb565b6101ac565b6040516100ce9291906108ba565b6100c1610340565b61011361010e3660046106f6565b610353565b6040516100ce93929190610922565b6100c161036b565b6100c161013836600461069a565b61036f565b6100c161037c565b6100c1610380565b610155610384565b6040516100ce9190610814565b6101756101703660046106f6565b610388565b6040516100ce9190610828565b6101136101903660046106bb565b610533565b6100c16101a3366004610748565b610550565b4290565b8051439060609067ffffffffffffffff8111156101d957634e487b7160e01b600052604160045260246000fd5b60405190808252806020026020018201604052801561020c57816020015b60608152602001906001900390816101f75790505b50905060005b835181101561033a5760008085838151811061023e57634e487b7160e01b600052603260045260246000fd5b6020026020010151600001516001600160a01b031686848151811061027357634e487b7160e01b600052603260045260246000fd5b60200260200101516020015160405161028c91906107f8565b6000604051808303816000865af19150503d80600081146102c9576040519150601f19603f3d011682016040523d82523d6000602084013e6102ce565b606091505b5091509150816102f95760405162461bcd60e51b81526004016102f090610885565b60405180910390fd5b8084848151811061031a57634e487b7160e01b600052603260045260246000fd5b602002602001018190525050508080610332906109c2565b915050610212565b50915091565b600061034d60014361097b565b40905090565b43804060606103628585610388565b90509250925092565b4390565b6001600160a01b03163190565b4490565b4590565b4190565b6060815167ffffffffffffffff8111156103b257634e487b7160e01b600052604160045260246000fd5b6040519080825280602002602001820160405280156103eb57816020015b6103d8610554565b8152602001906001900390816103d05790505b50905060005b825181101561052c5760008084838151811061041d57634e487b7160e01b600052603260045260246000fd5b6020026020010151600001516001600160a01b031685848151811061045257634e487b7160e01b600052603260045260246000fd5b60200260200101516020015160405161046b91906107f8565b6000604051808303816000865af19150503d80600081146104a8576040519150601f19603f3d011682016040523d82523d6000602084013e6104ad565b606091505b509150915085156104d557816104d55760405162461bcd60e51b81526004016102f090610844565b604051806040016040528083151581526020018281525084848151811061050c57634e487b7160e01b600052603260045260246000fd5b602002602001018190525050508080610524906109c2565b9150506103f1565b5092915050565b6000806060610543600185610353565b9196909550909350915050565b4090565b60408051808201909152600081526060602082015290565b80356001600160a01b038116811461058357600080fd5b919050565b600082601f830112610598578081fd5b8135602067ffffffffffffffff808311156105b5576105b56109f3565b6105c2828385020161094a565b83815282810190868401865b8681101561068c57813589016040601f198181848f030112156105ef578a8bfd5b6105f88261094a565b6106038a850161056c565b81528284013589811115610615578c8dfd5b8085019450508d603f850112610629578b8cfd5b898401358981111561063d5761063d6109f3565b61064d8b84601f8401160161094a565b92508083528e84828701011115610662578c8dfd5b808486018c85013782018a018c9052808a01919091528652505092850192908501906001016105ce565b509098975050505050505050565b6000602082840312156106ab578081fd5b6106b48261056c565b9392505050565b6000602082840312156106cc578081fd5b813567ffffffffffffffff8111156106e2578182fd5b6106ee84828501610588565b949350505050565b60008060408385031215610708578081fd5b82358015158114610717578182fd5b9150602083013567ffffffffffffffff811115610732578182fd5b61073e85828601610588565b9150509250929050565b600060208284031215610759578081fd5b5035919050565b60008282518085526020808601955080818302840101818601855b848110156107bf57858303601f19018952815180511515845284015160408585018190526107ab818601836107cc565b9a86019a945050509083019060010161077b565b5090979650505050505050565b600081518084526107e4816020860160208601610992565b601f01601f19169290920160200192915050565b6000825161080a818460208701610992565b9190910192915050565b6001600160a01b0391909116815260200190565b6000602082526106b46020830184610760565b90815260200190565b60208082526021908201527f4d756c746963616c6c32206167677265676174653a2063616c6c206661696c656040820152601960fa1b606082015260800190565b6020808252818101527f4d756c746963616c6c206167677265676174653a2063616c6c206661696c6564604082015260600190565b600060408201848352602060408185015281855180845260608601915060608382028701019350828701855b8281101561091457605f198887030184526109028683516107cc565b955092840192908401906001016108e6565b509398975050505050505050565b6000848252836020830152606060408301526109416060830184610760565b95945050505050565b604051601f8201601f1916810167ffffffffffffffff81118282101715610973576109736109f3565b604052919050565b60008282101561098d5761098d6109dd565b500390565b60005b838110156109ad578181015183820152602001610995565b838111156109bc576000848401525b50505050565b60006000198214156109d6576109d66109dd565b5060010190565b634e487b7160e01b600052601160045260246000fd5b634e487b7160e01b600052604160045260246000fdfea2646970667358221220c1152f751f29ece4d7bce5287ceafc8a153de9c2c633e3f21943a87d845bd83064736f6c63430008010033"


class Network(IntEnum):
    Mainnet = 1
    Kovan = 42
    Rinkeby = 4
    Görli = 5
    Gnosis = 100
    Polygon = 137
    Bsc = 56
    Fantom = 250
    Heco = 128
    Harmony = 1666600000
    Arbitrum = 42161
    Avax = 43114
    Moonriver = 1285
    Aurora = 1313161554
    Cronos = 25
    Optimism = 10
    OptimismKovan = 69
    Kava = 2222
    KavaTestnet = 2221
    Neon = 245022934
    NeonTestnet = 245022926


MULTICALL_ADDRESSES: Dict[int, str] = {
    Network.Mainnet: "0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441",
    Network.Kovan: "0x2cc8688C5f75E365aaEEb4ea8D6a480405A48D2A",
    Network.Rinkeby: "0x42Ad527de7d4e9d9d011aC45B31D8551f8Fe9821",
    Network.Görli: "0x77dCa2C955b15e9dE4dbBCf1246B4B85b651e50e",
    Network.Gnosis: "0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a",
    Network.Polygon: "0x95028E5B8a734bb7E2071F96De89BABe75be9C8E",
    Network.Bsc: "0x1Ee38d535d541c55C9dae27B12edf090C608E6Fb",
    Network.Fantom: "0xb828C456600857abd4ed6C32FAcc607bD0464F4F",
    Network.Heco: "0xc9a9F768ebD123A00B52e7A0E590df2e9E998707",
    Network.Harmony: "0xFE4980f62D708c2A84D3929859Ea226340759320",
    Network.Cronos: "0x5e954f5972EC6BFc7dECd75779F10d848230345F",
    Network.Optimism: "0x187C0F98FEF80E87880Db50241D40551eDd027Bf",
    Network.OptimismKovan: "0x2DC0E2aa608532Da689e89e237dF582B783E552C",
    Network.Kava: "0x7ED7bBd8C454a1B0D9EdD939c45a81A03c20131C",
    Network.KavaTestnet: "0x1Af096bFA8e495c2F5Eeb56141E7E2420066Cf78",
    Network.Neon: "",
    Network.NeonTestnet: "0x60B59FFA8d66910db6B68F90eBd44f32c976Ff10",
}

MULTICALL2_ADDRESSES: Dict[int, str] = {
    Network.Mainnet: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Kovan: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Rinkeby: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Görli: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Gnosis: "0x9903f30c1469d8A2f415D4E8184C93BD26992573",
    Network.Polygon: "0xc8E51042792d7405184DfCa245F2d27B94D013b6",
    Network.Bsc: "0xfF6FD90A470Aaa0c1B8A54681746b07AcdFedc9B",
    Network.Fantom: "0xBAD2B082e2212DE4B065F636CA4e5e0717623d18",
    Network.Moonriver: "0xB44a9B6905aF7c801311e8F4E76932ee959c663C",
    Network.Arbitrum: "0x842eC2c7D803033Edf55E478F461FC547Bc54EB2",
    Network.Avax: "0xdf2122931FEb939FB8Cf4e67Ea752D1125e18858",
    Network.Heco: "0xd1F3BE686D64e1EA33fcF64980b65847aA43D79C",
    Network.Aurora: "0xe0e3887b158F7F9c80c835a61ED809389BC08d1b",
    Network.Cronos: "0x5e954f5972EC6BFc7dECd75779F10d848230345F",
    Network.Optimism: "0x2DC0E2aa608532Da689e89e237dF582B783E552C",
    Network.OptimismKovan: "0x2DC0E2aa608532Da689e89e237dF582B783E552C",
    Network.Kava: "0x30A62aA52Fa099C4B227869EB6aeaDEda054d121",
    Network.Neon: "",
    Network.NeonTestnet: "0xcFC8002c27985410F7a5Df76f418E5F1a460e1eb",
}

# With default AsyncBaseProvider settings, some dense calls will fail
#   due to aiohttp.TimeoutError where they would otherwise succeed.
AIOHTTP_TIMEOUT = ClientTimeout(int(os.environ.get("AIOHTTP_TIMEOUT", 30)))

# Parallelism
user_choice = max(1, int(os.environ.get("MULTICALL_PROCESSES", 1)))
parallelism_capacity = max(1, os.cpu_count() - 1)
NUM_PROCESSES = min(user_choice, parallelism_capacity)
