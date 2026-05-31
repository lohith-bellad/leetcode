class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        free_servers = []
        busy_servers = []
        output = []

        for i in range(len(servers)):
            heappush(free_servers, (servers[i], i))

        t = 0
        task_idx = 0

        while task_idx < len(tasks):
            t = max(t, task_idx)

            if not free_servers:
                t = busy_servers[0][0]

            while busy_servers and busy_servers[0][0] <= t:
                _, server_weight, server_idx = heappop(busy_servers)
                heappush(free_servers, (server_weight, server_idx))

            while free_servers and task_idx < len(tasks) and task_idx <= t:
                server_weight, server_idx = heappop(free_servers)
                heappush(busy_servers, (t + tasks[task_idx], server_weight, server_idx))
                output.append(server_idx)
                task_idx += 1

        return output
        """
        freeServers = []
        busyServers = []

        for i in range(len(servers)):
            heapq.heappush(freeServers, (servers[i], i))
        
        output = []
        taskInd = 0
        curTime = 0

        while taskInd < len(tasks):
            curTime = max(curTime, taskInd)
            # If no free servers advance time until server becomes free
            if not freeServers:
                curTime = busyServers[0][0]
                
            # free up busy servers which are done processing
            while busyServers and busyServers[0][0] <= curTime:
                _, weight, ind = heapq.heappop(busyServers)
                heapq.heappush(freeServers, (weight, ind))

            # assign a free server to the task
            weight, ind = heapq.heappop(freeServers)
            heapq.heappush(busyServers, (curTime + tasks[taskInd], weight, ind))
            output.append(ind)

            taskInd += 1
        
        return output