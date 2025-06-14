class Solution(object):
    def canFinish1(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = [i for i in range(numCourses) if not indegree[i]], set()
        while starts:
            node = starts.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
        return len(visited) == numCourses
        
    def canFinish2(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = deque([i for i in range(numCourses) if not indegree[i]]), set()
        while starts:
            node = starts.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
        return len(visited) == numCourses
    
    def canFinish(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = deque([i for i in range(numCourses) if not indegree[i]]), set()
        for start in starts:
            self.dfs(indegree, adj_list, start, visited)
        return len(visited) == numCourses
    
    def dfs(self, indegree, adj_list, start, visited):
        if start in visited:
            return
        visited.add(start)
        for neigh in adj_list[start]:
            indegree[neigh] -= 1
            if not indegree[neigh]:
                self.dfs(indegree, adj_list, neigh, visited)