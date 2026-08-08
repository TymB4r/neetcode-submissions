class DoublyLinkedNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes_count = 0
        self.key_to_address = {}
        self.address_to_key = {}
        self.dummy = DoublyLinkedNode()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.key_to_address:
            return -1

        address_to_move = self.key_to_address[key]
        if address_to_move != self.tail:
            address_to_move.prev.next = address_to_move.next
            address_to_move.next.prev = address_to_move.prev
            self.tail.next = address_to_move
            address_to_move.prev = self.tail
            self.tail = self.tail.next
        return address_to_move.val

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_address:
            if self.nodes_count >= self.capacity:
                key_to_delete = self.address_to_key[self.dummy.next]
                self.dummy.next = self.dummy.next.next

                if self.dummy.next:
                    self.dummy.next.prev = self.dummy
                else:
                    self.tail = self.dummy

                del self.address_to_key[self.key_to_address[key_to_delete]]
                del self.key_to_address[key_to_delete]
                self.nodes_count -= 1

            self.tail.next = DoublyLinkedNode(value, self.tail)
            self.tail = self.tail.next
            self.key_to_address[key] = self.tail
            self.address_to_key[self.tail] = key
            self.nodes_count += 1
        else:
            address_to_move = self.key_to_address[key]
            address_to_move.val = value

            if address_to_move != self.tail:
                address_to_move.prev.next = address_to_move.next
                address_to_move.next.prev = address_to_move.prev
                self.tail.next = address_to_move
                address_to_move.prev = self.tail
                self.tail = address_to_move