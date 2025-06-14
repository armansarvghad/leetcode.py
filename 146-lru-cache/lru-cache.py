class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        
        self.head = {}
        self.tail = {}
        self.head['next'] = self.tail
        self.tail['prev'] = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node['val']
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])
            
        node = {'key': key, 'val': value}
        self._add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            lru_node = self.head['next']
            self._remove(lru_node)
            del self.cache[lru_node['key']]
            
    def _remove(self, node):
        prev = node['prev']
        next = node['next']
        prev['next'] = next
        next['prev'] = prev
        
    def _add(self, node):
        prev = self.tail['prev']
        prev['next'] = node
        self.tail['prev'] = node
        node['prev'] = prev
        node['next'] = self.tail