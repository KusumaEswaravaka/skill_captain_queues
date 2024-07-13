from collections import deque


def timeRequiredToBuy(tickets, k):
    # intialize a deque with indices of people in line
    queue = deque(range(len(tickets)))
    time = 0

    while queue:
        time += 1
        front = queue.popleft()  # remove the person at the front of the queue
        tickets[front] -= 1      # they buy one ticket
        if k == front and tickets[front]== 0: 
            return time   # if target person is done, return elapsed time
        if tickets[front] != 0:
            queue.append(front)  # if they still need tickets, re-add them to the queue
    return time

# Example usage:
tickets = [2, 3, 2]
k = 2
print(timeRequiredToBuy(tickets, k)) #output: 6