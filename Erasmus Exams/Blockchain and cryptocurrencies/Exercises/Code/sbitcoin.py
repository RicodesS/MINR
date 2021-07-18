import hashlib
from crypto_key import generate_key
from crypto_key import sign
from crypto_key import verify_sig
from time import time, ctime
 
class Transaction:
    def __init__(self, data: dict) -> None:
        self._data = data
        self._data["Timestamp"] = ctime(time())
        self._data["hash"] = str(self.digest())
 
    def add_signature(self, alias: str, password: str):
        '''
            Adds the signature of alias to this transaction
        '''
        self._data["signatures"].append(
            sign(self.digest(), alias, password)
        )
 
    def digest(self):
        '''
            Hashes the contents of the transaction
        '''
        m = hashlib.sha256()
        if self._data["type"] == "PayCoins":
            m.update(bytes(str(self._data["type"]), "utf-8"))
            m.update(bytes(str(self._data["coins_consumed"]), "utf-8"))
            m.update(bytes(str(self._data["coins_created"]), "utf-8"))
            m.update(bytes(str(self._data["Timestamp"]), "utf-8"))
        else:
            m.update(bytes(str(self._data["type"]), "utf-8"))
            m.update(bytes(str(self._data["coins_created"]), "utf-8"))
            m.update(bytes(str(self._data["Timestamp"]), "utf-8"))
        return m.hexdigest()
 
 
    def get_output(self, coin_id: int):
        '''
            Gets an output of the transaction by index
            else returns zero
        '''
        for e in self._data["coins_created"]:
            if e["num"] == coin_id:
                return [e["value"], e["recipient"]]
        return 0
 
    def get_coins_consumed(self):
        '''
            Gets the txhash and num input of every coin consumed
        '''
        coin_list = self._data["coins_consumed"]
        arr = []
        for i in range (len(coin_list)):
            arr.append(
                [coin_list[i]["hash"], coin_list[i]["num"]]
            )
        return arr
 
    def get_sum_spent(self):
        '''
            Returns the sum of coins spent by this transaction
        '''
        sum = 0
        for e in self._data["coins_created"]:
            sum = sum + e["value"]
        return sum
 
    def is_signed_by(self, alias) -> bool:
        '''
            Checks if this transaction was signed by alias
        '''
        content = self.digest()
        for e in self._data["signatures"]:
            if verify_sig(content, e, alias):
                return True
        return False
 
 
class Block:
    def __init__(self, trans_list, prev = None):
        '''
            creates a block with data
        '''
        self._id = prev._id + 1 if prev is not None else 0
        self._trans_list = trans_list
        self._prev = prev
        self._prev_hash = prev.digest() if prev else bytearray(256)
        self._nonce = 0
        self._timestamp = ctime(time())
 
    def digest(self):
        m = hashlib.sha256()
        for tx in self._trans_list:
            m.update(bytes(tx.digest(), 'utf-8'))
        m.update(bytes(str(self._prev_hash), 'utf-8'))
        m.update(bytes(str(self._nonce), 'utf-8'))
        m.update(bytes(str(self._timestamp), 'utf-8'))
        return bytearray(m.hexdigest(), 'utf-8')
 
    def verify(self, root_hash):
        my_hash = self.digest()
        if (root_hash != my_hash):
            print("Hash does not verify for the block {}".format(
                str(my_hash)))
        return (root_hash == my_hash and
                (not self._prev or self._prev.verify(self._prev_hash)))
 
    def get_transaction(self, txhash):
        for tx in self._trans_list:
            if tx._data["hash"] == str(txhash):
                return tx
        return None
 
    def set_nonce(self, n: int):
        self._nonce = min(n, 2 ** 32)
 
    def mine(self, difficulty):
        for i in range(0, 2 ** 32):
            if int(self.digest(), 16) <= difficulty:
                print("nonce found")
                return
            self.set_nonce(i)
 
 
class SBitcoin:
    def __init__(self):
        self._root_hash = bytearray(256)
        self._head = None
        self._difficulty = 15
        self._target = 2 ** (256 - self._difficulty)
        self._pending_pool = []
 
    def register_transaction(self, trans):
        #trans._data["Timestamp"] = ctime(time())
        #if self.verify_transaction(trans):
        self._pending_pool.append(trans)
        #else:
        #    print("""Transaction wasnt added to the pending pool because its"""
        #          """not valid""")
 
    def collect_valid_trans(self):
        '''
            for the miner to collect all valid transactions and delete
            all invalid transactions from the pool
        '''
        self._pending_pool = list(filter(self.verify_transaction, self._pending_pool))
        return self._pending_pool
 
    def get_block_from_pending_pool(self, miners_name, coinbase_hash = False):
        # gives you a block to mine. coinbase_transaction is the transaction
        # where you send yourself coins
        txdata = {"hash": "",
                  "type": "BaseCoins",
                  "coins_created": [
                      {"num": 0, "value": 20, "recipient": miners_name}
                      ],
                  "Timestamp": ctime(time())}
        tx = Transaction(txdata)
        if coinbase_hash:
            print(tx._data["hash"])
        return Block([tx] + self.collect_valid_trans(), self._head)
 
    def add_Block_to_Blockchain(self, new_block):
        '''
            Adds a block to the blockchain if it is coinsidered valid
 
        '''
        if self.verify_new_Block(new_block):
            self._root_hash = new_block.digest()
            self._head = new_block
            for tx in new_block._trans_list:
                if tx._data["type"] == "PayCoins":
                    self._pending_pool.remove(tx)
        else:
            print("block wasnt added because not valid")
 
    def verify_blockchain(self):
        ''' verifies the chain hashes '''
        return not self._head or self._head.verify(self._root_hash)
 
    def find_transaction(self, txhash):
        block_ptr = self._head
        while block_ptr is not None:
            tx = block_ptr.get_transaction(txhash)
            if isinstance(tx, Transaction):
                return tx
            block_ptr = block_ptr._prev
        print("Transaction with id {} was not found".format(txhash))
        return None
 
    def check_double_spending(self, trans):
        # for pending_tx in self._pending_pool:
        #     if pending_tx is trans:
        #         break
        #     for input in trans._data["coins_consumed"]:
        #         if input in pending_tx._data["coins_consumed"]:
        #             return True
 
        block_ptr = self._head
        while block_ptr is not None:
            for tx in block_ptr._trans_list:
                if tx._data["type"] == "PayCoins":
                    for input in trans._data["coins_consumed"]:
                        if input in tx._data["coins_consumed"] and tx is not trans:
                            return True
 
            block_ptr = block_ptr._prev
        return False
 
    def verify_transaction(self, trans):
        if trans._data["type"] == "BaseCoins":
            if trans.get_sum_spent() <= 20:
                return True
            print("Reward is not correct")
            return False
        elif trans._data["type"] == "PayCoins":
            # all consumed coins are valid (exist) and gets prev owners
            sum_coins_available = 0
            coin_owners = []
            for input in trans._data["coins_consumed"]:
                corresponding_trans = self.find_transaction(
                    input["hash"])
                if corresponding_trans is None:
                    # print("Transaction referenced was not found")
                    return False
                corresponding_output = corresponding_trans.get_output(input["num"])
                if corresponding_output == 0:
                    print("Referenced output was not found")
                    return False
                sum_coins_available += corresponding_output[0]
                coin_owners.append(corresponding_output[1])
 
            # check double spending
            if self.check_double_spending(trans):
                print("You cannot double spend")
                return False
 
            # all coints created are valid
            sum_coins_spent = trans.get_sum_spent()
            if sum_coins_available < sum_coins_spent:
                print("You cannot spend more coins in a tx than available")
                return False
 
            # signatures are valid
            for owner in coin_owners:
                if not trans.is_signed_by(owner):
                    print("Transaction wa not signed by all owners")
                    return False
            return True
 
    def get_utxo(self, alias):
        utxo = dict()
        block_ptr = self._head
        while block_ptr is not None:
            for tx in block_ptr._trans_list:
                for out in tx._data["coins_created"]:
                    if out["recipient"] == alias:
                        if not utxo.get(tx._data["hash"], None):
                            utxo[tx._data["hash"]] = []
                        utxo[tx._data["hash"]].append(out)
            block_ptr = block_ptr._prev
        block_ptr = self._head
        while block_ptr is not None:
            for tx in block_ptr._trans_list:
                if tx._data["type"] == "PayCoins":
                    for con in tx._data["coins_consumed"]:
                        out = utxo.get(con["hash"], None)
                        if out:
                            for o in out:
                                if o["num"] == con["num"]:
                                    out.remove(o)
                                    if len(out) == 0:
                                        utxo.pop(con["hash"])
                                        break
            block_ptr = block_ptr._prev
 
        return utxo
 
    def get_sum_balance(self, alias, verbose=False):
        balance =  sum(sum(k["value"] for k in v)
                       for k,v in self.get_utxo(alias).items())
        if verbose:
            print(alias, "currently has", str(balance), "coins!")
        return balance
 
    def verify_new_Block(self, my_block):
        '''
            check all transactions
            check nonce
            check if prev_hash == current root_hash
        '''
        return all([
            all([self.verify_transaction(tx) for tx in my_block._trans_list]),
            my_block._prev_hash == self._root_hash,
            int(my_block.digest(), 16) <= self._target
        ])