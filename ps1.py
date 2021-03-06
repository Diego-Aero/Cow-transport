###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    cowsCopy=cows.copy()
    #Hacemos una copia para no alterar el original
    
    #Python viejo no admite esta forma de ordenar que diseñé
    sorted_dict={}
    sorted_keys=sorted(cowsCopy, key=cowsCopy.get, reverse=True)
    #The sorted expression will return the list of keys whose values are sorted in order.
    #From there, we can create a new, sorted dictionary:
    for w in sorted_keys:
        sorted_dict[w]=cowsCopy[w]
        #Ordenamos el diccionario
    
    
    totalWeight=0
    result_prev=[]
    result=[]
    i=0
    while sorted_dict!={}:
        for cows in sorted_dict.keys():
            if (totalWeight+sorted_dict[cows])<=limit:
                result_prev.append(cows)
                totalWeight+=sorted_dict[cows]
                #Esto se hace para cada nave/viaje
        for i in result_prev:
            sorted_dict.pop(i)
            #Eliminamos del diccionario las vacas que hemos escogido
        result.append(result_prev)
        #Añadimos las vacas escogidas a la lista que contiene todas las naves/viajes
        result_prev=[]
        totalWeight=0
        #Reiniciamos los valores de peso y vacas del viaje en concreto
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy=cows.copy()
    result_prev=[]
    result=[]
    for ship in (get_partitions(cowsCopy.keys())):
        #Primero un viaje, luego dos, después 3...
        #ship es una lista con las vacas almacenadas:
        #[['c', 'd', 'a', 'b']] luego [['c', 'd', 'b'], ['a']] luego [['c', 'd', 'a'], ['b']]
        band=0
        for config in ship:
            totalWeight=0
            #Vemos las vaca en cada nave/viaje
            for cow in config:
                #cow es un string con el nombre de la vaca, es un item
                totalWeight+=cowsCopy[cow]
            if totalWeight<=limit:
                #Ccon la bandera nos servimos para ver si cada nave no pasa de su peso límite
                #También se puede hacer con un bool overload=True/False
                band+=1
        if band==len(ship):
            #Si hay tantas naves como configuraciones que cumplen con el peso, tenemos resultado válido
            #Falta comprobar que no haya otro mejor con menor número de viajes
            result_prev=ship
        if (len(result_prev)<len(result) or result==[]):
            #Para elegir el menor resultado, puesto que get_partitions no trabaja con dimensiones crecientes
            result=result_prev
    return result

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

'''
cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
'''
compare_cow_transport_algorithms()

