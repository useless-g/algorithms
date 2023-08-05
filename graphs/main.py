from collections import deque
search_queue = deque()
graph = dict()
graph["you"] = ["alice", 'bob', "claire"]
graph["alice"] = ["peggy"]
graph['bob'] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue += graph["you"]
searched = []
while search_queue:
    print(search_queue)
    person = search_queue.popleft()
    if person not in searched:
        if person == 'jonny':
            print('boy')
            break
        search_queue += graph[person]
        searched.append(person)

