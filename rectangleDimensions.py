# Define rect funtion with length and width 
# Calculate the perimeter, area, and diagonal length
# Print each output

# Import math
import math
# main function
def main():
    length = int(input('Enter length of rectangle '))
    width = int(input('Enter width of rectangle ')) # assigning length and width
    rect(length,width) # Call rect function
# Define rect function
def rect(l,w):   
    perimeter = 2 * (l + w) # Calculate and print perimeter 
    print('The perimeter is ',format(perimeter, ',.1f'), sep='') 
    area = l * w # Calculate the area and print 
    print('Area is ',format(area, ',.2f'), sep='')
    diagonal = (math.sqrt(l**2 + w**2)) # Calculate the diagonal length and print
    print('Diagonal length is ',format(diagonal, ',.1f'), sep='')
                                       
# Call main function to print
main()

