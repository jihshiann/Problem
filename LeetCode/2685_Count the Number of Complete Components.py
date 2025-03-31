class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False] * n
        complete_count = 0
        # �إ�graph(dict)
        # {0 :set(), 1:set()...}
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v) #{0:{1}}
            graph[v].add(u)
        
        # �Ҧ��`�I�ˬd�s�q����
        for i in range(n):
            if not visited[i]:
                #�s�q���I
                con_nodes = []
                stack = [i]
                visited[i] = True
                # �ϥ� DFS 
                while stack:
                    node = stack.pop()
                    #�s�q���I�]�t�ۤv
                    con_nodes.append(node)
                    #�ˬd�s�q���I
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)
                
                # con_nodes���ƶq = �Pi�s�q�`�I��
                r = len(con_nodes)
                # ����Ӹ`�I�A�q�{�{���O�����s�q�]�����Ϫ��w�q�b�u���@�ӳ��I�ɦ��ߡ^
                if r == 1:
                    complete_count += 1
                    continue
                
                
                comp_set = set(con_nodes)
                edge_count = 0
                # �p��o�ӹϪ����
                for node in con_nodes:
                    # �Ȳέp�۳s����
                    for nei in graph[node]:
                        if nei in comp_set:
                            edge_count += 1
                edge_count //= 2  # �C����Q�p��F�⦸
                
                # �����ϻݭn�����
                required = r * (r - 1) // 2
                if edge_count == required:
                    complete_count += 1
        
        return complete_count

        


# ���սd��
if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]
    print(sol.countCompleteComponents(n, edges)) #3
