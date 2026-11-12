
class ArrayQueue:

    def __init__(self):
        self.queue = []

    # Add element at the rear
    def push(self, x):
        self.queue.append(x)

    # Remove and return the front element
    def pop(self):
        if self.isEmpty():
            return -1

        return self.queue.pop(0)

    # Return the front element
    def peek(self):
        if self.isEmpty():
            return -1

        return self.queue[0]

    # Check whether queue is empty
    def isEmpty(self):
        return len(self.queue) == 0


def main():
    queue = ArrayQueue()

    queue.push(5)
    queue.push(10)

    print("Front element:", queue.peek())
    print("Removed element:", queue.pop())
    print("Is queue empty?", queue.isEmpty())
    print("Front element:", queue.peek())


if __name__ == "__main__":
    main()
