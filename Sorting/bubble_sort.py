
def bubbleSort(list_):
     
    list_length = len(list_)
 
    # For loop to traverse through all
    # element in an list_ay
    for element1 in range(list_length):
        for element2 in range(0, list_length - element1 - 1):
             
            # Range of the list_ay is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if list_[element2] > list_[element2 + 1]:
                list_[element2], list_[element2 + 1] = list_[element2 + 1], list_[element2]
    return list_ 

def selectionSort(list_):
     
    list_length = len(list_)

    for current_position in range(list_length):
        minimum_element_position = current_position
         
        for next_position in range(current_position + 1, list_length):
             
            # For sorting in descending order
            # for minimum element in each loop
            if list_[next_position] < list_[current_position]:
                minimum_element_position = next_position
 
        if minimum_element_position != current_position:
            list_[current_position], list_[minimum_element_position] = list_[minimum_element_position], list_[current_position]
    return list_ 

def insertion_sort(list_): 

    list_length = len(list_)
    # Outer loop to traverse on len(list1) 
    for current_position in range(1, list_length): 

        current_value = list_[current_position] 

        # Move elements of list1[0 to i-1],
        # which are greater to one position
        # ahead of their current position 
        previous_position = current_position - 1 
        
        while previous_position >= 0 and current_value < list_[previous_position]:
            #print(f"Start WHILE loop:", list_)
            list_[previous_position + 1] = list_[previous_position] 
            previous_position -= 1 
            #print("End WHILE loop:", list_)

        #print("Before LAST statement:", list_)
        list_[previous_position + 1] = current_value 
        #print("After LAST statement:", list_)
    return list_ 

    """
    EXAMPLE: 
        list = [6, 3, 5, 7, 4]
        
    PROCESS:
        CURRENT VALUE: 3
            Start WHILE loop: [6, 3, 5, 7, 4]
            End WHILE loop: [6, 6, 5, 7, 4]

            Before LAST statement: [6, 6, 5, 7, 4]
            After LAST statement: [3, 6, 5, 7, 4]
        
        CURRENT VALUE: 5
            Start WHILE loop: [3, 6, 5, 7, 4]
            End WHILE loop: [3, 6, 6, 7, 4]

            Before LAST statement: [3, 6, 6, 7, 4]
            After LAST statement: [3, 5, 6, 7, 4]
        
        CURRENT VALUE: 7
            Before LAST statement: [3, 5, 6, 7, 4]
            After LAST statement: [3, 5, 6, 7, 4]
    
        CURRENT VALUE: 4
            Start WHILE loop: [3, 5, 6, 7, 4]
            End WHILE loop: [3, 5, 6, 7, 7]

            Start WHILE loop: [3, 5, 6, 7, 7]
            End WHILE loop: [3, 5, 6, 6, 7]

            Start WHILE loop: [3, 5, 6, 6, 7]
            End WHILE loop: [3, 5, 5, 6, 7]

            Before LAST statement: [3, 5, 5, 6, 7]
            After LAST statement: [3, 4, 5, 6, 7]
"""


def merge(left_list, right_list):
    output = []
    position_left, position_right = 0, 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while position_left < len(left_list) and position_right < len(right_list):
        # 9. Compare the elements at every position of both lists during each iteration
        if left_list[position_left] < right_list[position_right]:
            # output is populated with the lesser value
            output.append(left_list[position_left])
            # 10. Move pointer to the right
            position_left += 1
        else:
            output.append(right_list[position_left])
            position_right += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left_list[position_left:])
    output.extend(right_list[position_right:])

    return output

def merge_sort(list_):
    # 1. Store the length of the list
    list_length = len(list_)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list_

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    print(f"[LEFT|BEFORE] List: {list_[:mid_point]}")
    left_partition = merge_sort(list_[:mid_point])
    print(f"[LEFT|AFTER] List: {left_partition}\n")
    
    print(f"[RIGHT|BEFORE] List: {list_[mid_point:]}")
    right_partition = merge_sort(list_[mid_point:])
    print(f"[RIGHT|AFTER] List: {right_partition}\n")

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)

if __name__ == "__main__":
    l = [6,3,5,7,4]

    l1 = merge_sort(l)
