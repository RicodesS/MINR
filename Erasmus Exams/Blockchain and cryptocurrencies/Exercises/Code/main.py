from sbitcoin import *
 
 
tx0 = {"hash": "db9ca9df899e7",
       "type": "BaseCoins",
       "coins_created": [
           {"num": 0, "value": 20, "recipient": "[Miner]"}
           ],
       "Timestamp": "2020-07-24 13:54:46.983531"}
 
tx1 = {"hash": "c821f7621208b",
       "type": "PayCoins",
       "coins_consumed": [
           {"hash": "db9ca9df899e7", "num": 0},
           {"hash": "772fe5688d766", "num": 2},
           {"hash": "8c9b6da77d6cb", "num": 1}
           ],
       "coins_created": [
           {"num": 0, "value": 3.2, "recipient": "alice"},
           {"num": 1, "value": 1.4, "recipient": "bob"},
           {"num": 2, "value": 7.5, "recipient": "caleb"}
           ],
       "signatures" : [],
       "Timestamp": "2020-07-24 14:34:26.653531"}
 
 
trans0 = Transaction(tx0)
trans1 = Transaction(tx1)
 
# ----------- 1
alice = generate_key("alice", "a")
bob = generate_key("bob", "b")
caleb = generate_key("caleb", "c")
mary = generate_key("mary", "m")
 
# test transaction.digest
assert len(trans0.digest()) == 64
assert len(trans1.digest()) == 64
 
# test transaction.get_output
assert trans1.get_output(2) == [7.5, "caleb"]
 
# test transaction.get_coins_consumed
assert trans1.get_coins_consumed() == [
    ["db9ca9df899e7", 0],
    ["772fe5688d766", 2],
    ["8c9b6da77d6cb", 1]
]
 
# test transaction.get_sum_spent
assert trans1.get_sum_spent() == (3.2 + 1.4 + 7.5)
 
 
# test_is_signed_by and add_signature
trans1.add_signature("alice", "a")
trans1.add_signature("bob", "b")
assert trans1.is_signed_by("alice") == True
assert trans1.is_signed_by("bob") == True
assert trans1.is_signed_by("caleb") == False
 
 
''' -------------------------------------------------------------------------
 
Do the following tests to your program.
1. Generate four accounts: Alice, Bob, Caleb and Marry
2. Alice mines a new block
3. Alice transfers 10 coins to Bob and 5 coins to Marry
4. Bob mines the next block
5. Bob transfers 25 coins to Caleb and 5 coins to Alice
6. Alice creates a transaction that Caleb transfers 15 coins to Alice, sign this transaction by Alice private key
7. Marry mines the next block
8. Alice and Marry transfer 5 coins to Bob and 5 coins to Caleb
9. Caleb transfers 15 coins to Bob and 5 coins to Marry
10. Alice creates a transaction that Caleb transfers 10 coins to Alice
11. Alice mines the next block
12. Bob transfers 20 coins to Marry and 5 coins to Alice
13. Caleb mines the next block
14. Marry transfers 10 coins to Alice
15. Alice mines the next block and changes her reward to 30 coins
16. Caleb transfers 5 coins to Marry
17. Alice transfers 20 coins to Bob
18. Bob transfers 15 coins to Alice
19. Marry mines the next block
20. Marry tampers with all blocks mined by her to change the rewards to 25 coins
 
'''
 
sb = SBitcoin()
 
# 2. Alice mines a new block
block2 = sb.get_block_from_pending_pool(miners_name="alice")
block2.mine(sb._target)
sb.add_Block_to_Blockchain(block2)
 
# 3. Alice transfers 10 coins to Bob and 5 coins to Marry
tx3 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # coinbase of block2
           {"hash": "COINBASE_BLOCK_2", "num": 0},
           ],
       "coins_created": [
           {"num": 0, "value": 10, "recipient": "bob"},
           {"num": 1, "value": 5, "recipient": "mary"},
           {"num": 2, "value": 5, "recipient": "alice"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx3["coins_consumed"][0]["hash"] = block2._trans_list[0]._data["hash"]
 
trans3 = Transaction(tx3)
trans3.add_signature("alice", "a")
 
sb.register_transaction(trans3)
assert len(sb._pending_pool) == 1
 
# 4. Bob mines the next block
 
block3 = sb.get_block_from_pending_pool(miners_name="bob")
block3.mine(sb._target)
sb.add_Block_to_Blockchain(block3)
assert len(sb._pending_pool) == 0
 
# 5. Bob transfers 25 coins to Caleb and 5 coins to Alice
 
tx4 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # coinbase block3 and tx3
           {"hash": "COINBASE_BLOCK_3", "num": 0},
           {"hash": "TX_3", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 25, "recipient": "caleb"},
           {"num": 1, "value": 5, "recipient": "alice"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx4["coins_consumed"][0]["hash"] = block3._trans_list[0]._data["hash"]
tx4["coins_consumed"][1]["hash"] = tx3["hash"]
 
trans4 = Transaction(tx4)
trans4.add_signature("bob", "b")
sb.register_transaction(trans4)
assert len(sb._pending_pool) == 1
 
# 6. Alice creates a transaction that Caleb transfers 15 coins to Alice, sign this transaction by Alice private key
 
tx5 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx4 hash
           {"hash": "TX_4", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 15, "recipient": "alice"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx5["coins_consumed"][0]["hash"] = tx4["hash"]
 
trans5 = Transaction(tx5)
trans5.add_signature("alice", "a")
sb.register_transaction(trans5)
assert len(sb._pending_pool) == 2
 
# 7. Marry mines the next block
 
block5 = sb.get_block_from_pending_pool(miners_name="mary")
block5.mine(sb._target)
assert len(block5._trans_list) == 2
sb.add_Block_to_Blockchain(block5)
assert len(sb._pending_pool) == 0
 
# 8. Alice and Marry transfer 5 coins to Bob and 5 coins to Caleb
 
tx6 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx3 hash
           {"hash": "TX_3", "num": 1},
           {"hash": "TX_3", "num": 2}
           ],
       "coins_created": [
           {"num": 0, "value": 5, "recipient": "bob"},
           {"num": 1, "value": 5, "recipient": "caleb"}
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx6["coins_consumed"][0]["hash"] = tx3["hash"]
tx6["coins_consumed"][1]["hash"] = tx3["hash"]
 
trans6 = Transaction(tx6)
trans6.add_signature("alice", "a")
trans6.add_signature("mary", "m")
sb.register_transaction(trans6)
assert sb.verify_transaction(trans6)
assert len(sb._pending_pool) == 1
 
# 9. Caleb transfers 15 coins to Bob and 5 coins to Marry
 
tx7 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx4 hash
           {"hash": "TX_4", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 15, "recipient": "bob"},
           {"num": 1, "value": 5, "recipient": "mary"},
           {"num": 2, "value": 5, "recipient": "caleb"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx7["coins_consumed"][0]["hash"] = tx4["hash"]
 
trans7 = Transaction(tx7)
trans7.add_signature("caleb", "c")
assert sb.verify_transaction(trans7)
sb.register_transaction(trans7)
assert len(sb._pending_pool) == 2
 
# 10. Alice creates a transaction that Caleb transfers 10 coins to Alice
 
tx8 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx4 hash
           {"hash": "TX_4", "num": 0},
           ],
       "coins_created": [
           {"num": 0, "value": 10, "recipient": "alice"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx8["coins_consumed"][0]["hash"] = tx4["hash"]
 
trans8 = Transaction(tx8)
# trans8.add_signature("alice", "a")
sb.register_transaction(trans8)
assert len(sb._pending_pool) == 3
 
# 11. Alice mines the next block
 
block6 = sb.get_block_from_pending_pool(miners_name="alice")
 
block6.mine(sb._target)
sb.add_Block_to_Blockchain(block6)
assert sb._head is block6
assert len(block6._trans_list) == 3
assert len(sb._pending_pool) == 0
 
# 12. Bob transfers 20 coins to Marry and 5 coins to Alice
 
tx9 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx7 hash,
           {"hash": "c058d588e3278cd6810e4beb1e73a4c739265843bceb47823224c0ff6c9336e0", "num": 0},
           # tx6 hash
           {"hash": "8f11003ffa0ea8e6e7fb365f7fce278790e71bd429aa56e38c1668a1bdeb028f", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 20, "recipient": "mary"},
           {"num": 1, "value": 5, "recipient": "alice"}
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx9["coins_consumed"][0]["hash"] = tx6["hash"]
tx9["coins_consumed"][1]["hash"] = tx7["hash"]
 
trans9 = Transaction(tx9)
trans9.add_signature("bob", "b")
sb.register_transaction(trans9)
#assert not sb.verify_transaction(trans9)
assert len(sb._pending_pool) == 1
 
# 13. Caleb mines the next block
 
block7 = sb.get_block_from_pending_pool(miners_name="caleb")
block7.mine(sb._target)
sb.add_Block_to_Blockchain(block7)
assert sb._head is block7
assert len(block7._trans_list) == 1
assert len(sb._pending_pool) == 0
 
# 14. Marry transfers 10 coins to Alice
 
tx10 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # block5 coinbase,
           {"hash": "COINBASE_BLOCK_5", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 10, "recipient": "alice"},
           {"num": 1, "value": 10, "recipient": "mary"}
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx10["coins_consumed"][0]["hash"] = block5._trans_list[0]._data["hash"]
 
trans10 = Transaction(tx10)
trans10.add_signature("mary", "m")
sb.register_transaction(trans10)
assert len(sb._pending_pool) == 1
 
# 15. Alice mines the next block and changes her reward to 30 coins
 
block8 = sb.get_block_from_pending_pool(miners_name="alice")
block8._trans_list[0]._data["coins_created"][0]["value"] = 30
block8.mine(sb._target)
sb.add_Block_to_Blockchain(block8)
assert len(sb._pending_pool) == 1
 
# 16. Caleb transfers 5 coins to Marry
 
tx11 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx7 hash,
           {"hash": "TX_7", "num": 2}
           ],
       "coins_created": [
           {"num": 0, "value": 5, "recipient": "alice"}
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx11["coins_consumed"][0]["hash"] = tx7["hash"]
 
trans11 = Transaction(tx11)
trans11.add_signature("caleb", "c")
sb.register_transaction(trans11)
assert len(sb._pending_pool) == 2
 
# 17. Alice transfers 20 coins to Bob
 
tx12 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # coinbase block 6
           {"hash": "505102e721381265bd8e91d205ec98247faf70abd0c546b77c2b49670f761923", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 20, "recipient": "bob"}
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx12["coins_consumed"][0]["hash"] = block6._trans_list[0]._data["hash"]
trans12 = Transaction(tx12)
trans12.add_signature("alice", "a")
sb.register_transaction(trans12)
assert len(sb._pending_pool) == 3
 
#18. Bob transfers 15 coins to Alice
 
tx13 = {"hash": "",
       "type": "PayCoins",
       "coins_consumed": [
           # tx12
           {"hash": "TX_1", "num": 0}
           ],
       "coins_created": [
           {"num": 0, "value": 15, "recipient": "alice"},
           {"num": 0, "value": 5, "recipient": "bob"},
           ],
       "signatures" : [],
       "Timestamp": ""}
 
tx13["coins_consumed"][0]["hash"] = tx12["hash"]
trans13 = Transaction(tx13)
trans13.add_signature("bob", "b")
sb.register_transaction(trans13)
assert len(sb._pending_pool) == 4
 
#19. Marry mines the next block
 
block9 = sb.get_block_from_pending_pool(miners_name="mary")
block9.mine(sb._target)
sb.add_Block_to_Blockchain(block9)
assert len(sb._pending_pool) == 0
assert sb._head is block9
assert len(block9._trans_list) == 4
 
#20. Marry tampers with all blocks mined by her to change the rewards to 25 coins
 
assert sb.verify_blockchain()
 
block5._trans_list[0]._data["coins_created"][0]["value"] = 25
block9._trans_list[0]._data["coins_created"][0]["value"] = 25
 
assert not sb.verify_blockchain()