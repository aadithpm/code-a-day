"""
https://www.codewars.com/kata/can-you-get-the-loop/python
"""
def loop_size(node):
    watcher = node
    player = node.next
    size = 0
    while watcher != player:
        watcher = watcher.next
        player = player.next.next
    size = size + 1
    watcher = watcher.next
    while watcher != player:
        size = size + 1
        watcher = watcher.next
    return size
    
        
