class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None
        return self._dfs(self.root, id)

    def _dfs(self, node, id):
        # Base case: if node is None
        if not node:
            return None
        
        # Check if current node matches the id
        if node['id'] == id:
            return node
        
        # Recursively search each child
        for child in node['children']:
            result = self._dfs(child, id)
            if result is not None:  # If found in subtree, return it
                return result
        
        # If not found in this subtree, return None
        return None