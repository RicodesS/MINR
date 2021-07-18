class Transaction:
	# the attribute _data is in a json format
	_data = None

	# 1. the constructor function
	def __init__(self, data):
        	self._data = data
		self._data["Timestamp"] = str(datetime.datetime.now())
		self._data["hash"] = self.digest()

	# 2. there should be two different digest functions for hashing a transaction. 
	# 2.1. this function returns a hash to be signed on. It is the hash of the fields "type", "coins_consumed", "coins_created" and "transaction fee" for "PayCoins" and "type" and "coins_created" for "CoinsBase"
	def digest_sign(self):

		# write your code here

	# 2.2. this function returns the hash of all fields
	def digest(self):

		# write your code here

    	# 3. this function signs on a transaction by a given private key (or an alias that names to a private key file, which may require a password to open). Note that, after signing, the signature is appended to the field "signatures" of the attribute _data. 
    	def sign(self, private_key):
	# or def sign(self, alias, password):

		# write your code here

	# 4. this function verifies whether the signature of a transaction, which is in the "signatures" field is valid with a given public key (or an alias that names for a public key file)
	def verify_sig(self, public_key):
	# or def verify_sig(self, alias):

		# write your code here

	# 5. this function returns the total amount of coins created in a transaction,
    	def get_sum_coin_created(self):

		# write your code here
      
	# 6. this function returns the value of a coin created
    	def get_value(self, num):

		# write your code here

	# 7. there may be other functions.

	# write your code for other functions here
     

class Block:    
	_prev_hash = bytearray(256)	
	_merkle_root = bytearray(256)
	_timestamp = None
        _nonce = 0
	_difficulty = 0
	_prev = None
	_data = []

	# 1. the constructor function
	def __init__ (self, data, nonce, difficulty, prev = None):
		self._prev_hash = prev.digest() if prev is not None else bytearray(256)
		self._merkle_root = construct_Merkletree(data)
        	self._nonce = nonce
		self._difficulty = difficulty
        	self._prev = prev
		self._data = data

        # 2. there should be two digest functions
	# 2.1. this function returns the hash of a block for the mining purpose. This hash is used to compare with the target in the proof of work algorithm. The data to be hashed includes _prev_hash, _nonce and _data. 
	def mining_digest(self):

		# write your code here

	# 2.2. this function returns the hash of a block. The data to be hashed includes all the attributes
	def digest(self):

		# write your code here

	# 3. this function returns the value of a coin created
	def get_value_coin (self, trans_hash, num):

		# write your code here

	# 4. there may be other functions
	
	# write your code for other functions here
	
class examcoin:
	_head = None
	_root_hash = bytearray(256)
	_diff = 10
	_maxNonce = 2 ** 32
	_target = 2 ** (256 - _diff)
	_pending_pool = {}
	_level = 0

	# 1. the constructor function.
	def __init__(self):
        	self._head = Block([], 0, 0, None)
		self._root_hash = self._head.digest()

	# 2. this function adds a new transaction to the pending pool.
	def add_transaction(self, trans):

		# write your code here.

	# 3. this function adds a new block to the chain. Note that this block need to contain a transaction that awards 20 coins to the minier. When a new block is added, the attribute _level should be increased by 1 and all the transactions that are included in this block should be removed from the pending pool.
	def __add_block(self, block, minier):
		json = {"hash": 0,
			"type": "CoinsBase",
 			"coins_created": [{"num": 0, "value": 20, "recipient": minier}],
			"Timestamp": ""}
		award = Transaction(json)	
		block._data.append(award)
	
		# write your code here.

	# 3.1. this function removes all selected transactions from the pending pool.
	def __filtering_pending_pool(self, selected_trans):

		# write your code here.

	# 4. this function checks whether a given transaction is valid.
    	def verify_trans(self, trans):

		# write your code here.
	
	# there are some functions that are useful to validate a transaction.
	# 4. 1. this function returns the owner of a coin,
	def get_coin_owner(self, trans_hash, num):
        		
		# write your code here.

	# 4.2. this functions checks whether the coins consumed in a transaction are double spending.
    	def check_double_spending(self, coins_consumed):

		# write the code here.
      	
	# 5. this function validates whether a given block is valid.
	def verify_block(self, block):	
		# check the validation of the mining, the merkel tree root and all the transactions.
		
		# write your code here.

	# 6. this functions checks whether the chain is valid.
	def verify_chain(self):

		# write your code here.

	# 7. this function collects all valid transactions from the pending pool.
	def collect_valid_trans(self, pending_pool):

		# write your code here.	

	# 8. given an array of valid transactions: 
	# 8.1. this function returns an array of maximum 10 valid transactions sorted by transaction fee.
	def sort_trans_by_fee(self, valid_trans):

		# write your code here.

	# 8.2. this function returns an array of maximum 10 valid transactions sorted by timestamp.
	def sort_trans_by_timstamp(self, valid_trans):

		# write your code here.

	# 8.3. this function returns an array of maximum 10 valid transactions randomly.
	def sort_trans_by_random(self, valid_trans):

		# write your code here.	

        # 9. this function mines a new block. The arguments are the public key (or alias), the ming method that could be "fee",  "timestamp" or "random" and the block that the new block want to append after (as default, it is the current head of the chain).
	def mine(self, alias, method = "fee", head = None):
		# the mining strategy is the proof of work algorithm as in Bitcoin. The nonce, difficulty (target) are used for mining. Note that the difficulty increases 20% after each cycle of 10 blocks created. The attribute _level could be used for this purpose.

		# write your code here.

	# 10. this function returns the balance of an account (public key or alias). The balance of an account is the value of its unspent coins.
	def get_balance(self, public_key):
		# or def get_balance(self, alias):

		# write your code here.

	# 11. this function performs a transfer that transfers the amount "amount" of coins from an account "from_addr" (private_key or alias) to another account "to_adrr" (public key or alias) with the transaction fee "fee".
	def transfer(self, amount, fee, from_addr, to_addr):
	# or def transfer(self, amount, fee, from_addr, to_addr, password):
		# the function need to find the unspent coins of "from_addr" account, which could be one coin or more such that the sum of their values are equal or greater than "amount" plus "fee".
		# the transfer is fail if the balance of the account "from_addr" is too low.
		# if the transfer is successful, the transaction is added to the pending pool.

		# write your code here.

	# 12. there may be other functions.

	# write your code for other functions here.


